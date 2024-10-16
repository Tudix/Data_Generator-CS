import re

# Predefined list of verbs with their corresponding precode
VERB_LIST = {
    "choose": 1,
    "use": 2,
    "visit ": 3,
    "visit": 4,
    "try": 5,
    "contact": 6,
    "seek research on": 7,
    "recommend": 8,
    "get a quote for": 9,
    "download": 10,
    "ask a doctor about": 11,
    "visit a website on": 12,
    "watch": 13,
    "buy": 14,
    "consider": 15,
    "play with": 16,
    "ask for": 17
}

def get_verb_used(doc_text):
  # Regular expression to find "Verb used tested ad:" line and extract the verb
  verb_match = re.search(r'Verb\s*used\s*tested\s*ad:\s*(.+)', doc_text , re.IGNORECASE)
  if verb_match:
    verb = verb_match.group(1).strip().lower()
    precode = VERB_LIST.get(verb)

    if precode:
        return f"QVerb1.Response = {{_{precode}}}\n\n"
    else:
      return f"Verb '{verb}' not found in the predifined list.\n\n"
  else:
    raise ValueError("'Verb used tested ad' not found in the document.")