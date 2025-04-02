from backend.core import TimestampModel
from sqlalchemy import Column, String


class Player(TimestampModel):
    __tablename__ = 'players'

    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<Player {self.username}>'