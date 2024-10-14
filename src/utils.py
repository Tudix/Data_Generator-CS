from docx import Document
import os

def read_word_document(file_path):
  # Reads the text from a Word document and returns it as a string.
  doc = Document(file_path)
  doc_text = []
  for paragraph in doc.paragraphs:
    doc_text.append(paragraph.text)
  return "\n".join(doc_text)


def create_folder(folder_name):
  # Creates the folder if it doesn't exist.
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder created: {folder_name}")
  else:
    print(f"Folder already exists: {folder_name}")