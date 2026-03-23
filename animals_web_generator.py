"""Generate an HTML page from animal JSON data using a template."""

import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Convert a single animal dictionary into an HTML list item."""
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    first_location = locations[0] if locations else None
    animal_type = animal.get("characteristics", {}).get("type")

    output = '<li class="cards__item">\n'

    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    if first_location:
        output += f'      <strong>Location:</strong> {first_location}<br/>\n'
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def main():
    """Generate final HTML page from template and animal data."""
    animals_data = load_data("animals_data.json")

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_template = file.read()

    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(new_html)


if __name__ == "__main__":
    main()
