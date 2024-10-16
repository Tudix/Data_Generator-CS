def generate_routing_language_section(languages):
  routing_output = ""

  for language in languages:
    is_entertainment_value = "_1" if language["is_entertainment"] == "yes" else "_2"
    tob_alco_value = "_1" if language["is_tobacco_or_alcohol"] == "yes" else "_2"

    if len(languages) > 1:
      routing_output += f'--- {language["language_label"]} - {language["language_name"]} ---\n\n'

    routing_output += (
      f'isEntertainment.Response = {{{is_entertainment_value}}}\n\n'
      f'TobAlcoBevCateg.Response = {{{tob_alco_value}}}\n\n'
    )

    if len(languages) > 1:
      routing_output += f'--- {language["language_label"]} - {language["language_name"]} --- END\n\n' 

  return routing_output