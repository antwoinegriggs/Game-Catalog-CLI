from faker import Faker
fake = Faker()
import random
from models import Genre, Platform, Game, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# session.query(Genre).delete()
# session.query(Platform).delete()
session.query(Game).delete()


genres = ['action', 'adventure', 'strategy',
        'puzzle', 'first-person shooter', 'racing']

platforms = ['nintendo 64', 'gamecube', 'wii', 'wii u', 'switch',
        'playstation', 'playstation 2', 'playstation 3', 'playstation 4',
        'playstation 5', 'xbox', 'xbox 360', 'xbox one', 'pc']

esrb_rating = ['Everyone', 'Everyone 10+','Teen','Mature','Adult']



for _ in range(15):
    games = Game(
        title = fake.unique.name(),
        esrb_rating = random.choice(esrb_rating)
    )
    session.add(games)
    session.commit()
   
print('Seeding....')
import ipdb; ipdb.set_trace()

# session.bulk_save_objects()
