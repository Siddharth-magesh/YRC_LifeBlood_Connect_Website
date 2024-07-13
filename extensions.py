# This code snippet is importing the `SQLAlchemy` class from the `flask_sqlalchemy` module and
# creating an instance of it named `db`. `SQLAlchemy` is a popular Python SQL toolkit and
# Object-Relational Mapping (ORM) library that simplifies database operations in Flask applications.
# By creating an instance of `SQLAlchemy`, you can interact with your database using SQLAlchemy ORM
# features within your Flask application.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()