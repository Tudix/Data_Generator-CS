import re

def extract_routing(text):
  # Extracts routing-related information from the text.
  routing_number = re.search(r"Routing Number:\s*(\d+)", text)

  if routing_number:
    return f"Routing Number: {routing_number.group(1)}"
  return "No routing information found."
