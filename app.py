import os
import streamlit as st
import pandas as pd
from openai import OpenAI
import os

st.set_page_config(layout="wide")
st.title('Assistants Management')

with st.sidebar:
    if os.environ.get('OPENAI_API_KEY'):
        print("Using OpenAI API key from environment variable")
        openai_api_key = os.environ.get('OPENAI_API_KEY')
    else:
        print("Using OpenAI API key from user input")
        openai_api_key = st.text_input("OpenAI API Key", key="open_api_key", type="password")
    if (st.button('Reload')):
        st.rerun()

if not openai_api_key:
    st.warning('Please provide your OpenAI API key')
    st.stop()

client=OpenAI(api_key=openai_api_key)

def toastMessage(message):
    if message.deleted:
        st.toast(f"Delete {message.object} {message.id}")  
    else:
        st.toast(f"Error: delete {message.object} {message.id} failed")


### Assistants ###

try:
    my_assistants = client.beta.assistants.list()
except (Exception) as e:   
    st.warning(e.message)
    st.stop()

# make a dataframe from the assistants
df_assist = pd.DataFrame(my_assistants.data, columns=['id', 'created_at', 'description', 'file_ids', 'instructions', 'metadata', 'model', 'name', 'object', 'tools'])
df_assist = df_assist.map(lambda x: x[1] if isinstance(x, tuple) else str(x))

# df formating
df_assist['created_at'] = pd.to_datetime(df_assist['created_at'], unit='s')

# add columns for selection tickboxes
df_assist['selected'] = False

# show the dataframe
edited_df = st.data_editor(df_assist[['selected', 'name', 'created_at', 'id', 'file_ids']], column_config={
        "selected": st.column_config.CheckboxColumn(
            "Select",
            help="Select assistant for deletion",
            default=False,
        )
    },
    disabled=['name', 'description', 'id', 'created_at', 'file_ids'],
    hide_index=True)


if (st.button('Delete selected assistants')):
    for index, row in edited_df.iterrows():
        print(row['selected'], row['name'], row['id'])
        if row['selected']:
            for file_id in row['file_ids']:
                try:
                    response_delfiles = client.files.delete(file_id)
                    print("delete file:", response_delfiles)
                    # print type of json variable
                    toastMessage(response_delfiles)
                except (Exception) as e:
                    print("delete file failed:", e)
            response_delassist = client.beta.assistants.delete(row['id'])
            print("delete assistant:", response_delassist)
            toastMessage(response_delassist)
    st.rerun()

### Files ###

my_files = client.files.list()
df_files = pd.DataFrame(my_files.data, columns=['id', 'bytes', 'created_at', 'filename', 'object', 'purpose', 'status', 'status_details'])
df_files = df_files.map(lambda x: x[1] if isinstance(x, tuple) else str(x))

# df formating
df_files['created_at'] = pd.to_datetime(df_files['created_at'], unit='s')

# add columns for selection tickboxes
df_files['selected'] = False

# show the dataframe
edited_df_file = st.data_editor(df_files[['selected', 'filename', 'bytes', 'created_at', 'purpose', 'id']], column_config={
        "selected": st.column_config.CheckboxColumn(
            "Select",
            help="Select file for deletion",
            default=False,
        )
    },
    disabled=['filename', 'bytes', 'created_at', 'purpose', 'id'],
    hide_index=True)

if (st.button('Delete selected files')):
    for index, row in edited_df_file.iterrows():
        print(row['selected'], row['filename'], row['id'])
        if row['selected']:
            try:
                response_delfile = client.files.delete(row['id'])
                print("delete file:", response_delfile)
                toastMessage(response_delfile)
            except (Exception) as e:
                print("delete file failed:", e)
    st.rerun()