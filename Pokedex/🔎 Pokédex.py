class Pokedex:

    def __init__(self):
        self.pokemons = {}

    def add_pokemon(self, pokemon):
        self.pokemons[pokemon.name] = pokemon

    def display_pokemon(self):
        for pokemon in self.pokemons.values():
            print(pokemon.get_pokemon_info())
