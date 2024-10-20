import re
from project_name import get_project_name
from .exposure_type import get_exposure_type
from .brand_product import get_project_type, get_hidlevels, get_brandproduct
from .verb_used import get_verb_used
from .language_info_routing import generate_routing_language_section
from metadata.language_info_metadata import get_language_sections
from .media_info_routing import get_media_info, generate_routing_for_media


def extract_routing(doc_text):
  # Extracts routing-related information from the doc_text.

  project_name = get_project_name(doc_text)
  exposure_type = get_exposure_type(doc_text)
  project_type = get_project_type(doc_text)
  hidlevels = get_hidlevels(project_type)
  brandproduct = get_brandproduct(project_type)
  verb_used = get_verb_used(doc_text)
  languages = get_language_sections(doc_text)
  media_info = get_media_info(doc_text)


  routing_output = (
        f">>> Project Name: {project_name}\n\n"
        f"---------------------\n"
        f"Routing Information:\n"
        f"---------------------\n\n"
    )

  # Exposure_Type
  if exposure_type:
    routing_output += f"exposure_type = {{{exposure_type}}}\n\n"

  # HidLevels
  routing_output += f"HidLevels.Response = {{_{hidlevels}}}\n\n"

  # BrandProduct
  if hidlevels == 1:
    brandproduct = get_brandproduct(project_type)
    routing_output += f"BrandProduct.Response = {{_{brandproduct}}}\n\n"

  # QVerb
  routing_output += verb_used

  # isEntertainment | TobAlcoBevCateg
  routing_output +=  generate_routing_language_section(languages)

  routing_output += generate_routing_for_media(media_info)



  return routing_output