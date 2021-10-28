from dataclasses import dataclass
from app.config.database import db


@dataclass
class Group(db.Model):

    id: int
    type: int

    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False, unique=True)
