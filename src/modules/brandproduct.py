import re

def extract_project_type(doc_text):
  """
  Extracts the project type from the provided document text.

  Parameters:
  - doc_text (str): The document text to search for project type.

  Returns:
  - str: The extracted project type.

  Raises:
  - ValueError: If the project type is not found in the document.
  """
  # Regular expression to find the "Project type" and extract the value
  project_type_match = re.search(r'Project\s*type:\s*(.+)', doc_text, re.IGNORECASE)

  if project_type_match:
    project_type = project_type_match.group(1).strip()
    return project_type
  else:
    raise ValueError("Project type not found in the document")

def extract_hidlevels(project_type):
  """
  Determines the HidLevels response code based on the project type.

  Parameters:
  - project_type (str): The project type extracted from the document.

  Returns:
  - int: 1 if the project type is "Brand" or "Product",
         2 if the project type is "Brand and Product".

  Raises:
  - ValueError: If the project type is unrecognized.
  """
  if project_type in ["Brand","Product"]:
    return 1      # HidLevels.Repsonse = {_1}
  elif project_type == "Brand and Product":
    return 2      # HidLevels.Response = {_2}
  else:
    raise ValueError(f"Unknown Project type: {project_type}")

def extract_brandproduct(project_type):
  """
  Determines the BrandProduct response code based on the project type.

  Parameters:
  - project_type (str): The project type extracted from the document.

  Returns:
  - int: 1 for "Brand", 2 for "Product" or "Brand and Product".

  Raises:
  - ValueError: If the project type is invalid for BrandProduct.
  """
  # Generate the BrandProduct.Response based on the hidlevel
  if project_type == "Brand":
    return 1      # BrandProduct.response = {_1} if Brand
  elif project_type in ["Product", "Brand and Product"]:
    return 2      # BrandProduct.response = {_2} if Product
  else:
    raise ValueError(f"Invalid project type for BrandProduct: {project_type}")