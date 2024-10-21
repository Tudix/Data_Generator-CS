import re

def get_filler_media_info(doc_text):
  """
  Extract filler media information for ads based on languages specified in the document text.

  :param doc_text: Full text of the document
  :param job_book_number: Job book number to replace in file names
  :param nr_tested_media: Number of tested media cells
  :return: fillerlist(unformatted data for function generate_fillerslist) , filler_brandproduct_list(unformatted)
  """

  fillerlist = []
  filler_brandproduct_list = []

  # Regular expression to capture filler media information per language
  filler_media_regex = re.compile(
    r'\s*Language(\d+):\s*(\w+)\s*\n'
    r'\s*Filler position 1:\s*(.*?)\s*\n'
    r'\s*Filler position 3:\s*(.*?)\s*\n'
    r'\s*Filler position 4:\s*(.*?)\s*\n\n'
    r'\s*Filler Brand/Product lists:\s*(.*?)(?=\n\n)',
    re.DOTALL
  )

  for match in filler_media_regex.finditer(doc_text):
    filler_media_list = {
      "language_label": match.group(1),
      "language_name": match.group(2),
      "fillers": [match.group(3), match.group(4), match.group(5)]
    }

    fillerlist.append(filler_media_list)

    filler_brandproduct_item = {
      "language_label": match.group(1),
      "language_name": match.group(2),
      "brandproduct": match.group(6)
    }

    filler_brandproduct_list.append(filler_brandproduct_item)

  return fillerlist, filler_brandproduct_list


def generate_fillerslist(fillerlist, job_book_number, nr_tested_media):

  rotation_codes = ['_1', '_3', '_4']

  # Generate output
  output_filler_list = ""

  # Generate the output for each filler ad per language
  for language in fillerlist:

    if len(fillerlist) > 1:
      # Header for each language section
      output_filler_list += f'--- Language{language["language_label"]} - {language["language_name"]} --- START\n\n'

    output_filler_list += (f'FillersList -\ndefine\n{{\n')

    for cell in range(1, nr_tested_media + 1):
        for i, filler in enumerate(language['fillers'], start=1):
            output_filler_list += f'    _{cell * i} "{filler.replace("[JOB_BOOK_NUMBER]", job_book_number)}"\n'
            output_filler_list += f'        [\n            Cell = {cell},\n            rotation_code = "{rotation_codes[i-1]}"\n        ],\n'

    output_filler_list += '};\n\n'

    if len(fillerlist) > 1:
      # Footer for each language section
      output_filler_list += f'--- Language{language["language_label"]} - {language["language_name"]} --- END\n\n'

  return output_filler_list