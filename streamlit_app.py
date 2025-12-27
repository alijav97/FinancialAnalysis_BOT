"""
Streamlit web application for Financial Analysis Bot
"""
import streamlit as st
from pathlib import Path
import os
from dotenv import load_dotenv
from file_extractor import extract_file_content, get_file_summary
from claude_analyzer import analyze_financial_data, ask_followup_question
from report_generator import export_analysis

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Financial Analysis Bot",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "file_name" not in st.session_state:
    st.session_state.file_name = None

# Header
st.title("📊 Financial Analysis Bot")
st.markdown("Powered by Claude AI - Analyze financial documents instantly")

# Sidebar
with st.sidebar:
    st.header("Settings")
    export_format = st.radio(
        "Export Format:",
        ["Word Document", "Audio (English)"]
    )

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📁 Upload Financial Document")
    
    uploaded_file = st.file_uploader(
        "Choose a financial file (PDF, Excel, CSV)",
        type=["pdf", "xlsx", "xls", "csv"]
    )
    
    if uploaded_file is not None:
        # Save uploaded file temporarily
        temp_dir = Path("temp_uploads")
        temp_dir.mkdir(exist_ok=True)
        temp_file_path = temp_dir / uploaded_file.name
        
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"✓ File uploaded: {uploaded_file.name}")
        
        if st.button("🔍 Analyze Document", key="analyze_btn"):
            with st.spinner("Extracting content..."):
                try:
                    file_content = extract_file_content(str(temp_file_path))
                    file_info = get_file_summary(str(temp_file_path))
                    
                    st.session_state.file_name = file_info['name']
                    
                    with st.spinner("Analyzing with Claude..."):
                        analysis, st.session_state.conversation_history = analyze_financial_data(
                            file_content,
                            file_info['name'],
                            st.session_state.conversation_history
                        )
                        st.session_state.analysis_result = analysis
                    
                    st.success("Analysis complete!")
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

with col2:
    if st.session_state.analysis_result:
        st.subheader("📋 Analysis Results")
        st.markdown(st.session_state.analysis_result)
        
        # Export buttons
        st.divider()
        st.subheader("📤 Export Options")
        
        col_export1, col_export2 = st.columns(2)
        
        with col_export1:
            if st.button("📄 Export as Word", key="word_export"):
                try:
                    output_file = export_analysis(
                        st.session_state.analysis_result,
                        st.session_state.file_name,
                        "word"
                    )
                    with open(output_file, "rb") as f:
                        st.download_button(
                            label="Download Word Document",
                            data=f.read(),
                            file_name=Path(output_file).name,
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )
                    st.success("Word document created!")
                except Exception as e:
                    st.error(f"Error creating Word document: {str(e)}")
        
        with col_export2:
            if st.button("🔊 Export as Audio", key="audio_export"):
                try:
                    output_file = export_analysis(
                        st.session_state.analysis_result,
                        st.session_state.file_name,
                        "audio"
                    )
                    with open(output_file, "rb") as f:
                        st.audio(f.read(), format="audio/mp3")
                    st.success("Audio generated!")
                except Exception as e:
                    st.error(f"Error creating audio: {str(e)}")

# Follow-up questions section
if st.session_state.analysis_result:
    st.divider()
    st.subheader("💬 Ask Follow-up Questions")
    
    followup_question = st.text_area(
        "Ask a question about the analysis:",
        placeholder="E.g., What are the main cost drivers? Should we invest in this?"
    )
    
    if st.button("Ask Question"):
        if followup_question:
            with st.spinner("Processing question..."):
                try:
                    response, st.session_state.conversation_history = ask_followup_question(
                        followup_question,
                        st.session_state.conversation_history
                    )
                    st.info(response)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a question.")

# Footer
st.divider()
st.markdown("""
---
**Financial Analysis Bot** | Powered by Claude AI  
Supported formats: PDF, Excel (.xlsx, .xls), CSV
""")
