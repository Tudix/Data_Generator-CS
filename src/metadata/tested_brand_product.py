import re

def extract_tested_lists(doc_text):

  output = []

  # Regular expression to find the "Tested brand/Product lists:" and extract the lists
  lists_match = re.search(r'\s*Tested\s*brand/Product\s*lists:\s*\n+(.*?)\n+\s*Open\s*ended\s*question:\s*', doc_text, re.DOTALL)

  language_regex = re.compile(
    r'\s*Language(\d+):\s*(\w+)\s*\n'
    r'((?:(?:\t.*\n?)+)+)',
    re.DOTALL
  )

  for match in language_regex.finditer(lists_match.group(1).strip()):
    match_list = {
      "language_label": match.group(1),
      "language_name": match.group(2),
      "brandproduct": match.group(3).strip()
    }

    output.append(match_list)

  return output
