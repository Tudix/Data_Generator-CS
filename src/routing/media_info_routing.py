import re

def get_media_info(doc_text):
  """
  Extract media information for tested ads based on languages specified in the document text.

  :param doc_text: Full text of the document
  :return: A list of dictionaries containing media information per language
  """
  media_info = []

  # Regular expression to capture media information per language
  media_info_regex = re.compile(
    r'\s*Language(\d+):\s*(\w+)\s*\n'
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

  for match in media_info_regex.finditer(doc_text):
    media_info_section = {
      "language_label": match.group(1),
      "language_name": match.group(2),
      "file_name": match.group(3),
      "dashboad_name": match.group(4),
      "groups": match.group(5),
      "deihid": match.group(6),
      "group_name": match.group(7),
      "represented": match.group(8),
      "deistat2": match.group(9),
      "finish_level": match.group(10),
      "telepics": match.group(11).splitlines(),
    }
    media_info.append(media_info_section)

  return media_info



def generate_routing_for_media(media_info):
  """
  Generate routing output for the media information extracted from the document.

  :param media_info: List of dictionaries containing media details for each language
  :return: Formatted routing output for each language section
  """

  routing_output = ""

  for media in media_info:

    if len(media_info) > 1:
      # Header for each language section
      routing_output += f'--- {media["language_label"]} - {media["language_name"]} --- START\n\n'

    formatted_groups = ','.join([f'_{group.strip()}' for group in media["groups"].split(',')])

    # Groups, DEIHID, DEIStat2
    routing_output += (
        f'Groups.Response = {{{formatted_groups}}}\n'
        f'DEIHID.Response = {{_{media["deihid"]}}}\n'
        f'DEIStat2.Response = {{_{media["deistat2"]}}}\n\n'
    )

    # Finish level
    finish_level_response = "_1" if media["finish_level"].lower() == "finished" else "_2"
    routing_output += f'QFinishUnfinish.Response = {{{finish_level_response}}}\n\n'

    # Telepics count
    screenshot_count = len(media["telepics"])
    routing_output += f'telepic_pictures = {screenshot_count}\n\n'

    if len(media_info) > 1:
      # Footer for each language section
      routing_output += f'--- {media["language_label"]} - {media["language_name"]} --- END\n\n'

  return routing_output
