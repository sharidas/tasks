"""
We create our app here
"""
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from flask import Flask, current_app, url_for
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app(env=None):
    """
    Create the app and return the app object
    """
    app = Flask(__name__, template_folder="templates")

    with app.app_context():
        if env == "production":
            app.config.from_object(__name__ + ".ProductionConfig")
        elif env == "development":
            app.config.from_object("config.DevelopmentConfig")
        else:
            app.config.from_object("config.TestingConfig")

        #jinja_env.auto_reload = True
        app.jinja_environment.auto_reload = True
        db = SQLAlchemy(app)
        ma = Marshmallow(app)

        current_app.ma = ma
        current_app.db = db

        from savedata.saveview import index_api, save_api
        app.register_blueprint(save_api, url_prefixes="/pages")
        app.register_blueprint(index_api)

        migrate = Migrate(app, db)

    return app
