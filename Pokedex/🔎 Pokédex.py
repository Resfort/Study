import requests

class Pokemon:
    def __init__(self, name, poke_type, attack, base_exp):
        self.name = name
        self.poke_type = poke_type
        self.attack = attack
        self.base_exp = base_exp
    def get_pokemon_info(self):
        return f"{self.name} is a {self.poke_type}-type Pokémon with an attack stat of {self.attack} and base experience of {self.base_exp}."
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    data = response.json()

    pokemon_obj = Pokemon(
        data["name"],
        data["types"][0]["type"]["name"],
        data["stats"][1]["base_stat"],
        data["base_experience"]
    )     
    return pokemon_obj

print(get_pokemon("pikachu").get_pokemon_info())