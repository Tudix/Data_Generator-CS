import re
from project_name import get_project_name
from .exposure_type import get_exposure_type

def extract_routing(doc_text):
  # Extracts routing-related information from the doc_text.

  project_name = get_project_name(doc_text)
  exposure_type = get_exposure_type(doc_text)

  routing_output = (
        f">>> Project Name: {project_name}\n\n"
        f"---------------------\n"
        f"Routing Information:\n"
        f"---------------------\n\n"
    )

  if exposure_type:
    routing_output += f"exposure_type = {{{exposure_type}}}\n\n"

  return routing_output