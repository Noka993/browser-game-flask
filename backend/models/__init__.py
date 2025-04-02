from backend.core.database import db
from backend.core.database import TimestampModel
from sqlalchemy.dialects.postgresql import UUID


class Player(TimestampModel):
    __tablename__ = "players"

    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    towns = db.relationship("Town", backref="player", lazy=True)

    def __repr__(self):
        return f"<Player {self.username}>"


class Town(TimestampModel):
    __tablename__ = "towns"

    player_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("players.id"), nullable=False
    )
    name = db.Column(db.String(80), nullable=False)
    population = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Town {self.name}>"
