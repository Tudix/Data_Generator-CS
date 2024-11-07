import re

def generate_brandproduct_lists(brandproduct_list_raw, language, hidlevels, brandproduct, optional_param=None):
  """
    Generates formatted brand/product lists for a specific language based on parameters.

    Parameters:
      brandproduct_list_raw (dict): Dictionary containing brand/product list data.
      language (str): Language key to select specific brand data from brandproduct_list_raw.
      hidlevels (int): Determines the hid level, controls output type.
      brandproduct (int): Controls output type, used to select brand or product.
      optional_param (str, optional): Specifies if the format is for filler (e.g., 'Filler').

    Returns:
      output (str): A formatted string containing the brand list, brand logos, and brand logo names.
    """

  output = ""
  prefix = f'{optional_param}' if optional_param else ""

  brands = []
  brand_logos = []
  brand_logo_names = []
  brand_counter = 0

  if hidlevels == 1 and brandproduct == 1:
    for line in brandproduct_list_raw[language]['brandproduct'].splitlines():
      if "Brand:" in line or "Brand name:" in line:
        brand_counter += 1
        brand_name = line.split(":")[1].strip()
        brands.append(f'_{brand_counter} "{brand_name}"')

      logo_file = None
      if optional_param:
        match = re.search(r'\s*FillerBrandLogo\d+\.jpg\s*', line)
        if match:
          logo_file = match.group().strip()
      else:
        match = (re.search(r'(.*?)\s*BrandLogo\d+\.jpg\s*', line))
        if match:
          logo_file = match.group().split(":")[1].strip()

      if logo_file:
        logo_path = f"<img src='{{#mediaPath}}{{#subFolder1}}/{{#CultureInfo_media}}/{logo_file}' />"
        brand_logos.append(f'_{brand_counter} "{logo_path}"')
        if brand_name:
          brand_logo_names.append(f'_{brand_counter} "{logo_path}<br\\>{brand_name}"')

    # Generate tested or filler lists
    output = f"{prefix}BrandList \"\"\ndefine\n{{\n    {',\n    '.join(brands)}\n}};\n\n"
    output += f"{prefix}BrandListLogo \"\"\ndefine\n{{\n    {',\n    '.join(brand_logos)}\n}};\n\n"
    output += f"{prefix}BrandListLogoName \"\"\ndefine\n{{\n    {',\n    '.join(brand_logo_names)}\n}};\n\n"

  return output