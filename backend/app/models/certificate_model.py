from dataclasses import dataclass
from datetime import date, datetime
from sqlalchemy.orm import relationship
from app.config.database import db


@dataclass
class Certificate(db.Model):

    id: int
    username: str
    name: str
    description: str
    expiration: int
    expirated_at: date
    created_at: date
    updated_at: date

    __tablename__ = "certificate"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String)
    expiration = db.Column(db.Integer)
    expirated_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), default=datetime.now())

    groups = relationship(
        "Group", backref="certificate", secondary="certificates_groups"
    )
