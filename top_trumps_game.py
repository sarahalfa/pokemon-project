import random

print(" ------------------------------------ ")
print("|                                    |")
print("|         Pokemon Top Trumps         |")
print("|                                    |")
print(" ------------------------------------ ")
print("")

import requests

def random_pokemon():
    random_pokemon = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_pokemon)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'number': pokemon['number'],
        'ability': pokemon['ability'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'forms': pokemon['forms'],
        'moves': pokemon['moves'],

    }

def computer_pokemon():
    computer_pokemon = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(computer_pokemon)
    response = requests.get(url)
    pokemon = response.json()

    return {
            'name': pokemon['name'],
            'number': pokemon['number'],
            'ability': pokemon['ability'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'forms': pokemon['forms'],
            'moves': pokemon['moves'],

        }

def play():

    computer_pokemon = random_pokemon

    print('You have been given the following pokemon card'.format ['random_pokemon'])
    print('Which stat would you like to use? (number, ability, height, weight, forms, moves)')
    
    computer_stat: ['object']
    random_pokemon_stat = [random_pokemon['stat_choice'],
    computer_stat [object] = [computer_pokemon['stat_choice'],
    print('Your opponent has chosen {}'.format(computer_pokemon['name']))

    if computer_stat > random_pokemon_stat:
        print('You Lose!')
    if computer_stat < random_pokemon_stat:
        print('You Win!')
    elif computer_stat == random_pokemon_stat:
        print('You both win! Its a draw!'),


play()
