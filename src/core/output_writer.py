def write_language_output(data, language):
  """
  Writes metadata or routing for a specific language.
  
  Args:
      data (dict): Dictionary containing metadata or routing details.
      language (str): Language identifier (e.g., "English").
  """
  filename_m = f"output/metadata_{language}.txt"
  with open(filename_m, "w") as f_m:
    f_m.write(f"{data["metadata"]}")

  filename_r = f"output/routing_{language}.txt"
  with open(filename_r, "w") as f_r:
    f_r.write(f"{data["routing"]}")