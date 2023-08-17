# from faker import Faker
# fake = Faker()
import random
import requests
import json
from models import Genre, Platform, Game, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print('Seeding Started...')
engine = create_engine('sqlite:///data.db')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.query(Genre).delete()
session.query(Platform).delete()
session.query(Game).delete()

# Variables
games = []
esrb_rating = ['Everyone', 'Everyone 10+','Teen','Mature','Adult']
platforms = set()
genres = set()

# API request from MMO Games
response = requests.get('https://www.mmobomb.com/api1/games')
json_data = json.loads(response.text)

# Get length of data and assign to list for data manipulation
data_index = list(range(len(json_data)))

# 
for _ in range(50):
    random_game = random.choice(data_index)
    games.append(json_data[random_game])


for game in games:
    print(game)

    add_game = Game(
        title = game["title"],
        esrb_rating = random.choice(esrb_rating))
    
    
    platform_name = game["platform"]
    existing_platform = session.query(Platform).filter_by(name=platform_name).first()
    
    if existing_platform:
        add_game.platform = existing_platform
    else:
        add_platform = Platform(name=platform_name)
        add_game.platform = add_platform
        session.add(add_platform)
        

    genre_name = game["genre"]
    existing_genre = session.query(Genre).filter_by(type=genre_name).first()
    
    if existing_genre:
        add_game.genre = existing_genre
    else:
        add_genre = Genre(type=genre_name)
        add_game.genre = add_genre
        session.add(add_genre)
    
    print(platforms)
    session.add(add_game)
    session.commit()
   
print('Seeding Complete')
import ipdb; ipdb.set_trace()



