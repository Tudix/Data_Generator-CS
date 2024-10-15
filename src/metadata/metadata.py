from .cell import get_cell
from project_name import get_project_name

def extract_metadata(doc_text):
  # Extracts metadata-related information from the text.
  project_name = get_project_name(doc_text)
  cell_output = get_cell(doc_text)

  metadata_output = (
        f">>> Project Name: {project_name}\n\n"
        f"---------------------\n"
        f"Metadata Information:\n"
        f"---------------------\n\n"
        f"{cell_output}\n\n"
    )

  return metadata_output