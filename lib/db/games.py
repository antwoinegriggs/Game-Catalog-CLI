from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer(), primary_key=True)
    title = Column(String)
    esrb_rating = Column(String)
    genre_id = Column(Integer(), ForeignKey("genres.id"))
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    
    genre = relationship("Genre", backref="game_genre")
    platform = relationship("Platform", backref="game_platform")


    def __repr__(self):
        return f"\n<Game " \
            + f"id = {self.id}, " \
            + f"title = {self.title}, " \
            + f"esrb_rating = {self.esrb_rating}, " \
            +">"