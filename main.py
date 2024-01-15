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


def choose_pokemon(deck):
    print("Choose your Pokemon:")
    for idx, pokemon in enumerate(deck, start=1):
        print(f"{idx}. {pokemon['name']} (ID: {pokemon['id']}, Height: {pokemon['height']}, Weight: {pokemon['weight']})")

    choice = int(input("Enter the number of the Pokemon you want to choose: "))
    return deck.pop(choice - 1)

player_name = input("Please, enter yor name\n")
game_score = 0

# Initialize new_score outside the if block
new_score = ""

#main cycle
while (input("Press ENTER to start a new game\n") != '\n'):
    deck = list(range(1, 151))
    player_deck = [get_pokemon(random.choice(deck)) for _ in range(5)]
    comp_deck = [get_pokemon(random.choice(deck)) for _ in range(5)]

    # Game cycle goes until one of the decks (player or computer) is not empty
    while len(comp_deck) > 0 and len(player_deck) > 0:
        print("Computer deck:\n", [pokemon['name'] for pokemon in comp_deck])
        print("\nPlayer deck:\n", [pokemon['name'] for pokemon in player_deck], "\n")

        # Get the player's chosen Pokemon
        player_pokemon = choose_pokemon(player_deck)

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
