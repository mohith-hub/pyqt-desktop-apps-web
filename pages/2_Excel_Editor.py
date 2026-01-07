import streamlit as st
from excel_editor.logic import load_excel, save_excel

st.title("📊 Excel Editor")

file = st.file_uploader("Upload Excel File", type=["xlsx"])

if file:
    df = load_excel(file)
    edited_df = st.data_editor(df, num_rows="dynamic")

    st.download_button(
        "Download Updated Excel",
        save_excel(edited_df),
        file_name="updated.xlsx"
    )
