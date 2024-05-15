from dataclasses import dataclass
from enum import Enum
from typing import List
import streamlit as st
import pandas as pd
from openai import OpenAI
import os


class Tool(Enum):
    CODEINTERPRETER = "code_interpreter"
    FILESEARCH = "file_search"
    function = "function"


@dataclass
class ToolFiles:
    id: str
    filename: str
    purpose: str
    vstore_id: str = None


@dataclass
class ToolResources:
    vector_ids: List[str]
    files: List[ToolFiles]


@dataclass
class Assistant:
    id: str
    name: str
    description: str
    instructions: str
    tools: List[Tool]
    tool_resources: ToolResources


def toastMessage(message):
    if message.deleted:
        st.toast(f"Delete {message.object} {message.id}")
    else:
        st.toast(f"Error: delete {message.object} {message.id} failed")


def listAssistants():
    try:
        response = st.session_state.client.beta.assistants.list()
        return response
    except Exception as e:
        print(e)
        return e


def deleteAssistant(assistant_id):
    try:
        response = st.session_state.client.beta.assistants.delete(assistant_id)
        return response
    except Exception as e:
        return e


def deleteFile(file_id):
    try:
        response = st.session_state.client.files.delete(file_id)
        return response
    except Exception as e:
        return e


def deleteVectorStore(vector_store_id):
    try:
        response = st.session_state.client.beta.vector_stores.delete(vector_store_id)
        return response
    except Exception as e:
        return e


def updateIdUseCounts(id):
    if id not in st.session_state.idUseCounts:
        st.session_state.idUseCounts[id] = 1
    else:
        st.session_state.idUseCounts[id] += 1


def getFileDetails(file_id, vector_store_id=None):
    file_details = st.session_state.client.files.retrieve(file_id)
    file: ToolFiles = ToolFiles(
        id=file_details.id,
        filename=file_details.filename,
        purpose=file_details.purpose,
        vstore_id=vector_store_id,
    )
    return file


def getFileFromVectorStore(vector_store_ids):
    files = []
    for vstore in vector_store_ids:
        vector_store_files = st.session_state.client.beta.vector_stores.files.list(
            vector_store_id=vstore
        )
        files.extend([getFileDetails(f.id, vstore) for f in vector_store_files.data])
    return files


def setData(assistants):
    data: List[Assistant] = []
    for assistant in assistants:

        tools: List[Tool] = [Tool(t.type) for t in assistant.tools]

        if assistant.tool_resources.code_interpreter:
            resources: ToolResources = ToolResources(
                vector_ids=[],
                files=[
                    getFileDetails(f)
                    for f in assistant.tool_resources.code_interpreter.file_ids
                ],
            )
            for f in resources.files:
                updateIdUseCounts(f.id)
        elif assistant.tool_resources.file_search:
            resources = ToolResources(
                vector_ids=assistant.tool_resources.file_search.vector_store_ids,
                files=getFileFromVectorStore(
                    assistant.tool_resources.file_search.vector_store_ids
                ),
            )
            for f in resources.files:
                updateIdUseCounts(f.id)
            for v in resources.vector_ids:
                updateIdUseCounts(v)
        else:
            resources = ToolResources(vector_ids=[], files=[])
        data.append(
            Assistant(
                id=assistant.id,
                name=assistant.name,
                description=assistant.description,
                instructions=assistant.instructions,
                tools=tools,
                tool_resources=resources,
            )
        )
    return data


st.set_page_config(layout="wide")
st.title("Assistants Management")

if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""
if "client" not in st.session_state:
    st.session_state.client = None
if "idUseCounts" not in st.session_state:
    st.session_state.idUseCounts = {}

with st.sidebar:
    if os.environ.get("OPENAI_API_KEY"):
        print("Using OpenAI API key from environment variable")
        st.session_state.openai_api_key = os.environ.get("OPENAI_API_KEY")
    else:
        print("Using OpenAI API key from user input")
        st.session_state.openai_api_key = st.text_input(
            "OpenAI API Key", value=st.session_state.openai_api_key , key="open_api_key", type="password", 
        )
    if st.button("Reload"):
        st.rerun()

if not st.session_state.openai_api_key:
    st.warning("Please provide your OpenAI API key")
    st.stop()

st.session_state.client = OpenAI(api_key=st.session_state.openai_api_key)

### Assistants ###

with st.spinner("Loading assistants..."):
    my_assistants = listAssistants()
    print("ici ")
    print(my_assistants)
    data = setData(my_assistants.data)

# with st.spinner("Loading files and vector stores..."):
#     fileslist = listFiles()
#     vector_stores = listVectorStores()


for assistant in data:
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.write("**Assistant Name**: ", assistant.name)
                st.write(" - ID: ", assistant.id)
                st.button(
                    "Delete",
                    on_click=deleteAssistant,
                    args=[assistant.id],
                    key=assistant.id,
                )
        with col2:
            with st.container(border=True):
                st.write("**Description**: ", assistant.description)
                st.write("**Instruction**: ", assistant.instructions)
                st.write("**Tools**:")
                with st.container(border=True):
                    for t in assistant.tools:
                        st.write(" - Type: ", t.value)
                st.write("**Tool Resources**:")
                with st.container(border=True):
                    for vstore in assistant.tool_resources.vector_ids:
                        st.write("Vector store: ID:", vstore)

                    st.write("Files:")
                    files = [f for f in assistant.tool_resources.files]
                    df = pd.DataFrame(files, columns=["filename", "id"])
                    st.write(df)


# st.write("**useCounts:**", idUseCounts)

# st.write("**Files:**", listFiles())

# st.write("**Vector Stores:**", listVectorStores())
