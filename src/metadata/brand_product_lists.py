import re

def generate_brandproduct_lists(languages, brandproduct_list_raw, hidlevels, brandproduct, optional_param=None):
  """
    Generate brand or filler outputs based on the parameters provided.
    
    :param languages: Dictionary of language keys for each language's output.
    :param brandproduct_list: List containing brand and product details for each language.
    :param hidlevels: Integer controlling hid level.
    :param brandproduct: Integer controlling brand/product output type.
    :param optional_param: Optional string ('Filler') to differentiate between tested and filler outputs.
    :return: Dictionary with outputs per language.
    """

  output = {}
  prefix = f'{optional_param}' if optional_param else ""

  for language_data in brandproduct_list_raw:
    lang_label = f"Language{language_data['language_label']} - {language_data['language_name']}"

    brands = []
    brand_logos = []
    brand_logo_names = []
    brand_counter = 0

    for line in language_data['brandproduct'].splitlines():
      if ("Brand:" or "Brand name:") in line:
        brand_counter += 1
        brand_name = line.split(":")[1].strip()
        brands.append(f'_{brand_counter} "{brand_name}"')
      if optional_param:
        logo_file = re.search(r'\s*FillerBrandLogo\d+\.jpg\s*', line)
      else:
        logo_file = re.search(r'(.?*)\s*BrandLogo\d+\.jpg\s*', line)

      if logo_file:
        logo_path = f"<img src='{{#mediaPath}}{{#subFolder1}}/{{#CultureInfo_media}}/{logo_file.group().strip()}' />"
        brand_logos.append(f'_{brand_counter} "{logo_path}"')
        brand_logo_names.append(f'_{brand_counter} "{logo_path}<br\\>{brand_name}"')

    # Generate tested or filler lists
    output[lang_label] = f"{prefix}BrandList \"\" define {{\n    {',\n    '.join(brands)}\n}};\n"
    output[lang_label] += f"{prefix}BrandListLogo \"\" define {{\n    {',\n    '.join(brand_logos)}\n}};\n"
    output[lang_label] += f"{prefix}BrandListLogoName \"\" define {{\n    {',\n    '.join(brand_logo_names)}\n}};\n"

  return output