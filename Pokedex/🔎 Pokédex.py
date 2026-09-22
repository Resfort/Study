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

class Pokedex:
    def __init__(self):
        self.pokemons = {}

    def add_pokemon(self, pokemon):
        self.pokemons[pokemon.name] = pokemon

    def display_all(self):
        for pokemon in self.pokemons.values():
            print(pokemon.get_pokemon_info())

# Проверка работы:
my_pokedex = Pokedex()
pikachu = get_pokemon("pikachu")
my_pokedex.add_pokemon(pikachu)

my_pokedex.display_all()