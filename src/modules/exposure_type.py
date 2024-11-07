import re

def extract_exposure_type(doc_text, json_settings):
  """
  Extracts the exposure type from the document text based on mappings
  defined in settings.json.

  Parameters:
  - doc_text (str): The document text to search for exposure type.
  - json_settings (dict): Dictionary containing settings loaded from settings.json.

  Returns:
  - str: The code for the exposure type (e.g., "_1", "_2") or None if no match is found.
  """
  exposure_mappings = json_settings.get("exposure_types", {})

  # Regular expression to find the "C|S type" line
  exposure_type_match = re.search(r'C\|S\s*type:\s*(.+)', doc_text, re.IGNORECASE)
  if exposure_type_match:
      exposure_type_line = exposure_type_match.group(1).lower()

      # Search for matching exposure type keywords in line
      for keyword, code in exposure_mappings.items():
          if keyword.lower() in exposure_type_line:
              return code

  return None