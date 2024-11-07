import re

def extract_project_name(doc_text):
  """
  Extracts project name information from the document text.

  Args:
    doc_text (str): Complete text of the document.

  Returns:
    dict: Extracted metadata including project name.
  """

  match = re.search(r'Project\s*name:\s*(.+)', doc_text, re.IGNORECASE)

  return match.group(1).strip() if match else None
