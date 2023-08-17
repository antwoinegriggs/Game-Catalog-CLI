from base import Base
from game_genre_join import game_genre_join
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer(), primary_key=True)
    type = Column(String)

    games = relationship("Game", secondary=game_genre_join, backref="join_genre")
    

    def __repr__(self):
        return f"\n<Genre " \
            + f"id = {self.id}, " \
            + f"type = {self.type}" \
            +">"