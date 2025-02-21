import re

def get_filler_media_info(doc_text):
  """
  Extracts filler media information for ads based on languages specified in the document text.

  Args:
    doc_text (str): Full text from the document.

  Returns:
    tuple: Two dictionaries -
      fillerlist (dict): Contains unformatted data for filler ads per language.
      filler_brandproduct_list_raw (dict): Contains unformatted brand/product data per language.
  """

  fillerlist = {}
  filler_brandproduct_list_raw = {}

  # Regular expression to capture filler media information per language
  filler_media_regex = re.compile(
    r'\s*Language(\d+):\s*(\w+)\s*\n'
    r'\s*Filler position 1:\s*(.*?)\s*\n'
    r'\s*Filler position 3:\s*(.*?)\s*\n'
    r'\s*Filler position 4:\s*(.*?)\s*\n+'
    r'\s*Filler Brand/Product lists:\s*(.*?)\n\n',
    re.DOTALL
  )

  for match in filler_media_regex.finditer(doc_text):
    language = match.group(2)
    language_label = match.group(1)
    fillers_ads = [match.group(3), match.group(4), match.group(5)]
    brand_product = match.group(6)

    fillerlist[language] = {
      "language_label": language_label,
      "fillers_ads": fillers_ads
    }

    filler_brandproduct_list_raw[language] = {
      "language_label": language_label,
      "brandproduct": brand_product
    }


  return fillerlist, filler_brandproduct_list_raw


def generate_fillerslist(fillerlist, language, job_book_number, nr_tested_media):
    """
    Generates metadata output for filler ads for a specified language.

    Args:
      fillerlist (dict): Contains filler media information.
      language (str): The language key for which metadata is generated.
      job_book_number (str): Job book number to replace in file names.
      nr_tested_media (int): Number of tested media cells.

    Returns:
      str: Formatted metadata output for filler ads.

    Raises:
      ValueError: If the specified language is not found in the fillerlist dictionary.
    """
    rotation_codes = ['_1', '_3', '_4']
    filler_list_entries = []
    output_filler_list = "FillersList -\ndefine\n{\n"

    try:
      fillers_ads = fillerlist[language]["fillers_ads"]
      counter = 1
      for cell in range(1, nr_tested_media + 1):
        for i, filler in enumerate(fillers_ads):
          file_name = filler.replace("[JOB_BOOK_NUMBER]", job_book_number)
          filler_list_entries.append(
            f'    _{counter} "{file_name}"\n'
            f'        [\n'
            f'            Cell = {cell},\n'
            f'            rotation_code = "{rotation_codes[i]}"\n'
            f'        ]'
          )
          counter += 1

      output_filler_list += ',\n'.join(filler_list_entries) + '\n};\n\n'

    except KeyError:
        raise ValueError(f"Language '{language}' not found in filler media information.")

    return output_filler_list