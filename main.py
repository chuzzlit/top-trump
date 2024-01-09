import requests
import random
from pprint import pprint


def get_pokemon(pokemon_number):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    new_pokemon = {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }
    return new_pokemon

player_name = input("Please, enter yor name\n")
game_score = 0
#main cycle
while (input("Press ENTER to start a new game\n") != '\n'):
    deck = list(range(1, 151))
    player_deck = list()
    while len(player_deck) < 5:
        num = random.choice(deck)
        player_deck.append(get_pokemon(num))
        deck.remove(num)

    comp_deck = list()
    while len(comp_deck) < 5:
        num = random.choice(deck)
        comp_deck.append(get_pokemon(num))
        deck.remove(num)

# game cycle goes until one of the decks (player or computer) will not be empty

    while(len(comp_deck) > 0 and len(player_deck) > 0):
        print("Computer deck: \n")
        for pokemon in comp_deck:
            print(pokemon['name'])
        print("\n Player deck: \n")
        for pokemon in player_deck:
            print(pokemon['name'])
        print("\n")

# get first pokemon from the players deck and print info about it
        player_pokemon = player_deck.pop(0)
        print("Your Pokemon is {}\n ID: {} \n Height: {} \n Weight: {} \n".format(player_pokemon['name'].upper(),
                                                                              player_pokemon['id'],
                                                                              player_pokemon['height'],
                                                                              player_pokemon['weight']))

# choosing of the statement
        choose = input("Choose the stat: h for height, w for weight, everything else for id.\n")
        if choose == 'h':
            stat = "height"
        elif choose == 'w':
            stat = "weight"
        else:
            stat = 'id'

 # get first pokemon from computer deck and print info about it
        comp_pokemon = comp_deck.pop(0)
        print("Computer Pokemon is {}\n ID: {} \n Height: {} \n Weight: {} \n".format(comp_pokemon['name'].upper(),
                                                                                  comp_pokemon['id'],
                                                                                  comp_pokemon['height'],
                                                                                  comp_pokemon['weight']))

        if player_pokemon[stat] > comp_pokemon[stat]:
            print("YOUR POKEMON WINs!!! \n")
            game_score += (player_pokemon[stat] - comp_pokemon[stat])
            player_deck.append(player_pokemon)  #player wins, adding his pokemon and then computer pokemon to the end of the players deck
            player_deck.append(comp_pokemon)
        elif player_pokemon[stat] < comp_pokemon[stat]:
            print("Computer wins! \n")
            game_score += (comp_pokemon[stat] - player_pokemon[stat])
            comp_deck.append(comp_pokemon)
            comp_deck.append(player_pokemon)
        else:
            print("It's a draw! Next round\n")  #draw, add pokemons to the end of its draws
            comp_deck.append(comp_pokemon)
            player_deck.append(player_pokemon)


    if len(player_deck) > 1:    #if player draw contents all the pokemons (10 elements) he wins
        print("YOU WIN!!! Your score is " + str(game_score))
        with open('game_score.txt', 'r') as score_file:
            contents = score_file.read()
        with open('game_score.txt', 'w+') as score_file:
            new_score = contents + player_name + " " + str(game_score) + "\n"
            score_file.write(new_score)
    else:
        print("Computer wins!")

    print(new_score)
