from metadata import extract_metadata
from routing import extract_routing

def generate_all_outputs(text):
  # Generates all outputs by combining results from metadata.py and routing.py
  outputs = {}
  outputs['metadata'] = extract_metadata(text)
  outputs['routing'] = extract_routing(text)
  return outputs