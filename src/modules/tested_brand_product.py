import re

def extract_tested_lists(doc_text):
  """
	Extracts brand/product lists for each language from the document text.

	Args:
		doc_text (str): Full text from the document.

	Returns:
		tested_brandproduct_list_raw (dict): Contains unformatted brand/product data per language.
	"""

  tested_brandproduct_list_raw = {}

  # Regular expression to find the "Tested brand/Product lists:" and extract the lists
  lists_match = re.search(r'\s*Tested\s*brand/Product\s*lists:\s*\n+(.*?)\n+\s*Open\s*ended\s*question:\s*', doc_text, re.DOTALL)

  language_regex = re.compile(
    r'\s*Language(\d+):\s*(\w+)\s*\n'
		r'(.*?)(?=Language\d+:|$)',
    re.DOTALL
  )

  for match in language_regex.finditer(lists_match.group(1).strip()):
    language = match.group(2)
    language_label = match.group(1)
    brand_product = match.group(3).strip()

    tested_brandproduct_list_raw[language] = {
      "language_label": language_label,
      "brandproduct": brand_product
    }

  return tested_brandproduct_list_raw