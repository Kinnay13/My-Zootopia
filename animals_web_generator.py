import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ""

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    first_location = locations[0] if locations else None
    animal_type = animal.get("characteristics", {}).get("type")

    if name:
        output += f"Name: {name}\n"
    if diet:
        output += f"Diet: {diet}\n"
    if first_location:
        output += f"Location: {first_location}\n"
    if animal_type:
        output += f"Type: {animal_type}\n"

    output += "\n"

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(new_html)