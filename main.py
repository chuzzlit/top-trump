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

def output_pokemon_info(pokemon):
    print(" {}\n ID: {} \n Height: {} \n Weight: {} \n".format(pokemon['name'].upper(),
                                                                                  pokemon['id'],
                                                                                  pokemon['height'],
                                                                                  pokemon['weight']))



DECK_SIZE = 5
stats = ["id", "height", "weight"]
player_name = input("Please, enter yor name\n")
# main cycle
while input('Press ENTER to start a new game\n') != '\n':
    player_move = True
    game_score = 0
    deck = list(range(1, 151))

    player_deck = list()
    while len(player_deck) < DECK_SIZE:
        num = random.choice(deck)
        player_deck.append(get_pokemon(num))
        deck.remove(num)

    comp_deck = list()
    while len(comp_deck) < DECK_SIZE:
        num = random.choice(deck)
        comp_deck.append(get_pokemon(num))
        deck.remove(num)

    # game cycle goes until one of the decks (player or computer) will not be empty
    while len(comp_deck) > 0 and len(player_deck) > 0:
        # get first pokemon from the players deck and print info about it
        player_pokemon = player_deck.pop(0)
        comp_pokemon = comp_deck.pop(0)
        if player_move:
            print("Your Pokemon is")
            output_pokemon_info(player_pokemon)
          # choosing of the statement
            choose = input("Choose the stat: h for height, w for weight, everything else for id.\n")
            if choose == 'h':
                stat = "height"
            elif choose == 'w':
                stat = "weight"
            else:
                stat = 'id'

            print("Computer Pokemon is")
            output_pokemon_info(comp_pokemon)

        else:
            stat = random.choice(stats)
            print("Computer Pokemon is")
            output_pokemon_info(comp_pokemon)
            print("Computer choice is {}.\n".format(stat))

        if player_pokemon[stat] > comp_pokemon[stat]:
            # player wins, adding his pokemon and then computer pokemon to the end of the players deck
            print("YOUR POKEMON WINs!!! \n")
            player_move = True
            game_score += (player_pokemon[stat] - comp_pokemon[stat])
            player_deck.append(player_pokemon)
            player_deck.append(comp_pokemon)
        elif player_pokemon[stat] < comp_pokemon[stat]:
            print("Computer wins! \n")
            player_move = False
            game_score += (comp_pokemon[stat] - player_pokemon[stat])
            comp_deck.append(comp_pokemon)
            comp_deck.append(player_pokemon)
        else:
            # draw, add pokemons to the end of its draws
            print("It's a draw! Next round\n")
            player_move = not player_move
            comp_deck.append(comp_pokemon)
            player_deck.append(player_pokemon)

    # if player draw contents all the pokemons (10 elements) he wins
    if len(player_deck) > 1:
        print("YOU WIN!!! Your score is " + str(game_score))
        with open('game_score.txt', 'r') as score_file:
            contents = ""
            score_written = True
            for line in score_file:
                new_name = line.split(' ')
                if game_score > int(new_name[1]) and score_written:
                    contents = contents + player_name + " " + str(game_score) + "\n"
                    score_written = not score_written
                contents = contents + line

        with open('game_score.txt', 'w+') as score_file:
            score_file.write(contents)
    else:
        print("Computer wins!")

    print(contents)
