import streamlit as st
from src.transcribe_file import transcribe_audio_live
from src.upload_file import save_to_word

st.title("Sbobinatore 🎙️")
st.subheader("Upload an audio file to extract text")

if "full_transcription" not in st.session_state:
    st.session_state.full_transcription = ""

uploaded_file = st.file_uploader("Select an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file and not st.session_state.full_transcription:
    with st.spinner("Work in progress, please wait..."):
        live_text_display = st.empty()  
        full_transcription = ""

        try:
            for i, line in enumerate(transcribe_audio_live(uploaded_file)):
                full_transcription += line + "\n"
                unique_key = f"live_transcription_area_{i}"
                live_text_display.text_area("Live extracted transcription:", full_transcription, height=300, key=unique_key)

            st.session_state.full_transcription = full_transcription
            st.success("Transcription completed!")

        except ValueError as e:
            st.error(str(e))

if st.session_state.full_transcription:
    st.text_area("Final transcription:", st.session_state.full_transcription, height=300, key="final_transcription_area")

st.subheader("Download the extracted text")
col1, col2 = st.columns(2)

with col1:
    txt_file = "transcription.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(st.session_state.full_transcription)

    st.download_button(
        label="Download simple text file",
        data=open(txt_file, "rb"),
        file_name=txt_file,
        mime="text/plain",
    )

with col2:
    docx_file = "transcription.docx"
    save_to_word(st.session_state.full_transcription, docx_file)

    st.download_button(
        label="Download word file",
        data=open(docx_file, "rb"),
        file_name=docx_file,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
