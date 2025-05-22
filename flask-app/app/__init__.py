from flask import Flask
from .main import routes as main_blueprint


def create_app():
    app = Flask(__name__)
    app.secret_key = (
        "secret_key_for_sessions"  # Set a secret key for session management
    )
    app.register_blueprint(main_blueprint.main)

    return app
