# Sbobinatore 🎙️

Sbobinatore is a web application built with Streamlit that allows you to upload an audio file (MP3, WAV, M4A) and transcribe its content into text. You can view the transcription in real-time and download it as a text file or Word document.

## Features

- **File Upload**: Upload an audio file (MP3, WAV, M4A).
- **Real-time Transcription**: View the transcription as the file is being processed.
- **Download**: Download the transcription as a text (TXT) file or a Word (DOCX) document.

## Requirements

- Python 3.8+
- Streamlit
- Pydub
- Speech Recognition
- Python-docx

To install all the dependencies, run:

```bash
pip install -r requirements.txt
```

# How to Use

1. Run the App: 

    After installing the dependencies, run the following command to start the app:

    ```bash
    streamlit run app.py
    ```

2. Upload Your Audio File: 

    On the app page, click "Choose an audio file" to upload your file. MP3, WAV, and M4A formats are supported.

    View the Transcription: Once the file is uploaded, the system will begin transcribing the audio, and the text will be displayed in real-time.

    Download the Transcription: After the transcription is complete, you can download it as a .txt or .docx file using the download buttons.

    Project Structure
    app.py: The main file for the Streamlit application.
    src/:
    transcribe_file.py: Contains the transcribe_audio_live function, which handles the audio transcription.
    upload_file.py: Contains the save_to_word function, which saves the transcription into a Word file.
    Contributing
    If you would like to contribute to this project, feel free to make a pull request or open an issue.

# License

This project is licensed under the MIT License. It is free to use, modify, and distribute for both personal and commercial purposes.