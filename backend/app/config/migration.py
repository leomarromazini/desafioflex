from flask_migrate import Migrate
from flask import Flask


def init_app(app: Flask):

    from app.models.certificate_model import Certificate
    from app.models.group_model import Group
    from app.models.cerficates_groups_model import Certificates_groups

    Migrate(app, app.db)
