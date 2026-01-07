import streamlit as st
from search_translate.logic import perform_search, translate_ui_labels

# ---------- DEFAULT UI TEXT ----------
if "ui" not in st.session_state:
    st.session_state.ui = {
        "title": "Search Engine",
        "search": "Search",
        "translate": "Translate UI",
        "placeholder": "Enter search query"
    }

# ---------- UI ----------
st.title(st.session_state.ui["title"])

query = st.text_input(st.session_state.ui["placeholder"])

if st.button(st.session_state.ui["search"]):
    st.info(perform_search(query))

st.markdown("### Translate UI")

lang = st.selectbox(
    "Select language",
    ["en", "fr", "es", "de", "ja", "zh-cn"]
)

if st.button(st.session_state.ui["translate"]):
    st.session_state.ui = translate_ui_labels(lang)
    st.rerun()   # 🔥 THIS LINE IS IMPORTANT
