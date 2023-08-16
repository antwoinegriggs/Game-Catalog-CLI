from models import Genre, Platform, Game
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(Genre).delete()
session.query(Platform).delete()
session.query(Game).delete()


genres = ['action', 'adventure', 'strategy',
        'puzzle', 'first-person shooter', 'racing']

platforms = ['nintendo 64', 'gamecube', 'wii', 'wii u', 'switch',
        'playstation', 'playstation 2', 'playstation 3', 'playstation 4',
        'playstation 5', 'xbox', 'xbox 360', 'xbox one', 'pc']

games = []

for _ in range(15):
    game = Game(
        title = faker.unique.name(),
        genre=random.choice(genres),
        platforms=random.choice(platforms)
    )

    session.add(game)
    session.commit()



# session.bulk_save_objects()
