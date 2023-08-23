from base import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer(), primary_key=True)
    type = Column(String)

    def __repr__(self):
        return f"\n<Genre " \
            + f"id = {self.id}, " \
            + f"type = {self.type}" \
            +">"