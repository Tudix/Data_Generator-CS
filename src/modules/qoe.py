import re

def extract_qoe(doc_text, json_settings):
  """
  Extracts QOE-related questions and maps them to predefined responses based on keywords found in the open-ended question section of the document text.

  Parameters:
  - doc_text (str): Full text of the document.
  - json_settings (dict): Settings dictionary loaded from settings.json, containing QOE keywords and their respective codes.

  Returns:
  - list of str: A list of QOE response codes based on the keywords found in the open-ended question section.
  """
  # Initialize an empty list to store QOE response codes
  qoe_responses = []

  # Load QOE keywords and codes from the JSON settings
  qoe_mappings = json_settings.get("qoe_keywords", {})

  # Regular expression to capture open-ended question block
  qoe_regex = re.compile(
      r'\s*Open ended question:\s*\n\s*(.*)',
      re.DOTALL
  )

  match = qoe_regex.search(doc_text)

  if match:
    qoe_text = match.group(1).lower()

    # Iterate through QOE keywords and append the corresponding code if a keyword is found
    for keyword, code in qoe_mappings.items():
      if keyword.lower() in qoe_text:
        qoe_responses.append(code)

    return qoe_responses