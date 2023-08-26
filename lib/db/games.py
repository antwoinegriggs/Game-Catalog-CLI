from base import Base
from game_platform_join import game_platform_join

from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship




class Game(Base):
    __tablename__ = "games"
    __table_args__= (PrimaryKeyConstraint("id"),)

    genre = relationship("Genre",  backref="the_game")
    platform = relationship("Platform", secondary=game_platform_join, backref="the_game")
  
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    esrb_rating = Column(String())
    name_platform = Column(String())
    platform_id = Column(Integer(), ForeignKey("platforms.id"), nullable=True)
    type_genre = Column(String())
    genre_id = Column(Integer(), ForeignKey("genres.id"))
    

    def __repr__(self):
        return f"\n<Game " \
            + f"id = {self.id}, " \
            + f"title = {self.title}, " \
            + f"esrb_rating = {self.esrb_rating}, " \
            +">"