from flask import Flask
from app.config import env_configs, database, migration
from app.routes import certificate_blueprint
from flask_cors import CORS

def create_app():

    app = Flask(__name__)
    cors = CORS(app)
    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)

    app.register_blueprint(certificate_blueprint.bp)

    return app
