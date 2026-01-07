import streamlit as st

st.set_page_config(
    page_title="PyQt Desktop Apps – Web Version",
    layout="wide"
)

st.title("PyQt Desktop Applications (Web Version)")

st.markdown(
    """
    This is a collection of **desktop applications originally built using PyQt**  
    and later **re-engineered into web applications using Streamlit**.

    👉 You can either **click a project below** or use the **sidebar** to navigate.
    """
)

st.markdown("---")

# ---------- CARD STYLE ----------
st.markdown(
    """
    <style>
   .card {
    background-color: #111827;
    padding: 20px;
    border-radius: 16px;
    min-height: 220px;
    margin-bottom: 20px;   /* 👈 THIS FIXES IT */
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}

    .card h3 {
        margin-top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- CARDS ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>📄 XML Viewer</h3>
            <p>Upload and visualize structured XML student data in a table format.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Open XML Viewer"):
        st.switch_page("pages/1_XML_Viewer.py")

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>📊 Excel Editor</h3>
            <p>Edit Excel files directly in the browser and download updated versions.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Open Excel Editor"):
        st.switch_page("pages/2_Excel_Editor.py")

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>🌐 Translator</h3>
            <p>Translate text into multiple languages using an online translation engine.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Open Translator"):
        st.switch_page("pages/3_Translator.py")

with col4:
    st.markdown(
        """
        <div class="card">
            <h3>🔍 Search & Translate</h3>
            <p>Search input with dynamic UI translation support.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Open Search App"):
        st.switch_page("pages/4_Search_Translate.py")
