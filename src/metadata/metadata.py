from .cell import get_cell
from project_name import get_project_name
from .language_info_metadata import generate_metadata_language_section, get_language_sections
from routing.media_info_routing import get_media_info
from .media_info_metadata import generate_metadata_for_media

def extract_metadata(doc_text, job_book_number):
  # Extracts metadata-related information from the text.
  project_name = get_project_name(doc_text)
  cell_output = get_cell(doc_text)
  languages = get_language_sections(doc_text)
  media_info = get_media_info(doc_text)

  metadata_output = (
        f">>> Project Name: {project_name}\n\n"
        f"---------------------\n"
        f"Metadata Information:\n"
        f"---------------------\n\n"
        f"{cell_output}\n\n"
    )

  metadata_output += generate_metadata_language_section(languages)

  # TestedAds
  metadata_output += generate_metadata_for_media(media_info, job_book_number)

  return metadata_output