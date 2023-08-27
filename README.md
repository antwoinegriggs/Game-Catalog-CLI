# Game Catalog CLI

The Game Catalog CLI is a command-line interface application that allows users to manage and interact with a catalog of video games. Users can view, edit, and search for games based on various criteria such as title, genre, and platform.

The current package requirement:
sqlalchemy = "==1.4.41"
python_version = "3.8"

# Installation

    1. Clone the repository to your local machine.

    2. Install the required dependencies
        pipenv install

    3. Open virtual environment
        pipenv shell

    4. Navigate to database directory
        cd lib/db/

    5. Create the database and seed it with sample data:
        python seed.py
            or
        python3 seed.py

    6. Run CLI
        python cli.py
            or
        python3 cli.py

# Data Models and Schema - models.py

    Game: Game table includes the title, ESRB rating, genre, and platforms.

    Genre: Genre table represents game genre.

    Platform: Platform table represents game platform.

    Game/Platform Join Table: Join table represents the associates between the Game and Platform Table.

# Seed - seed.py

The seed.py file sets up the database with example game data, like titles, genres, and platforms, gathered from an external external API.

# CLI - cli.py

<h3>main_menu() and render_main_main()</h3> 
<h4>These functions will display and operate the main menu with several options:</h4>

    My Games: View and search games.

    Edit Games: Add, edit, or delete games.

    Exit: Exit the application.

<h3>my_games() and render_my_games()</h3>
<h4>These functions will display and operate the my games menu with several options:</h4>

        View All Games: Display information about all available games.

        Search Game By Title: Search for games by title.

        Search Game By Platform: Search for games by platform - platform_search() function.

        Main Menu: Return to the main menu.

        Exit: Exit the application.

<h3>edit_games() and render_edit_games()</h3>
<h4>These functions will display and operate the edit games menu with several options:</h4>

        Add A Game: Add a new game to the catalog - add_game() fucntion.

        Edit A Game: Modify information about an existing game - modify_game() function.

        Delete A Game: Delete a game from the catalog - delete_game() function.

        Main Menu: Return to the main menu.

        Exit: Exit the application.

# Helpers - helpers.py

<h3>print_game_info(game)</h3> 
<h4>Function that takes game data as an argument and display the id, title, genre, and platform.</h4>

# API

The sample data for the catalog is fetched from 'https://www.mmobomb.com/api', an external API to seed the initial database.
