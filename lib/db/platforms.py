from base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer(), primary_key=True)
    name = Column(String)

    # games = relationship("Game", backref="platform_game")

    def __repr__(self):
        return f"\n<Platform " \
            + f"id = {self.id}, " \
            + f"name = {self.name} " \
            +">"