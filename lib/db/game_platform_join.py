from base import Base
from sqlalchemy import Column, Integer, Table, ForeignKey


game_platform_join = Table(
    "game_platforms",
    Base.metadata,
    Column("id",Integer, primary_key=True),
    Column("game_id", ForeignKey("games.id")),
    Column("platform_id", ForeignKey("platforms.id"))
)