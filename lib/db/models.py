from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table


Base = declarative_base()


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    type = Column(String)

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True)
    name = Column(String)\
    
class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    title = Column(String)



