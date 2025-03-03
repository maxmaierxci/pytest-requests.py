import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
TRAINER_ID = '23057'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Max'