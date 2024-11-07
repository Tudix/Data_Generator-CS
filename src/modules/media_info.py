import re

def get_media_info(doc_text):
  """
  Extracts media information for each language from the document text.

  Args:
    doc_text (str): Full text from the document.

  Returns:
    dict: Dictionary containing media information for each language, with multiple ads.
  """
  
  media_info = {}

  # Regular expression to capture media information per language
  media_info_regex = re.compile(
    r'\s*Language(\d+):\s*(\w+)\s*\n'
    r'((?:\s*File name used in the URL:\s*(.*?)\s*\n'
    r'\s*Name to be displayed in Entropik dashboard:\s*(.*?)\s*\n'
    r'\s*Groups:\s*(.*?)\s*\n'
    r'\s*DEIHID:\s*(\d+)\s*\n'
    r'\s*GROUP_NAME:\s*(\w*)\s*\n'
    r'\s*REPRESENTED:\s*(\w*)\s*\n'
    r'\s*DEIStat2:\s*(\d+)\s*\n'
    r'\s*Finish level:\s*(\w+)\s*\n'
    r'\s*Screenshots:\s*(.*?)\s*\n\n)+)',
    re.DOTALL
  )

  for match in media_info_regex.finditer(doc_text):
    language = match.group(2)

    # Initialize a list of ads if the language key is not yet in media_info
    if language not in media_info:
      media_info[language] = {"language_label": match.group(1), "ads": []}

    # Capture each ad using inner regex
      ad_regex = re.compile(
        r'\s*File name used in the URL:\s*(.*?)\s*\n'
        r'\s*Name to be displayed in Entropik dashboard:\s*(.*?)\s*\n'
        r'\s*Groups:\s*(.*?)\s*\n'
        r'\s*DEIHID:\s*(\d+)\s*\n'
        r'\s*GROUP_NAME:\s*(\w*)\s*\n'
        r'\s*REPRESENTED:\s*(\w*)\s*\n'
        r'\s*DEIStat2:\s*(\d+)\s*\n'
        r'\s*Finish level:\s*(\w+)\s*\n'
        r'\s*Screenshots:\s*(.*?)\s*\n\n',
        re.DOTALL
      )

    for ad_match in ad_regex.finditer(match.group(3)):
      media_info[language]["ads"].append({
        "file_name": ad_match.group(1),
        "dashboad_name": ad_match.group(2),
        "groups": ad_match.group(3),
        "deihid": ad_match.group(4),
        "group_name": ad_match.group(5),
        "represented": ad_match.group(6),
        "deistat2": ad_match.group(7),
        "finish_level": ad_match.group(8),
        "telepics": ad_match.group(9).splitlines(),
    })

  return media_info

def generate_metadata_for_media(media_info, language, job_book_number):
  """
  Generates metadata output for tested ads for a given language.

  Args:
    media_info (dict): Dictionary containing media information for each language.
    language (str): The language key to generate metadata for.
    job_book_number (str): The job book number to replace in file names.

  Returns:
    str: Formatted metadata output for the specified language.
  """

  metadata_output = "TestedAdsList -\ndefine\n{\n"

  # Check if the language exists in media_info
  if language in media_info:
    ads_entries = []
    for index, ad in enumerate(media_info[language]["ads"], start=1):
      file_name = ad["file_name"].replace("[JOB_BOOK_NUMBER]", job_book_number)
      ads_entries.append(
        f'    _{index} "{file_name}"\n'
        f'        [\n'
        f'            Cell = {index},\n'
        f'            rotation_code = "_2"\n'
        f'        ]'
      )

  else:
    raise ValueError(f"Language '{language}' not found in media information.")

  metadata_output += ',\n'.join(ads_entries) + "\n};\n\n"

  return metadata_output

def generate_routing_for_media(media_info, language):
  """
  Generates routing information for each ad in the specified language.

  Args:
    media_info (dict): Dictionary containing media information for each language.
    language (str): The language key to generate routing information for.

  Returns:
    str: Formatted routing output for the specified language.
  """

  if language not in media_info:
    raise ValueError(f"Language '{language}' not found in media information.")

  routing_output = ""

  for index,media in enumerate(media_info[language]["ads"], start=1):

    routing_output += f"Tested AD{index}:\n"

    formatted_groups = ','.join([f'_{group.strip()}' for group in media["groups"].split(',')])

    # Groups, DEIHID, DEIStat2
    routing_output += (
        f'Groups.Response = {{{formatted_groups}}}\n'
        f'DEIHID.Response = {{_{media["deihid"]}}}\n'
        f'DEIStat2.Response = {{_{media["deistat2"]}}}\n'
    )

    # Finish level
    finish_level_response = "_1" if media["finish_level"].lower() == "finished" else "_2"
    routing_output += f'QFinishUnfinish.Response = {{{finish_level_response}}}\n'

    # Telepics count
    screenshot_count = len(media["telepics"])
    routing_output += f'telepic_pictures = {screenshot_count}\n\n'


  return routing_output