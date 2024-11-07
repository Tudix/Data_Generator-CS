import re

def extract_category_settings(doc_text):
  """
  Extracts category settings for each language found in the document text.

  Args:
    doc_text (str): Full text from the document.

  Returns:
    dict: A dictionary where each key is a language name and each value is another dictionary
          containing category settings for that language.
  """
  category_settings = {}

  # Regular expression to capture all language-specific category settings
  category_settings_regex = re.compile(
    r'(Language\d+):\s*(\w+).*?\n'
    r'\s*Category\s*tested\s*ad:\s*(.*?)\n'
    r'\s*Category\s*tested\s*ad\s*article:\s*(.*?)\n'
    r'\s*Is_Entertainment:\s*(.*?)\n'
    r'\s*is_tobacco_or_alcohol:\s*(.*?)\n'
    r'\s*Category\s*filler\s*ad:\s*(.*?)\n'
    r'\s*Category\s*filler\s*ad\s*article:\s*(.*?)\n', 
    re.DOTALL)

  # Process each match found by the regular expression
  for match in category_settings_regex.finditer(doc_text):
    category_settings[match.group(2)] = {
      "language_label": match.group(1),
      "category_tested_ad": match.group(3),
      "category_tested_ad_article": match.group(4),
      "is_entertainment": match.group(5),
      "is_tobacco_or_alcohol": match.group(6),
      "category_filler_ad": match.group(7),
      "category_filler_ad_article": match.group(8),
      }

  return category_settings

def generate_metadata_output(category_settings, language):
    """
    Generates metadata output for category settings.

    Args:
      category_settings (dict): Dictionary containing category settings for all languages.
      language (str): Specific language for which metadata is generated.

    Returns:
      str: Formatted metadata output string for the specified language.
    """
    lang_settings = category_settings.get(language)
    if not lang_settings:
      raise ValueError(f"Language '{language}' not found in category settings.")

    return (
      f'QCategory "Hidden - category piping"\n'
      f'categorical [1..1]\n'
      f'{{\n'
      f'    _1 "{lang_settings["category_tested_ad"]}"\n'
      f'}};\n\n'
      f'QCategoryArticle "Hidden - category piping"\n'
      f'categorical [1..1]\n'
      f'{{\n'
      f'    _1 "{lang_settings["category_tested_ad_article"]}"\n'
      f'}};\n\n'
      f'QCategoryFiller "Hidden - category piping for Filler"\n'
      f'categorical [1..1]\n'
      f'{{\n'
      f'    _1 "{lang_settings["category_filler_ad"]}"\n'
      f'}};\n\n'
      f'QCategoryFillerArticle "Hidden - category piping for Filler"\n'
      f'categorical [1..1]\n'
      f'{{\n'
      f'    _1 "{lang_settings["category_filler_ad_article"]}"\n'
      f'}};\n\n'
    )

def generate_routing_output(category_settings, language):
  """
  Generates routing output based on entertainment and tobacco/alcohol settings.

  Args:
    category_settings (dict): Dictionary containing category settings for all languages.
    language (str): Specific language for which routing is generated.

  Returns:
    str: Formatted routing output string for the specified language.
  """
  lang_settings = category_settings.get(language)
  if not lang_settings:
    raise ValueError(f"Language '{language}' not found in category settings.")

  is_entertainment_value = "_1" if lang_settings["is_entertainment"] == "yes" else "_2"
  tob_alco_value = "_1" if lang_settings["is_tobacco_or_alcohol"] == "yes" else "_2"

  return (
    f'isEntertainment.Response = {{{is_entertainment_value}}}\n\n'
    f'TobAlcoBevCateg.Response = {{{tob_alco_value}}}\n\n'
  )

def generate_category_outputs(category_settings, language):
  """
  Generates both metadata and routing outputs for a specified language.

  Args:
    category_settings (dict): Dictionary containing category settings for all languages.
    language (str): Specific language for which outputs are generated.

  Returns:
    tuple: A tuple containing metadata and routing output strings.
  """
  metadata_output = generate_metadata_output(category_settings, language)
  routing_output = generate_routing_output(category_settings, language)

  return metadata_output, routing_output