import streamlit as st
from src.pipeline import summarize_text

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------
# Header
# -------------------------------
st.markdown(
    """
    # 🧠 AI Text Summarizer
    ### Transform long articles into short, meaningful summaries in seconds

    This application uses **Natural Language Processing (NLP)** techniques to generate concise summaries from long text inputs.

    ---
    """
)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.header("📌 About the Project")

    st.markdown("""
    **AI Text Summarizer**

    This project demonstrates the use of **NLP pipelines** to automatically summarize long text content.

    **Tech Stack**
    - Python
    - Streamlit
    - NLP Models
    - Machine Learning

    **Use Cases**
    - Summarizing articles
    - Research papers
    - News content
    - Reports
    """)

    st.markdown("---")
    st.markdown("👨‍💻 Built for portfolio demonstration")

# -------------------------------
# Main Layout
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Input Text")

    text = st.text_area(
        "Paste your article here",
        height=300,
        placeholder="Enter a long article, blog post, or report..."
    )

with col2:
    st.subheader("✂️ Generated Summary")

    summary_placeholder = st.empty()

# -------------------------------
# Button
# -------------------------------
st.markdown("")

if st.button("🚀 Generate Summary", use_container_width=True):

    if text.strip() == "":
        st.warning("⚠️ Please enter some text to summarize.")
    else:
        with st.spinner("AI is generating summary..."):

            summary = summarize_text(text)

        summary_placeholder.success(summary)

# -------------------------------
# How it Works
# -------------------------------
st.markdown("---")

with st.expander("⚙️ How This Works"):
    st.markdown("""
    1. User inputs a long piece of text.
    2. The text is passed to an **NLP summarization pipeline**.
    3. The model extracts the most relevant information.
    4. A concise summary is generated and displayed.

    This helps save time when reading long documents.
    """)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        🚀 Built with <b>Streamlit</b> | AI & NLP Demo Project
    </div>
    """,
    unsafe_allow_html=True
)