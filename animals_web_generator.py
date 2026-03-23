import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    name = animal.get("name")

    diet = animal.get("characteristics", {}).get("diet")

    locations = animal.get("locations", [])
    first_location = locations[0] if locations else None

    animal_type = animal.get("characteristics", {}).get("type")

    print("Name:", name)

    if diet:
        print("Diet:", diet)

    if first_location:
        print("First location:", first_location)

    if animal_type:
        print("Type:", animal_type)

    print("-" * 30)