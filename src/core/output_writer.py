import os

def write_language_output(data, language, output_folder):
  """
  Writes metadata or routing for a specific language.
  
  Args:
      data (dict): Dictionary containing metadata or routing details.
      language (str): Language identifier (e.g., "English").
      output_folder (str): Folder container for output files.
  """

  # filename_m = f"output/metadata_{language}.txt"
  filename_m = os.path.join(output_folder,f"metadata_{language}.txt")
  with open(filename_m, "w") as f_m:
    f_m.write(f"{data["metadata"]}")

  # filename_r = f"output/routing_{language}.txt"
  filename_r = os.path.join(output_folder,f"routing_{language}.txt")
  with open(filename_r, "w") as f_r:
    f_r.write(f"{data["routing"]}")