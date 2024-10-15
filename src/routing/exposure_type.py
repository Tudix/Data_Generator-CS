import re

def get_exposure_type(doc_text):
  # Regular expression to find the "C|S type" line
  exposure_type_match = re.search(r'C\|S\s*type:\s*(.+)', doc_text, re.IGNORECASE)
  if exposure_type_match:
    exposure_type_line = exposure_type_match.group(1).lower()
    if any(keyword in exposure_type_line for keyword in ['standard', 'fc', 'tv']):
      return "_1"
    elif 'digital' in exposure_type_line:
      return "_2"
  return None