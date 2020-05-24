import random

import data


def print_grid(array):
    """ Print the current game grid
    Ex :
        a   b   c
      + - + - + - +
    1 | X | O | - |
      + - + - + - +
    2 | - | X | - |
      + - + - + - +
    3 | - | O | - |
      + - + - + - +
"""

    print("    a   b   c  ")
    print("  + - + - + - +")
    for i, ligne in enumerate(array):
        print(i + 1, "", end='')
        for j, case in enumerate(ligne):
            if case == 0:
                print("|", "- ", end='')
            elif case == 1:
                print("| X ", end='')
            else:
                print("| O ", end='')
        print("| \n"
              "  + - + - + - +")


def print_banner():
    print("")


def is_remaining_case():
    """ Return True if the file contains empty box"""
    if any(0 in x for x in data.grid):
        return True
    return False


def check_win(value_to_verify):
    """Return true if there's a winner """
    # Diagonal check
    if (data.grid[2][0] == value_to_verify and data.grid[2][0] == data.grid[1][1] and data.grid[0][2] ==
        data.grid[1][1]) or (
            data.grid[0][0] == value_to_verify and data.grid[0][0] == data.grid[1][1] and data.grid[2][2] ==
            data.grid[1][1]):
        return True

    # Lines check
    for i in range(3):
        if (data.grid[i][0] == value_to_verify and data.grid[i][0] == data.grid[i][1] and data.grid[i][2] ==
            data.grid[i][1]) or (
                data.grid[0][i] == value_to_verify and data.grid[0][i] == data.grid[1][i] and data.grid[2][i] ==
                data.grid[1][i]):
            return True
    return False


def ask_value():
    """Ask the player to enter the coordinates of the chosen box"""
    print("Entrez les coordonnées de la case choisie :")
    try:
        letter_inserted = str(input("Entrez la lettre => "))
        number_inserted = int(input("Entrez le chiffre => "))
    except ValueError:
        return [-1]

    # Check if the value is correct
    if ['a', 'b', 'c'].count(letter_inserted) == 1 and range(1, 4).count(number_inserted) == 1:
        # Parse coordinate to index of the grid
        return [number_inserted - 1, ord(letter_inserted) - 97]
    else:
        return [-1]


def place_value(array_coord_tab, user_digit, silent_mode=False):
    if data.grid[array_coord_tab[0]][array_coord_tab[1]] == 0:
        data.grid[array_coord_tab[0]][array_coord_tab[1]] = user_digit
        return True
    else:
        if not silent_mode:
            print("Erreur valeur déjà prise")
        return False


def get_random_value():
    """Return an array of two randow value between 0 and 2"""
    return [random.randint(0, 2), random.randint(0, 2)]


def ask_player_name():
    """Ask and define the username of the current player"""
    username = ''
    while username.strip() == '':
        print("Entrez votre pseudo")
        username = str(input("====> "))

    data.current_username = username
