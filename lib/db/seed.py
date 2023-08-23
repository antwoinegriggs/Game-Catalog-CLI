# Packages
import random
import requests
import json

# Schemas
from base import Base
from platforms import Platform
from genres import Genre
from games import Game
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
games = []
esrb_rating = ['Everyone', 'Everyone 10+','Teen','Mature','Adult']

# API request from MMO Games
response = requests.get('https://www.mmobomb.com/api1/games')
json_data = json.loads(response.text)

# Get length of data and assign to list for data manipulation
data_index = list(range(len(json_data)))

# Loop to manipulate and append data to games
for _ in range(5):
    random_game = random.choice(data_index)
    games.append(json_data[random_game])


for game in games:
    # Game
    add_game = Game(
        title = game["title"],
        esrb_rating = random.choice(esrb_rating))
    
    # Platform
    platform_name = game["platform"]

    # Check for duplicate platforms
    # Not compatiable need to be list-like
    existing_platform = session.query(Platform).filter_by(name=platform_name).first()
    if existing_platform:
        add_game.platform.append(existing_platform)
    else:
        add_platform = Platform(name=platform_name)
        add_game.platform.append(add_platform)
        session.add(add_platform)
        
    # Genre
    genre_type = game["genre"]

    # Check for duplicate genre
    existing_genre = session.query(Genre).filter_by(type=genre_type).first()
    if existing_genre:
        add_game.genre = existing_genre 
    else:
        add_genre = Genre(type=genre_type)
        add_game.genre = add_genre
        session.add(add_genre)
        


    # Commit
    session.add(add_game)
    session.commit()
  
print('Seeding Complete')
import ipdb; ipdb.set_trace()



