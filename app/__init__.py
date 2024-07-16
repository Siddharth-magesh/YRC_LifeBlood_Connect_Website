# The code snippet you provided is a Python script for creating a Flask application. Let's break down
# what each line is doing:
from flask import Flask
from .extensions import db
from .config import Config
from .routes.main import main
from .routes.admin import admin

def create_app(config_class = Config):
    """
    The function creates a Flask application with specified configuration and initializes a database.
    
    :param config_class: The `config_class` parameter in the `create_app` function is used to specify
    the configuration class that should be used for configuring the Flask application. By default, it is
    set to `Config`, which is a custom configuration class that likely contains settings for the Flask
    application such as database connection details,
    :return: The function `create_app` is returning an instance of the Flask application with the
    specified configuration class, database initialization, blueprint registration, and database
    creation within the application context.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(admin)

    with app.app_context():
        db.create_all()

    return app