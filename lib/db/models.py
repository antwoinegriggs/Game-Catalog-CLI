from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date


Base = declarative_base()


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer(), primary_key=True)
    type = Column(String)

    def __repr__(self):
        return f"\n<Genre " \
            + f"id = {self.id}, " \
            + f"type = {self.type}" \
            +">"

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer(), primary_key=True)
    name = Column(String)

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


    def __repr__(self):
        return f"\n<Game " \
            + f"id = {self.id}, " \
            + f"title = {self.title}, " \
            + f"esrb_rating = {self.esrb_rating}, " \
            +">"



