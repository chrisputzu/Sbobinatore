from docx import Document

def save_to_word(text, file_name):
    """
    Save the given text to a .docx file.
    
    Args:
        text (str): Text to be saved.
        file_name (str): Name of the .docx file.
    """
    doc = Document()
    doc.add_paragraph(text)
    doc.save(file_name)