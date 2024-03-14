import requests


def get_pokemon_moves(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    data = response.json()
    pokemon_moves = []
    for move in data['moves']:
        pokemon_moves.append(move['move']['name'])
    return pokemon_moves


def pokemon_weaknesses(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    data = response.json()
    weaknesses = []
    for type_slot in data['types']:
        type_url = type_slot['type']['url']
        type_response = requests.get(type_url)
        type_data = type_response.json()
        for weakness in type_data['damage_relations']['double_damage_from']:
            weaknesses.append(weakness['name'])
    return list(set(weaknesses))


def is_move_strong(pokemon_move, weakness_list):
    response = requests.get(f"https://pokeapi.co/api/v2/move/{pokemon_move.lower()}")
    data = response.json()
    move_type = data['type']['name']
    return move_type in weakness_list


def format_move_list(move_list):
    capitalized_words = []
    for i in range(len(move_list)):
        move = move_list[i].split('-')
        for word in move:
            capitalized_words.append(word.capitalize())
        formatted_move = ' '.join(capitalized_words)
        capitalized_words = []
        move_list[i] = formatted_move
    return move_list

def main():
    strong_moves = []
    move_list = get_pokemon_moves('charmander')
    weakness_list = pokemon_weaknesses('bulbasaur')

    for move in move_list:
        if is_move_strong(move, weakness_list) is True:
            strong_moves.append(move)

    print(format_move_list(strong_moves))


if __name__ == '__main__':
    main()
