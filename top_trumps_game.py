import random
 #import the random module to get a random card

print(" ------------------------------------ ")
print("|                                    |")
print("|         Pokemon Top Trumps         |")
print("|                                    |")
print(" ------------------------------------ ")
print("")

import requests
#define the key variable here, add randint, API, and def of pokemon variable
def random_pokemon():
    random_pokemon = random.randint(1, 151)
    url = 'https://pokeapi.co/'.format(random_pokemon)
    response = requests.get(url)
    pokemon = response.json()

#dictionaries list here
    return {
        'name': pokemon['name'],
        'number': pokemon['number'],
        'ability': pokemon['ability'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'forms': pokemon['forms'],
        'moves': pokemon['moves'],

    }

#def play, w/ if/else/elif statements for the actual game

def play():

    your_pokemon = random_pokemon()

    print('You have been given the following pokemon card'.format ['random_pokemon'])

    computer_stat: ['object']
    random_pokemon_stat = [random_pokemon['stat_choice'],
    computer_stat [object] = [random_pokemon['stat_choice'],
    print('Your opponent has chosen {}'.format(random_pokemon['name']))

    if computer_stat > random_pokemon_stat:
        print('You Lose!')
    elif computer_stat < random_pokemon_stat:
        print('You Win!')
    else:
        print('You both win! Its a draw!'),


play()