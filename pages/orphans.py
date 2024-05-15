import streamlit as st
import pandas as pd


def listFiles():
    try:
        response = st.session_state.client.files.list()
        return response
    except Exception as e:
        return e


def listVectorStores():
    try:
        response = st.session_state.client.beta.vector_stores.list()
        return response
    except Exception as e:
        return e

def toastMessage(message):
    if message.deleted:
        st.toast(f"Delete {message.object} {message.id}")  
    else:
        st.toast(f"Error: delete {message.object} {message.id} failed")

def deleteAll():
    with st.spinner("Deleting all..."):
        if not df_files.empty:
            for f in df_files["id"]:
                if f not in st.session_state.idUseCounts:
                    response_delfiles = st.session_state.client.files.delete(f)
                    toastMessage(response_delfiles)
        if not df_vector.empty:
            for v in df_vector["id"]:
                response_delvector = st.session_state.client.beta.vector_stores.delete(v)
                toastMessage(response_delvector)


if "client" not in st.session_state or "idUseCounts" not in st.session_state:
    st.switch_page("assistants.py")


with st.sidebar:
    st.button("Remove All", on_click=deleteAll)

### Files ###

st.write("**Orphan Assistants Files:**")
with st.spinner("Loading files..."):
    fileslist = listFiles()
    filtered_files = [
        {
            "id": f.id,
            "filename": f.filename,
            "created_at": f.created_at,
            "purpose": f.purpose,
        }
        for f in fileslist
        if f.id not in st.session_state.idUseCounts
    ]
    df_files = pd.DataFrame(filtered_files)
    if not df_files.empty:
        df_files["created_at"] = pd.to_datetime(df_files["created_at"], unit="s")
    st.write(df_files)


#######

st.write("**Unused vector stores:**")
with st.spinner("Loading vector store..."):
    vectorStores = listVectorStores()

    filtered_vector = [
        {"id": vs.id, "created_at": vs.created_at, "last_active_at": vs.last_active_at}
        for vs in vectorStores
        if vs.file_counts.total == 0
    ]
    df_vector = pd.DataFrame(filtered_vector)
    if not df_vector.empty:
        df_vector["created_at"] = pd.to_datetime(df_vector["created_at"], unit="s")
        df_vector["last_active_at"] = pd.to_datetime(df_vector["last_active_at"], unit="s")

    st.write(df_vector)
