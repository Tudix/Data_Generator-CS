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

  brand_counter = 0
  brands = []
  brand_logos = []
  brand_logo_names = []

  product_counter = 0
  products = []
  product_logos = []
  product_logo_names = []

  lists_productsbrand = []
  lists_img_productsbrand = []
  lists_img_name_productsbrand = []

  # Regular expression to capture all language-specific tested brand
  tested_brand_product_regex = re.compile(
    r'\s*Brand\s*name\s*:\s*(.*?)\n'
    r'\s*Type:\s*(.*?)\n'
    r'\s*File:\s*(.*?)\n'
    r'\s*Status:\s*(.*?)\n'
    r'\s*Aliases:\s*(.*?)\n'
    r'\s*Auto\s*Coding:\s*(.*?)\n'
    r'\s*Products:\s*\n(.*?)(?=(\s*Competitive\s*Products:\s*|\s*Brand\s*name:\s*))',
    re.DOTALL)

  comp_brand_product_regex = re.compile(
    r'\s*Brand\s*name\s*:\s*(.*?)\n'
    r'\s*Type:\s*(.*?)\n'
    r'\s*File:\s*(.*?)\n'
    r'\s*Status:\s*(.*?)\n'
    r'\s*Products:\s*(.*?)(?=(\n\s*Brand\s*name:\s*|$))',
    re.DOTALL)


  # Regular expression to capture all language-specific tested product
  tested_product_regex = re.compile(
    r'\s*Product\s*name\s*:\s*(.*?)\n'
    r'\s*Type:\s*(.*?)\n'
    r'\s*File:\s*(.*?)\n'
    r'\s*Status:\s*(.*?)\n'
    r'\s*Aliases:\s*(.*?)',
    re.DOTALL)

  # Regular expression to capture all language-specific competitive product
  comp_products_regex = re.compile(
    r'\s*Product\s*name:\s*(.*?)\n'
    r'\s*Type:\s*(.*?)\n'
    r'\s*File:\s*(.*?)\n'
    r'\s*Status:\s*(.*?)\n*',
    re.DOTALL)

  def add_brand_withproducts(match, brand_counter, brands, brand_logos, brand_logo_names, index_products_match):
    brand_counter += 1
    brand_name = match.group(1).strip()
    logo_file = match.group(3).strip()
    logo_path = f"<img src='{{#mediaPath}}{{#subFolder1}}/{{#CultureInfo_media}}/{logo_file}' />"

    brands.append(f'_{brand_counter} "{brand_name}"')
    brand_logos.append(f'_{brand_counter} "{logo_path}"')
    brand_logo_names.append(f'_{brand_counter} "{logo_path}<br\\>{brand_name}"')

    product_list_raw = match.group(index_products_match)

    return brand_counter, brands, brand_logos, brand_logo_names, product_list_raw

  def prep_product_lists(brand_counter, products, product_logos, product_logo_names):
    product_counter = brand_counter*100
    products.clear()
    product_logos.clear()
    product_logo_names.clear()
    return product_counter, products, product_logos, product_logo_names

  def add_product(match_product, product_counter, products, product_logos, product_logo_names):
    product_counter += 1
    product_name = match_product.group(1).strip()
    product_file = match_product.group(3).strip()
    product_path = f"<img src='{{#mediaPath}}{{#subFolder1}}/{{#CultureInfo_media}}/{product_file}' />"

    products.append(f'_{product_counter} \"{product_name}\"')
    product_logos.append(f'_{product_counter} \"{product_path}\"')
    product_logo_names.append(f'_{product_counter} \"{product_path}<br\\>{product_name}\"')

    return product_counter, products, product_logos, product_logo_names

  # Brand
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

  # Product
  if hidlevels == 1 and brandproduct == 2:

    # Process each match found by the regular expression
    for match in tested_brand_product_regex.finditer(brandproduct_list_raw[language]['brandproduct']):
      brand_counter, brands, brand_logos, brand_logo_names, product_list_raw = add_brand_withproducts(match, brand_counter, brands, brand_logos, brand_logo_names, 7)

      product_counter, products, product_logos, product_logo_names = prep_product_lists(brand_counter, products, product_logos, product_logo_names)

      for match_product in tested_product_regex.finditer(product_list_raw):
        product_counter, products, product_logos, product_logo_names = add_product(match_product, product_counter, products, product_logos, product_logo_names)

      lists_productsbrand.append(f'List{prefix}ProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(products)}\n}};\n\n')
      lists_img_productsbrand.append(f'List{prefix}ImgProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(product_logos)}\n}};\n\n')
      lists_img_name_productsbrand.append(f'List{prefix}ImgNameProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(product_logo_names)}\n}};\n\n')

    # Regular expression to capture all language-specific competitive products
    competitive_products =  re.search(
      r'\s*Competitive\s*Products\s*:\s*\n\s*Products:\s*\n(.*?)(?=$)',
      brandproduct_list_raw[language]['brandproduct'],
      re.DOTALL
    ).group(1)
    print("comp:\n",competitive_products)

    brand_counter += 1
    product_counter, products, product_logos, product_logo_names = prep_product_lists(brand_counter, products, product_logos, product_logo_names)

    for comp_match in comp_products_regex.finditer(competitive_products):
      product_counter, products, product_logos, product_logo_names = add_product(comp_match, product_counter, products, product_logos, product_logo_names)

    lists_productsbrand.append(f'List{prefix}ProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(products)}\n}};\n\n')
    lists_img_productsbrand.append(f'List{prefix}ImgProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(product_logos)}\n}};\n\n')
    lists_img_name_productsbrand.append(f'List{prefix}ImgNameProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(product_logo_names)}\n}};\n\n')


  # Brand and Product
  if hidlevels == 2 and brandproduct == 2:

    for match in tested_brand_product_regex.finditer(brandproduct_list_raw[language]['brandproduct']):

      brand_counter, brands, brand_logos, brand_logo_names, product_list_raw = add_brand_withproducts(match, brand_counter, brands, brand_logos, brand_logo_names, 7)

      product_counter, products, product_logos, product_logo_names = prep_product_lists(brand_counter, products, product_logos, product_logo_names)

      for match_product in comp_products_regex.finditer(product_list_raw):
        product_counter, products, product_logos, product_logo_names = add_product(match_product, product_counter, products, product_logos, product_logo_names)

      lists_productsbrand.append(f'List{prefix}ProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(products)}\n}};\n\n')
      lists_img_productsbrand.append(f'List{prefix}ImgProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(product_logos)}\n}};\n\n')
      lists_img_name_productsbrand.append(f'List{prefix}ImgNameProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(product_logo_names)}\n}};\n\n')

    comp_brand_product_find = re.search(
    r'\s*Brand\s*name\s*:\s*(.*?)\n'
    r'\s*Type:\s*(.*?)\n'
    r'\s*File:\s*(.*?)\n'
    r'\s*Status:\s*(.*?)\n'
    r'\s*Aliases:\s*(.*?)\n'
    r'\s*Auto\s*Coding:\s*(.*?)\n'
    r'\s*Products:\s*\n(.*?)\n+'
    r'(\s*Brand\s*name\s*:\s*(.*?))(?=($))',
    brandproduct_list_raw[language]['brandproduct'],
    re.DOTALL).group(8)

    for comp_match in comp_brand_product_regex.finditer(comp_brand_product_find):


      brand_counter, brands, brand_logos, brand_logo_names, product_list_raw = add_brand_withproducts(comp_match, brand_counter, brands, brand_logos, brand_logo_names, 5)
      product_counter, products, product_logos, product_logo_names = prep_product_lists(brand_counter, products, product_logos, product_logo_names)

      for match_product in comp_products_regex.finditer(product_list_raw):
        product_counter, products, product_logos, product_logo_names = add_product(match_product, product_counter, products, product_logos, product_logo_names)

      lists_productsbrand.append(f'List{prefix}ProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(products)}\n}};\n\n')
      lists_img_productsbrand.append(f'List{prefix}ImgProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(product_logos)}\n}};\n\n')
      lists_img_name_productsbrand.append(f'List{prefix}ImgNameProductsBrand{brand_counter} \"\"\ndefine\n{{\n    {',\n    '.join(product_logo_names)}\n}};\n\n')

  # Generate tested or filler lists
  output = f"{prefix}BrandList \"\"\ndefine\n{{\n    {',\n    '.join(brands)}\n}};\n\n"
  output += f"{prefix}BrandListLogo \"\"\ndefine\n{{\n    {',\n    '.join(brand_logos)}\n}};\n\n"
  output += f"{prefix}BrandListLogoName \"\"\ndefine\n{{\n    {',\n    '.join(brand_logo_names)}\n}};\n\n"

  if brandproduct == 2:
    output += f"{''.join(lists_productsbrand)}"
    output += f"{''.join(lists_img_productsbrand)}"
    output += f"{''.join(lists_img_name_productsbrand)}"

  return output

# brandproduct_list_raw = {"English": {'brandproduct': """

# Brand name: PreserVision
# 		Type: tested
# 		File: BrandLogo1.jpg
# 		Status: launched
# 		Aliases: PrsVision, PreserVson, PreVision, preservision, Preser Vision
# Auto Coding: 2 (NO)
# 		Products: 
# 			Product name: PreserVision
# 				Type: tested
# 				File: Packshot101.jpg
# 				Status: launched
# 				Aliases: PrsVision, PreserVson, PreVision, preservision, Preser Vision


# 		Competitive Products: 
# 		Products: 
# 			Product name: Centrum Silver
# 				Type: competitor
# 				File: Packshot201.jpg
# 				Status: launched
# 			Product name: Ocuvite
# 				Type: competitor
# 				File: Packshot202.jpg
# 				Status: launched
# 			Product name: One-a-day
# 				Type: competitor
# 				File: Packshot203.jpg
# 				Status: launched
# 			Product name: Store Brand vitamins
# 				Type: competitor
# 				File: Packshot204.jpg
# 				Status: launched
# 			Product name: Nature Made
# 				Type: competitor
# 				File: Packshot205.jpg
# 				Status: launched
# 			Product name: Macuhealth
# 				Type: competitor
# 				File: Packshot206.jpg
# 				Status: launched


#                                      """}}

# brandproduct_list_raw = {"English": {'brandproduct': """

# 	Brand name: BodyArmor
# 		Type: tested
# 		File: BrandLogo1.jpg
# 		Status: launched
# 		Aliases: BodyArmor, Bodyarmor, Body Armor, body armor, bodyarmor, BODYARMOR
# Auto Coding: 2 (NO)
# 		Products: 
# 			Product name: BodyArmor Flash IV
# 				Type: tested
# 				File: Packshot101.jpg
# 				Status: launched

# 	Brand name: Gatorade
# 		Type: competitor
# 		File: BrandLogo2.jpg
# 		Status: launched
# 		Products: 
# 			Product name: Gatorlyte
# 				Type: competitor
# 				File: Packshot201.jpg
# 				Status: launched
# 			Product name: Gatorlyte Zero
# 				Type: competitor
# 				File: Packshot202.jpg
# 				Status: launched

# 	Brand name: Liquid IV
# 		Type: competitor
# 		File: BrandLogo3.jpg
# 		Status: launched
# 		Products: 
# 			Product name: Multiplicador de hidratación
# 				Type: competitor
# 				File: Packshot301.jpg
# 				Status: launched

# 	Brand name: Pedialyte
# 		Type: competitor
# 		File: BrandLogo4.jpg
# 		Status: launched
# 		Products: 
# 			Product name: Pedialyte Sport Liters
# 				Type: competitor
# 				File: Packshot401.jpg
# 				Status: launched

# 	Brand name: PRIME
# 		Type: competitor
# 		File: BrandLogo5.jpg
# 		Status: launched
# 		Products: 
# 			Product name: PRIME Hydration
# 				Type: competitor
# 				File: Packshot501.jpg
# 				Status: launched

# 	Brand name: Electrolit
# 		Type: competitor
# 		File: BrandLogo6.jpg
# 		Status: launched
# 		Products: 
# 			Product name: Electrolit Instant Hydration
# 				Type: competitor
# 				File: Packshot601.jpg
# 				Status: launched

# 	Brand name: Hydralyte
# 		Type: competitor
# 		File: BrandLogo7.jpg
# 		Status: launched
# 		Products: 
# 			Product name: Rehidratación lista para beberehydration
# 				Type: competitor
# 				File: Packshot701.jpg
# 				Status: launched

# 	Brand name: LMNT
# 		Type: competitor
# 		File: BrandLogo8.jpg
# 		Status: launched
# 		Products: 
# 			Product name: Grapefruit Salt
# 				Type: competitor
# 				File: Packshot801.jpg
# 				Status: launched
# 			Product name: Crudo sin sabor
# 				Type: competitor
# 				File: Packshot802.jpg
# 				Status: launched

# 	Brand name: Nuun
# 		Type: competitor
# 		File: BrandLogo9.jpg
# 		Status: launched
# 		Products: 
# 			Product name: Nuun Sport Powder
# 				Type: competitor
# 				File: Packshot901.jpg
# 				Status: launched
# 			Product name: Nuun Sport Tablets
# 				Type: competitor
# 				File: Packshot902.jpg
# 				Status: launched

# 	Brand name: DripDrop
# 		Type: competitor
# 		File: BrandLogo10.jpg
# 		Status: launched
# 		Products: 
# 			Product name: Lima-limón
# 				Type: competitor
# 				File: Packshot1001.jpg
# 				Status: launched
# 			Product name: Cero azúcar - Sandía
# 				Type: competitor
# 				File: Packshot1002.jpg
# 				Status: launched


# """}}

# output = generate_brandproduct_lists(brandproduct_list_raw, "English", 1, 2)

# print(output)