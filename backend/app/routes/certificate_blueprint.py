from flask import Blueprint
from app.controllers.certificate_controller import (
    create_certificate,
    delete_certificate,
    get_certificate_by_id,
    list_all_certificates,
    update_certificate,
)

bp = Blueprint("certificate_bp", __name__, url_prefix="/certificate")

bp.post("")(create_certificate)
bp.get("/<int:id>")(get_certificate_by_id)
bp.get("")(list_all_certificates)
bp.patch("/<int:certificate_id>")(update_certificate)
bp.delete("/<int:id>")(delete_certificate)
