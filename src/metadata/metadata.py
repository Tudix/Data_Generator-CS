from .cell import get_cell

def extract_metadata(doc_text):
  # Extracts metadata-related information from the text.
  cell_output = get_cell(doc_text)


  metadata_output = cell_output

  #return "\n".join(output_lines) if output_lines else "No metadata found."
  return metadata_output