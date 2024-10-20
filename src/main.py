import os
from utils import read_word_document, create_folder
from generate_output import generate_all_outputs

if __name__ == "__main__":

  input_file = "input/86044_project_information.docx"
  output_folder = 'output'                                          # Container folder
  metadata_file = os.path.join(output_folder,'Metadata.txt')
  routing_file = os.path.join(output_folder,'Routing.txt')
  job_book_number = "10-123456-20"

  # Create container folder
  create_folder(output_folder)


  # Read word document
  doc_text = read_word_document(input_file)

  # Generate Metadata & Routing
  outputs = generate_all_outputs(doc_text, job_book_number)

  # Save to respective files
  with open(metadata_file, 'w') as f:
    f.write(outputs['metadata'])

  with open(routing_file, 'w') as f:
    f.write(outputs['routing'])

  print("Metadata.txt and routing.txt generated!")