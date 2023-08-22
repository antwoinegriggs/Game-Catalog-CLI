import sys

def render_main_menu():
    print("Welcome to Game Catalog")
    # print("Please selct one of the following options")
    print("1. My Games")
    print("2. Edit Games")
    print("3. Exit")
    

def render_my_games():
    print("\nMy Games:")
    print("1. View All Games")
    print("2. Search Game By Title")
    print("3. Search Game By Genre")
    print("4. Main Menu")
    print("5. Exit")
    option = input("Please selct one of the following options: ")
    

def edit_games():
    print("\nEdit Games")
    print("1. Add A Game")
    print("2. Edit A Game")
    print("3. Delete A Game")
    print("4. Main Menu")
    print("5. Exit")
    
    option = input("Please selct one of the following options: ")

def main_menu():
    while True:
        render_main_menu()
        option = input("Please selct one of the following options: ")

        if not option.isdigit():
            print("Invalid Input. Please enter a valid input.")
            continue
    
        option = int(option)

        if option == 1:
            render_my_games()
        elif option == 2:
            print("Search By Game")
        elif option == 3:
            print("Search By Genre")
        elif option == 4:
            render_main_menu()
        elif option == 5:
            print("Goodbye...")
            sys.exit()
        else:
            print("Invalid Input. Please enter a valid input.")
            render_main_menu()

def my_games():
    while True:
        render_my_games()
        option = input("Please selct one of the following options: ")

        if not option.isdigit():
            print("Invalid Input. Please enter a valid input.")
            continue
    
            option = int(option)

        if option == 1:
            render_my_games()
        elif option == 2:
            edit_games()
        elif option == 3:
            print("Goodbye...")
            sys.exit()
        else:
            print("Invalid Input. Please enter a valid input.")
            render_main_menu()

if __name__ == "__main__":
    main_menu()