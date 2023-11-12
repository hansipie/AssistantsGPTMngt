import os
import streamlit as st
import pandas as pd
from openai import OpenAI

st.set_page_config(layout="wide")
st.title('Assistants Management')

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="open_api_key", type="password")
    if (st.button('Reload')):
        st.rerun()

if not openai_api_key:
    st.warning('Please provide your OpenAI API key')
    st.stop()

client=OpenAI(api_key=openai_api_key)

my_assistants = client.beta.assistants.list()

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
            st.write("delete: ", row['name'], row['id'])
            for file_id in row['file_ids']:
                response_delfiles = client.beta.assistants.files.delete(assistant_id=row['id'], file_id=file_id)
                print("delete file:", response_delfiles)
            response_delassist = client.beta.assistants.delete(row['id'])
            print("delete assistant:", response_delassist)
    st.rerun()
