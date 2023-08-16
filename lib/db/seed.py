from faker import Faker
fake = Faker()
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

games = []

esrb_rating = ['Everyone', 'Everyone 10+','Teen','Mature','Adult']
# API request MMO Games
response = requests.get('https://www.mmobomb.com/api1/games')
json_data = json.loads(response.text)

new_data = list(range(len(json_data)))


for _ in range(20):
    random_game = random.choice(new_data)
    games.append(json_data[random_game])

print("....")

platforms = set()
genres = set()
genre = []
for game in games:
    print(game)
    add_game = Game(
        title = game["title"],
        esrb_rating = random.choice(esrb_rating)

        
    )

    platform = game["platform"]
    if platform not in platforms:
        platforms.add(platform)
        add_platform = Platform(
            name = platform
        )

    genre = game["genre"]
    if genre not in genres:
        genres.add(genre)
        add_genre = Genre(
            type = genre
        )
    
    session.add(add_genre)
    session.add(add_platform)
    session.add(add_game)
    
    session.commit()
   
print('Seeding Complete')
import ipdb; ipdb.set_trace()

# session.bulk_save_objects()



# print(json_data["title"])
# print(json_data["platform"])
# print(json_data["release_date"])
# print(json_data["genre"])

