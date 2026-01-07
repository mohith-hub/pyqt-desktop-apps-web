import streamlit as st
import pandas as pd
from xml_viewer.logic import parse_xml

st.title("📄 XML Viewer")

file = st.file_uploader("Upload XML File", type=["xml"])

if file:
    data = parse_xml(file)
    df = pd.DataFrame(data)
    st.dataframe(df)
