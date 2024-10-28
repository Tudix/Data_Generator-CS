from metadata import extract_metadata
from routing import extract_routing
import re

def get_languages(doc_text):
  languages = {}

  # Regular expression to capture languages
  languages_regex = re.findall(r'\s*Language of survey:\s*([\w\s,]+)\n', doc_text, re.IGNORECASE)

  languages_list = [lang.strip() for lang in languages_regex[0].split(',')]

  for index, lang in enumerate(languages_list, start = 1):
    lang_key = f'Language{index} - {lang}'
    if lang_key not in languages:
      languages[lang_key] = None

  return languages

def generate_all_outputs(doc_text, job_book_number):
  # Generates all outputs by combining results from metadata.py and routing.py
  outputs = {}
  outputs['routing'], hidlevels, brandproduct = extract_routing(doc_text)
  outputs['metadata'] = extract_metadata(doc_text, job_book_number, hidlevels, brandproduct)
  return outputs