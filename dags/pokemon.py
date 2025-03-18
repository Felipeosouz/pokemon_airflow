import requests
import random

from database import insert_pokemon_data

#id = random.randint(1, 1025)


def pokemon_capture(pokemon_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        
        types = [type_info['type']['name'] for type_info in data['types']]
        
        stats = {
            'hp': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'hp'),
            'attack': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'attack'),
            'defense': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'defense'),
            'speed': next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'speed')
        }
        
        species_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}")
        
        if species_response.status_code == 200:
            species_data = species_response.json()

            gender_rate = species_data['gender_rate']
            if gender_rate == 0:
                gender = "female"
            elif gender_rate == 8:
                gender = "male"
            else:
                genders = ["male", "female"]
                gender = random.sample(genders, 1)[0]
            
            evolution_url = species_data['evolution_chain']['url']
            evolution_response = requests.get(evolution_url)
            if evolution_response.status_code == 200:
                evolution_data = evolution_response.json()
                evolutions = [evolution['species']['name'] for evolution in evolution_data['chain']['evolves_to']]
            else:
                evolutions = []

            habitat = species_data.get('habitat')
            if habitat and 'name' in habitat:
                habitat = habitat['name']
            else:
                habitat = 'Unknown'
        else:
            gender = 'Unknown'
            evolutions = []
            habitat = 'Unknown'

        pokemon_data = {
            'pokemon_name': name,
            'gender': gender,
            'types': types,
            'stats': stats,
            'evolution': evolutions,
            'habitat': habitat
        }
        #insert_pokemon_data(pokemon_data)
        print(f"Pokemon {name} capturado!")
        return pokemon_data
    else:
        return {"error": "Erro ao obter dados do Pokémon"}

#pokemon_capture(id)
