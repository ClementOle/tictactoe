import data
import files_functions
import functions
import score_functions

# Init the saved data
files_functions.init_wall_of_fame()

while True:

    # Init an empty grid
    data.grid = [[0 for x in range(3)] for y in range(3)]

    nb_game_turn = 0

    # Ask the player name and save it
    functions.ask_player_name()

    while True:
        nb_game_turn += 1
        functions.print_grid(data.grid)
        is_value_ok = False

        # Player turns
        while not is_value_ok:
            array_of_value = functions.ask_value()
            if array_of_value[0] == -1:
                print("Valeur incorrect recommencez !")
                continue
            # Placing the value on the grid
            is_value_ok = functions.place_value(array_of_value, 1, False)

        if functions.check_win(1):
            print("Vous avez gagné en {0} tours !".format(nb_game_turn))

            # If the player win we update his best score in the dictionary
            if data.current_username in data.wall_of_fame:
                if data.wall_of_fame[data.current_username] < nb_game_turn:
                    data.wall_of_fame[data.current_username] = nb_game_turn
            else:
                data.wall_of_fame.update({data.current_username: nb_game_turn})
            break
        if not functions.is_remaining_case():
            print("Match nul !")
            break

        # Computer turns
        is_value_ok = False
        while not is_value_ok:
            array_of_value = functions.get_random_value()
            is_value_ok = functions.place_value(array_of_value, 2, True)

        if functions.check_win(2):
            print("La machine a gagné !")
            break
        if not functions.is_remaining_case():
            print("Match nul ! ")
            break
    # Ask if we show the wall of fame
    choice = ''
    while choice != 'Y' and choice != 'N':
        print("Voulez-vous afficher le tableau des scores Y/N?")
        choice = str(input("=====> "))
        choice = choice.capitalize()
    if choice == "Y":
        score_functions.print_wall_of_fame()


    # Ask if we replay
    choice = ''
    while choice != 'Y' and choice != 'N':
        print("Voulez-vous refaire une partie ?")
        print("Y: Oui, N: Non")
        choice = str(input("====> "))
        choice = choice.capitalize()
    if choice == 'N':
        break

# Save the scores to file
files_functions.write_dict_in_file(data.wall_of_fame)
