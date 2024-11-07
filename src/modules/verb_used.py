import re

def extract_verb_used(doc_text, json_settings):
  """
  Extracts the verb used in the tested ad from the document text and maps it to a code based on predefined mappings in the settings file.

  Parameters:
  - doc_text (str): The document text to search for the verb used in the tested ad.
  - json_settings (dict): Settings dictionary loaded from settings.json, containing verb mappings.

  Returns:
  - str: The code for the matched verb if found, based on verb mappings in settings.json.

  Raises:
  - ValueError: If 'Verb used tested ad' line is not found in the document text.
  """
  # Load verb mappings from settings
  verb_mappings = json_settings.get("verb_used", {})

  # Regular expression to find "Verb used tested ad:" line and extract the verb
  verb_match = re.search(r'Verb\s*used\s*tested\s*ad:\s*(.+)', doc_text, re.IGNORECASE)
  if verb_match:
    verb = verb_match.group(1).strip().lower()

    # Search for a matching verb keyword in mappings
    for keyword, code in verb_mappings.items():
      if keyword.lower() in verb:
        return code

  # Raise an error if 'Verb used tested ad' line is not found or no mapping is matched
  raise ValueError("'Verb used tested ad' not found or no matching verb in mappings.")