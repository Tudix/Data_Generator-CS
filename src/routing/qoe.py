import re

def get_qoe(doc_text):
  """
  Extract QOE-related questions and map them to predefined responses based on keywords found in the text.
  
  :param doc_text: Full text of the document
  :return: A list of QOE response codes based on the keywords found in the open-ended question section
  """
  qoe_responses = []

  # Regular expression to capture open-ended question block
  qoe_regex = re.compile(
      r'\s*Open ended question:\s*\n\s*(.*)',
      re.DOTALL
  )

  match = qoe_regex.search(doc_text)

  if match:
    qoe_text = match.group(1).lower()

    # Check for 'reactions', 'tell a friend', and 'main idea'
    if '(reactions)' in qoe_text:
      qoe_responses.append("_1")
    if '(tell a friend)' in qoe_text:
      qoe_responses.append("_2")
    if '(main idea)' in qoe_text:
      qoe_responses.append("_3")

  return qoe_responses