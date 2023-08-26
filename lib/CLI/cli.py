import sys
from ..db.base import Base
from ..db.game_platform_join import game_platform_join
from ..db.games import Game
from ..db.genres import Genre
from ..db.platforms import Platform


# Main Menu

    # Render
def render_main_menu():
    print("Welcome to Game Catalog")
    print("Please selct one of the following options")
    print("1. My Games")
    print("2. Edit Games")
    print("3. Exit")

    # Init Main_Menu
def main_menu():
    while True:
        render_main_menu()
        option = input("Please selct one of the following options: ")

        if not option.isdigit():
            print("Invalid Input. Please enter a valid input.")
            continue
    
        option = int(option)

        if option == 1:
            my_games()
            break
        elif option == 2:
            edit_games()
            break
        elif option == 3:
            print("Goodbye...")
            sys.exit()

        else:
            print("Invalid Input. Please enter a valid input.")



# My Game

    # Render
def render_my_games():
    print("\nMy Games:")
    print("1. View All Games")
    print("2. Search Game By Title")
    print("3. Search Game By Genre")
    print("4. Main Menu")
    print("5. Exit")

    # Init Game
def my_games():
    while True:
        render_my_games()
        option = input("Please selct one of the following options: ")

        if not option.isdigit():
            print("Invalid Input. Please enter a valid input.")
            continue
    
        option = int(option)

        if option == 1:
             print("All Games")
             break
        elif option == 2:
            print("Search By Game")
            break
        elif option == 3:
            print("Search By Genre")
            break
        elif option == 4:
            return
        elif option == 5:
            print("Goodbye...")
            sys.exit()
        else:
            print("Invalid Input. Please enter a valid input.")


    
# Edit Game

    # Render
def render_edit_games():
    print("\nEdit Games")
    print("1. Add A Game")
    print("2. Edit A Game")
    print("3. Delete A Game")
    print("4. Main Menu")
    print("5. Exit")
    
    # Init Edit   
def edit_games():
    while True:
        render_edit_games()
        option = input("Please selct one of the following options: ")

        if not option.isdigit():
            print("Invalid Input. Please enter a valid input.")
            continue
    
        option = int(option)

        if option == 1:
            print("Add Game Function")
            break
        elif option == 2:
            print("Edit Game Function")
            break
        elif option == 3:
            print("Delete Game Function")
            break
        elif option == 4:
            return
        elif option == 5:
            print("Goodbye...")
            sys.exit()
        else:
            print("Invalid Input. Please enter a valid input.")







if __name__ == "__main__":
    main_menu()