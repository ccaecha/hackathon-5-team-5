from flask import Flask
from .main import routes as main_blueprint

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(main_blueprint.main)

    return app