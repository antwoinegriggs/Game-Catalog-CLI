from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import MetaData, Column, Integer, String, Table, ForeignKey


Base = declarative_base(metadata=MetaData())


game_platform_join = Table(
    "game_platforms",
    Base.metadata,
    Column("id",Integer, primary_key=True),
    Column("game_id", ForeignKey("games.id")),
    Column("platform_id", ForeignKey("platforms.id"))
)

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    esrb_rating = Column(String())
    name_platform = Column(String())
    platform_id = Column(Integer(), ForeignKey("platforms.id"), nullable=True)
    type_genre = Column(String())
    genre_id = Column(Integer(), ForeignKey("genres.id"))

    genre = relationship("Genre",  backref="the_game")
    platform = relationship("Platform", secondary=game_platform_join)
  
class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer(), primary_key=True)
    type = Column(String())

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True)
    name = Column(String())
