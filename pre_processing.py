import os

from IPython.display import JSON

import json
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError

from unstructured.partition.html import partition_html
from unstructured.partition.pptx import partition_pptx
from unstructured.staging.base import dict_to_elements, elements_to_json
load_dotenv()
DLAI_API_KEY = os.getenv("DLAI_API_KEY")
DLAI_API_URL = os.getenv("DLAI_API_URL")

s = UnstructuredClient(
    api_key_auth=DLAI_API_KEY,
    server_url=DLAI_API_URL,
)

st.image()
