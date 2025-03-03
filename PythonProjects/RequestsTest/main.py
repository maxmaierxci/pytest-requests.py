import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'trainer_token'
}
BODY_post = {
    "name": "generate",
    "photo_id": -1
}
BODY_put = {
    "pokemon_id": "248245",
    "name": "Pikachu",
    "photo_id": 25
}
BODY_post_add = {
    "pokemon_id": "248245"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_post)
print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_put)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_post_add)
print(response.text)