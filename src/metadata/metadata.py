from .cell import extract_nr_of_tested_media, generate_cells_output
from project_name import get_project_name
from .language_info_metadata import generate_metadata_language_section, get_language_sections
from routing.media_info_routing import get_media_info
from .media_info_metadata import generate_metadata_for_media
from .filler_media_info import get_filler_media_info, generate_fillerslist
from .brand_product_lists import generate_brandproduct_lists
from .tested_brand_product import extract_tested_lists

def extract_metadata(doc_text, job_book_number, hidlevels, brandproduct):
  # Extracts metadata-related information from the text.
  project_name = get_project_name(doc_text)
  nr_tested_media = extract_nr_of_tested_media(doc_text)
  cells_output = generate_cells_output(nr_tested_media)
  category_settings = get_language_sections(doc_text)
  media_info = get_media_info(doc_text)
  filler_info, filler_brandproduct_list_raw = get_filler_media_info(doc_text)
  tested_brandproduct_list_raw = extract_tested_lists(doc_text)

  metadata_output = (
        f">>> Project Name: {project_name}\n\n"
        f"---------------------\n"
        f"Metadata Information:\n"
        f"---------------------\n\n"
        f"{cells_output}\n\n"
    )

  metadata_output += generate_metadata_language_section(category_settings)

  # TestedAds
  metadata_output += generate_metadata_for_media(media_info, job_book_number)

  # FillersList
  metadata_output += generate_fillerslist(filler_info,job_book_number, nr_tested_media)

  # Filler brandproduct lists
  #TBD

  # Tested brandproduct lists
  #TBD

  return metadata_output