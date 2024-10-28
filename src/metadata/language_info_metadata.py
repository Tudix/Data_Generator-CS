import re

def get_language_sections(doc_text):
  category_settings = []

  # Regular expression to capture first section of languages
  category_settings = re.compile(
    r'(Language\d+):\s*(\w+).*?\n'
    r'\s*Category\s*tested\s*ad:\s*(.*?)\n'
    r'\s*Category\s*tested\s*ad\s*article:\s*(.*?)\n'
    r'\s*Is_Entertainment:\s*(.*?)\n'
    r'\s*is_tobacco_or_alcohol:\s*(.*?)\n'
    r'\s*Category\s*filler\s*ad:\s*(.*?)\n'
    r'\s*Category\s*filler\s*ad\s*article:\s*(.*?)\n', 
    re.DOTALL)

  for match in category_settings.finditer(doc_text):
    category_settings_info = {
      "language_label": match.group(1),
      "language_name": match.group(2),
      "category_tested_ad": match.group(3),
      "category_tested_ad_article": match.group(4),
      "is_entertainment": match.group(5),
      "is_tobacco_or_alcohol": match.group(6),
      "category_filler_ad": match.group(7),
      "category_filler_ad_article": match.group(8),
    }
    category_settings.append(category_settings_info)

  return category_settings

def generate_metadata_language_section(category_settings):
  metadata_output = ""

  for language in category_settings:

    if len(category_settings) > 1:
      metadata_output += f'--- {language["language_label"]} - {language["language_name"]} --- START\n\n' 

    metadata_output += (
      f'QCategory "Hidden - category piping"\n'
      f'categorical [1..1]\n'
      f'{{\n'
      f'    _1 "{language["category_tested_ad"]}"\n'
      f'}};\n\n'
      f'QCategoryArticle "Hidden - category piping"\n'
      f'categorical [1..1]\n'
      f'{{\n'
      f'    _1 "{language["category_tested_ad_article"]}"\n'
      f'}};\n\n'
      f'QCategoryFiller "Hidden - category piping for Filler"\n'
      f'categorical [1..1]\n'
      f'{{\n'
      f'    _1 "{language["category_filler_ad"]}"\n'
      f'}};\n\n'
      f'QCategoryFillerArticle "Hidden - category piping for Filler"\n'
      f'categorical [1..1]\n'
      f'{{\n'
      f'    _1 "{language["category_filler_ad_article"]}"\n'
      f'}};\n\n'
    )

    if len(category_settings) > 1:
      metadata_output += f'--- {language["language_label"]} - {language["language_name"]} --- END\n\n' 

  return metadata_output
