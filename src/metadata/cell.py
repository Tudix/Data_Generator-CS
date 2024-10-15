import re

def extract_nr_of_tested_media(doc_text):
  # Regular expression to find "Nr of tested media" and extract the value
  #nr_tested_media_match = re.search(r'Nr of tested media:\s*(/d+)', doc_text)
  nr_tested_media_match = re.search(r'Nr\s*of\s*tested\s*media:\s*(\d+)', doc_text, re.IGNORECASE)
  if nr_tested_media_match:
    nr_tested_media = int(nr_tested_media_match.group(1))
    return nr_tested_media
  else:
    raise ValueError("Number of tested media not found in the document.")

def generate_cells_output(nr_tested_media):
  cells_output = 'Cell "cell - hidden"\ncategorical [0..]\n{\n'
  for i in range(1, nr_tested_media + 1):
    if i < nr_tested_media:
      cells_output += f'    _{i} "Cell {i}",\n'
    else:
      cells_output += f'    _{i} "Cell {i}"\n'
  cells_output += '};'
  return cells_output

def get_cell(doc_text):
  nr_tested_media = extract_nr_of_tested_media(doc_text)
  cells_output = generate_cells_output(nr_tested_media)
  return cells_output


## Process the document and print the output
#output = get_cell(doc_text)
#print(output)