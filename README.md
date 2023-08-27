# Phase 3 CLI Project

Data Models and Schema - models.py

Game: Game table includes the title, ESRB rating, genre, and platforms.

Genre: Genre table represents game genre.

Platform: Platform table represents game platform.

Game/Platform Join Table: Join table represents the associates between the Game and Platform Table.

Seed - seed.py

CLI - cli.py

main_menu() and render_main_main() - These functions will display and operate the main menu with several options:

    My Games: View and search games.

    Edit Games: Add, edit, or delete games.

    Exit: Exit the application.

my_games() and render_my_games() - These functions will display and operate the my games menu with several options:

        View All Games: Display information about all available games.

        Search Game By Title: Search for games by title.

        Search Game By Platform: Search for games by platform via platform_search() function.

        Main Menu: Return to the main menu.

        Exit: Exit the application.

edit_games() and render_edit_games - These functions will display and operate the edit games menu with several options:

        Add A Game: Add a new game to the catalog via add_game() fucntion.

        Edit A Game: Modify information about an existing game via modify_game() function.

        Delete A Game: Delete a game from the catalog via delete_game() function.

        Main Menu: Return to the main menu.

        Exit: Exit the application.

Helpers - helpers.py

print_game_info(game) - Function that takes game data as an argument and display the id, title, genre, and platform.

API
The sample data for the catalog is fetched from 'https://www.mmobomb.com/api', an external API to seed the initial database.
