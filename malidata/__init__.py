from flask import Flask
from flask_bootstrap import Bootstrap

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    Bootstrap(app)

    with app.app_context():
        from . import routes

        return app
