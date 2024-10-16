import re

def get_project_type(doc_text):
  # Regular expression to find the "Project type" and extract the value
  project_type_match = re.search(r'Project\s*type:\s*(.+)', doc_text, re.IGNORECASE)

  if project_type_match:
    project_type = project_type_match.group(1).strip()
    return project_type
  else:
    raise ValueError("Project type not found in the document")

def get_hidlevels(project_type):
  if project_type in ["Brand","Product"]:
    return 1      # HidLevels.Repsonse = {_1}
  elif project_type == "Brand and Product":
    return 2      # HidLevels.Response = {_2}
  else:
    raise ValueError(f"Unknown Project type: {project_type}")


def get_brandproduct(project_type):
  # Generate the BrandProduct.Response based on the hidlevel
  if project_type == "Brand":
    return 1      # BrandProduct.response = {_1} if Brand
  elif project_type == "Product":
    return 2      # BrandProduct.response = {_2} if Product
  else:
    raise ValueError("Invalid project type for BrandProduct")