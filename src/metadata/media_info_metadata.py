import re

def generate_metadata_for_media(media_info, job_book_number):
  """
  Generate metadata output for the media information extracted from the document.

  :param media_info: List of dictionaries containing media details for each language
  :return: Formatted metadata output for each language section
  """

  metadata_output = ""

  for media in media_info:

    if len(media_info) > 1:
      # Header for each language section
      metadata_output += f'--- {media["language_label"]} - {media["language_name"]} --- START\n\n'

    # File and dashboard name for the tested ads
    metadata_output += (
        f'TestedAdsList -\n'
        f'define\n'
        f'{{\n'
        f'    _1 "{media["file_name"].replace("[JOB_BOOK_NUMBER]", job_book_number)}"\n'
        f'        [\n'
        f'            Cell = 1,\n'
        f'            rotation_code = "_2"\n'
        f'        ]\n'
        f'}};\n\n'
    )

    if len(media_info) > 1:
      # Footer for each language section
      metadata_output += f'--- {media["language_label"]} - {media["language_name"]} --- END\n\n'

  return metadata_output