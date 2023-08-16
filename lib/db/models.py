from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


Base = declarative_base()


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer(), primary_key=True)
    type = Column(String)

    games = relationship("Game", backref="genre_game")
    

    def __repr__(self):
        return f"\n<Genre " \
            + f"id = {self.id}, " \
            + f"type = {self.type}" \
            +">"

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer(), primary_key=True)
    name = Column(String)

    games = relationship("Game", backref="platform_game")

    def __repr__(self):
        return f"\n<Platform " \
            + f"id = {self.id}, " \
            + f"name = {self.name} " \
            +">"
    
class Game(Base):
    __tablename__ = "games"

    id = Column(Integer(), primary_key=True)
    title = Column(String)
    esrb_rating = Column(String)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    
    genre = relationship("Genre", backref="game_genre")
    platform = relationship("Platform", backref="game_genre")


    def __repr__(self):
        return f"\n<Game " \
            + f"id = {self.id}, " \
            + f"title = {self.title}, " \
            + f"esrb_rating = {self.esrb_rating}, " \
            +">"



