import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, game_platform_join, Game, Platform, Genre


engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine)
session = Session()

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
    print("3. Search Game By Platform")
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
            games = session.query(Game).all()
            for game in games:
                print()
                print(f"Title: {game.title}")
                print(f"Genre: {game.type_genre}")
                print(f"Platform: {game.name_platform}")
                print()  
            print("complete")   
        elif option == 2:
            search_title = input("Enter the game title: ")
            match_games = session.query(Game).filter(Game.title.startswith(search_title)).all()
    
            if match_games:
                for game in match_games:
                    print()
                    print(f"Title: {game.title}")
                    print(f"Genre: {game.type_genre}")  
                    print(f"Platform: {game.name_platform}")  
                    print() 
            else:
                print("No games match the search criteria.")

        elif option == 3:
            platform_search()
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

# Platfrom Search
def render_platform_search():
    print("Select a platform option:")
    print("1. PC (Windows)")
    print("2. Web Browser")
    print("3. PC (Windows), Web Browser")
    print("4. Main Menu")
    print("5. Exit")

def platform_search():

    platform_mapping = {
        "1": ["PC (Windows)"],
        "2": ["Web Browser"],
        "3": ["PC (Windows)", "Web Browser"]
    }

    while True:
        render_platform_search()
        option = input("Choose a Platform: ")

        if option == "4":
            main_menu()
            break
        elif option == "5":
            print("Goodbye...")
            sys.exit()



        platform_name = platform_mapping.get(option)
        if platform_name is not None:
            platforms = [platform_name] if isinstance(platform_name, str) else platform_name

            matching_games = (
                session.query(Game)
                .join(game_platform_join)
                .join(Platform)
                .filter(Platform.name.in_(platforms))
                .all()
            )

            if matching_games:
                for game in matching_games:
                    print()
                    print(f"Title: {game.title}")
                    print(f"Genre: {game.type_genre}")
                    print(f"Platform(s): {game.name_platform}")
                    print() 
            
        else:
            print("Invalid Input. Please enter a valid input.")








if __name__ == "__main__":
    main_menu()