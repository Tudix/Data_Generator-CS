import re

def extract_languages(doc_text):
  """
  Extracts a dictionary of languages from the document text with their corresponding index.

  Args:
      doc_text (str): The text content of the document.

  Returns:
      dict: A dictionary with language names as keys and index as values.
  """
  languages = {}

  language_match = re.search(r'\s*Language of survey:\s*([\w\s,]+)\n', doc_text, re.IGNORECASE)

  languages_list = [lang.strip() for lang in language_match.group(1).split(',')]

  for index, lang in enumerate(languages_list, start=1):
    if lang not in languages:
      languages[lang] = {"index": index}

  return languages