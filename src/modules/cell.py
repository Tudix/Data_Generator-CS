import re

def extract_nr_of_tested_media(doc_text):
  """
  Extracts the number of tested media from the document text.

  Args:
    doc_text (str): Full text from the document.

  Returns:
    int: The number of tested media found in the document.

  Raises:
    ValueError: If the "Nr of tested media" is not found in the document.
  """

  # Regular expression to find "Nr of tested media" and extract the integer value
  nr_tested_media_match = re.search(r'Nr\s*of\s*tested\s*media:\s*(\d+)', doc_text, re.IGNORECASE)
  if nr_tested_media_match:
    nr_tested_media = int(nr_tested_media_match.group(1))
    return nr_tested_media
  else:
    raise ValueError("Number of tested media not found in the document.")

def generate_cells_output(nr_tested_media):
  """
  Generates the cells output string based on the number of tested media.

  Args:
    nr_tested_media (int): The number of tested media.

  Returns:
    str: Formatted output string for cell definitions.
  """
  cells_output = 'Cell "cell - hidden"\ncategorical [0..]\n{\n'
  cell_entries = [f'    _{i} "Cell {i}"' for i in range(1, nr_tested_media + 1)]
  cells_output += ',\n'.join(cell_entries) + '\n};\n\n'

  return cells_output