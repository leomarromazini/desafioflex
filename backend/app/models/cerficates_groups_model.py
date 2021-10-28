from dataclasses import dataclass
from app.config.database import db


@dataclass
class Certificates_groups(db.Model):

    id: int
    certificate_id: int
    group_id = int

    __tablename__ = "certificates_groups"

    id = db.Column(db.Integer, primary_key=True)
    certificate_id = db.Column(
        db.Integer, db.ForeignKey("certificate.id"), nullable=False
    )
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
