from .cell import extract_nr_of_tested_media, generate_cells_output
from project_name import get_project_name
from .language_info_metadata import generate_metadata_language_section, get_language_sections
from routing.media_info_routing import get_media_info
from .media_info_metadata import generate_metadata_for_media
from .filler_media_info import get_filler_media_info, generate_fillerslist

def extract_metadata(doc_text, job_book_number):
  # Extracts metadata-related information from the text.
  project_name = get_project_name(doc_text)
  nr_tested_media = extract_nr_of_tested_media(doc_text)
  cells_output = generate_cells_output(nr_tested_media)
  languages = get_language_sections(doc_text)
  media_info = get_media_info(doc_text)
  filler_info, filler_brandproduct_list = get_filler_media_info(doc_text)

  metadata_output = (
        f">>> Project Name: {project_name}\n\n"
        f"---------------------\n"
        f"Metadata Information:\n"
        f"---------------------\n\n"
        f"{cells_output}\n\n"
    )

  metadata_output += generate_metadata_language_section(languages)

  # TestedAds
  metadata_output += generate_metadata_for_media(media_info, job_book_number)

  #FillersList
  metadata_output += generate_fillerslist(filler_info,job_book_number, nr_tested_media)

  return metadata_output