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