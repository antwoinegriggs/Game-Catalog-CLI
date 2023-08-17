from base import Base
from sqlalchemy import Column, Integer, Table, ForeignKey


game_genre_join = Table(
    "game_genres",
    Base.metadata,
    Column("id",Integer, primary_key=True),
    Column("game_id", ForeignKey("games.id")),
    Column("genre_id", ForeignKey("genres.id"))
)