from models import Genre, Platform, Game
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(Genre).delete()
session.query(Platform).delete()
session.query(Game).delete()

from faker import Faker

session.bulk_save_objects()
session.commit()