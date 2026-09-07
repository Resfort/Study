import requests

# Отправляем запрос к PokeAPI
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# Печатаем статус-код ответа (200 значит, что всё прошло успешно!)
print("Статус ответа:", response.status_code)

data = response.json()

# Мы можем обращаться к ключам как в обычном словаре:
print("Имя:", data["name"])
print("Рост:", data["height"])
print("Вес:", data["weight"])

class Pokemon:
    def __init__(self, name, poke_type, attack, base_exp):
        self.name = name
        self.poke_type = poke_type
        self.attack = attack
        self.base_exp = base_exp
    def get_pokemon_info(self):
        return f"{self.name} is a {self.poke_type}-type Pokémon with an attack stat of {self.attack} and base experience of {self.base_exp}."
pikachu = Pokemon(
    data["name"],
    data["types"][0]["type"]["name"],
    data["stats"][1]["base_stat"],
    data["base_experience"]
)