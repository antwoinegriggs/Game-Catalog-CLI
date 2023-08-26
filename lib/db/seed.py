# Packages
import random
import requests
import json

# Schemas
from base import Base
from games import Game
from platforms import Platform
from genres import Genre
from game_platform_join import game_platform_join

# Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print('Seeding Started...')
engine = create_engine('sqlite:///data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Clear data
session.query(Genre).delete()
session.query(Platform).delete()
session.query(Game).delete()
session.query(game_platform_join).delete()

# Variables
esrb_rating = ['Everyone', 'Everyone 10+', 'Teen', 'Mature', 'Adult']

# API request from MMO Games
response = requests.get('https://www.mmobomb.com/api1/games')
json_data = json.loads(response.text)

# Extract platform data from the API response
platforms = set()
for game in json_data:
    platforms.add(game["platform"])

# Convert platform data to a list of dictionaries
platforms_list = [{"name": platform} for platform in platforms]

# Load platform data into the database
for platform_data in platforms_list:
    platform_name = platform_data["name"]
    existing_platform = session.query(Platform).filter_by(name=platform_name).first()
    if not existing_platform:
        add_platform = Platform(name=platform_name)
        session.add(add_platform)
        session.commit()

# Assign random games from data
games = []
for _ in range(1):
    random_game = random.choice(json_data)
    games.append(random_game)

# Game
for game_data in games:
    add_game = Game(
        title = game_data["title"],
        esrb_rating = random.choice(esrb_rating),
        type_genre = game_data["genre"],
        name_platform = game_data["platform"]
    )
    
    # Check for duplicate and assign platform
    platform_name = game_data["platform"]
    existing_platform = session.query(Platform).filter_by(name=platform_name).first()
    if existing_platform:
        add_game.platform_id = existing_platform.id
    else:
        new_platform = Platform(name=platform_name)
        session.add(new_platform)
        session.commit()
        add_game.platform_id = new_platform.id
    
    # Check for duplicate and assign genre
    genre_type = game_data["genre"]
    existing_genre = session.query(Genre).filter_by(type=genre_type).first()
    if existing_genre:
        add_game.genre = existing_genre
    else:
        new_genre = Genre(type=genre_type)
        session.add(new_genre)
        session.commit()
        add_game.genre = new_genre
    
    # Commit Game
    session.add(add_game)
    session.commit()

print('Seeding Complete')
import ipdb; ipdb.set_trace()
