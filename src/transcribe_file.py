import os
import tempfile
from faster_whisper import WhisperModel

def transcribe_audio_live(uploaded_file):
    """
    Transcribe an uploaded audio file line by line and yield each segment.
    
    Args:
        uploaded_file (UploadedFile): Audio file uploaded through Streamlit.
        
    Yields:
        str: Transcribed segment of text.
    """
    file_extension = os.path.splitext(uploaded_file.name)[-1]
    if file_extension not in [".mp3", ".wav", ".m4a"]:
        raise ValueError("Unsupported file format. Please upload an MP3, WAV, or M4A file.")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    model = WhisperModel("base", device="cpu")
    
    segments, _ = model.transcribe(temp_file_path)
    for segment in segments:
        yield segment.text 