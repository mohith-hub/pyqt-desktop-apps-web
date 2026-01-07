import streamlit as st
from translator.logic import translate_text

st.title("🌐 Language Translator")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-cn",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru"
}

lang = st.selectbox("Select language", list(languages.keys()))

if st.button("Translate"):
    st.success(translate_text(text, languages[lang]))
