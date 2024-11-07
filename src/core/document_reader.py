import docx

def read_document(document_path):
  """
  Reads a Word document and returns the text.
  
  Args:
      document_path (str): Path to the Word document.
      
  Returns:
      str: Document text as a single string.
  """
  doc = docx.Document(document_path)
  return "\n".join([para.text for para in doc.paragraphs])