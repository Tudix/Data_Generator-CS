from docx import Document
import re
import os

def read_word_document(file_path):
  doc = Document(file_path)
  text = []
  for paragraph in doc.paragraphs:
    text.append(paragraph.text)
  return "\n".join(text)


def save_output(output, output_path):
  with open(output_path, 'w') as f:
    f.write(output)

def create_folder(folder_name):
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder created: {folder_name}")
  else:
    print(f"Folder already exists: {folder_name}")


if __name__ == "__main__":

  input_file = "input/10981_project_information.docx"
  output_folder = 'output'
  metadata_file = os.path.join(output_folder,'Metadata.txt')
  routing_file = os.path.join(output_folder,'Routing.txt')

  create_folder(output_folder)

  text = read_word_document(input_file)
  save_output(text,metadata_file)
  #save_output(text,routing_file)  #Create Routing.txt

  print("Output saved!")