import re

def get_project_name(doc_text):
  # Regular expression to find "Project name" and extract the value
  project_name_match = re.search(r'Project\s*name:\s*(.+)', doc_text, re.IGNORECASE)
  if project_name_match:
    project_name = project_name_match.group(1).strip()
    return project_name
  else:
    raise ValueError("Project name not found in the document.")