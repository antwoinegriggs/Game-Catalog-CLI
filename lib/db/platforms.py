from base import Base
from game_platform_join import game_platform_join
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class Platform(Base):
    __tablename__ = "platforms"
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    
   
    
    def __repr__(self):
        return f"\n<Platform " \
            + f"id = {self.id}, " \
            + f"name = {self.name} " \
            +">"