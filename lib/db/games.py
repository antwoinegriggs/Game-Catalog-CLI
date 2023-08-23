from base import Base
from game_platform_join import game_platform_join
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer(), primary_key=True)
    title = Column(String)
    esrb_rating = Column(String)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    
    genre = relationship("Genre",  backref="game_genre")
    platform = relationship("Platform", secondary=game_platform_join, backref="game_platform")


    def __repr__(self):
        return f"\n<Game " \
            + f"id = {self.id}, " \
            + f"title = {self.title}, " \
            + f"esrb_rating = {self.esrb_rating}, " \
            +">"