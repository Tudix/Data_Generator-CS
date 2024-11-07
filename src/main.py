import os
from core import *
from modules import *

def run_generator(document_path, job_book_number):

  doc_text = read_document(document_path)
  json_settings = load_settings()

  languages = data = extract_languages(doc_text)
  project_name = extract_project_name(doc_text)
  nr_tested_media = extract_nr_of_tested_media(doc_text)
  cells_output = generate_cells_output(nr_tested_media)
  category_settings = extract_category_settings(doc_text)
  media_info = get_media_info(doc_text)
  filler_media_info, filler_brandproduct_list_raw = get_filler_media_info(doc_text)
  tested_brandproduct_list_raw = extract_tested_lists(doc_text)
  exposure_type = extract_exposure_type(doc_text,json_settings)
  project_type = extract_project_type(doc_text)
  hidlevels = extract_hidlevels(project_type)
  brandproduct = extract_brandproduct(project_type)
  qverb_code = extract_verb_used(doc_text, json_settings)
  qoe_responses = extract_qoe(doc_text, json_settings)

  print(data)

  for lang in languages.keys():
    print(lang)
    # Display language (M+R)
    data[lang]["metadata"] = data[lang]["routing"] = f'---------------------\n>>> {lang}\n---------------------\n'

    # Project Name (M+R)
    data[lang]["metadata"] += f'---------------------\n>>> Project name: {project_name}\n---------------------\n\n'
    data[lang]["routing"] += f'---------------------\n>>> Project name: {project_name}\n---------------------\n\n'

    # Cells (M)
    data[lang]["metadata"] += f'{cells_output}'

    # Category Settings (M+R)
    category_metadata, category_routing = generate_category_outputs(category_settings, lang)
    data[lang]["metadata"] += f'{category_metadata}'
    data[lang]["routing"] += f'{category_routing}'


    # Tested ads (M)
    media_info_m =  generate_metadata_for_media(media_info, lang, job_book_number)
    data[lang]["metadata"] += f'{media_info_m}'

    # Filler ads (M)
    filler_media_info_m =  generate_fillerslist(filler_media_info, lang, job_book_number, nr_tested_media)
    data[lang]["metadata"] += f'{filler_media_info_m}'

    # Tested brand/product lists (M)
    tested_brandproduct_lists = generate_brandproduct_lists(tested_brandproduct_list_raw, lang, 1, 1)
    data[lang]["metadata"] += f'{tested_brandproduct_lists}'


    # Filler brand/product lists (M)
    filler_brandproduct_lists = generate_brandproduct_lists(filler_brandproduct_list_raw, lang, 1, 1, "Filler")
    data[lang]["metadata"] += f'{filler_brandproduct_lists}'

    # Exposure_Type (R)
    data[lang]["routing"] += f'exposure_type = {{{exposure_type}}}\n\n'

    # HidLevels (R)
    data[lang]["routing"] += f"HidLevels.Response = {{_{hidlevels}}}\n\n"

    # BrandProduct (R)
    data[lang]["routing"] += f"BrandProduct.Response = {{_{brandproduct}}}\n\n"

    # QVerb (R)
    data[lang]["routing"] += f"QVerb1.Response = {{_{qverb_code}}}\n\n"

    # QOE (R)
    data[lang]["routing"] += f'QOE.Response = {{{",".join(qoe_responses)}}}\n\n'

    # Tested ads (R)
    media_info_r =  generate_routing_for_media(media_info, lang)
    data[lang]["routing"] += f'{media_info_r}'


    write_language_output(data[lang], lang)

if __name__ == "__main__":

  input_file = "input/86044_project_information.docx"
  job_book_number = "10-123456-20"
  output_folder = 'output'                                          # Container folder
  os.makedirs(output_folder, exist_ok=True)
  # metadata_file = os.path.join(output_folder,'Metadata.txt')
  # routing_file = os.path.join(output_folder,'Routing.txt')


  run_generator(input_file,job_book_number)


  # def create_folder(folder_name):
  #   # Creates the folder if it doesn't exist.
  #   if not os.path.exists(folder_name):
  #     os.makedirs(folder_name)
  #     print(f"Folder created: {folder_name}")
  #   else:
  #     print(f"Folder already exists: {folder_name}")

  # # Create container folder
  # create_folder(output_folder)