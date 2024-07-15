# The lines `import os`, `from os import environ, path`, and `from dotenv import load_dotenv` are used
# to import necessary modules and functions for working with environment variables and loading them
# from a `.env` file in a Python script.
import os
from os import environ,path
from dotenv import load_dotenv

# `basedir = os.path.abspath(os.path.dirname(__name__))` is a line of code that is used to get the
# absolute path of the directory where the current Python script is located. Here's a breakdown of
# what each part of the code does:
basedir = os.path.abspath(os.path.dirname(__name__))

# `load_dotenv(path.join(basedir,".env"))` is a line of code that loads environment variables from a
# .env file located in the same directory as the Python script. The `load_dotenv` function from the
# `dotenv` library is used to load these environment variables into the script's environment, making
# them accessible through `environ.get()` calls. This is a common practice for storing sensitive
# information like API keys, database URIs, and other configuration settings outside of the codebase.
load_dotenv(path.join(basedir,".env"))

# The `Config` class defines configuration settings for a Python application, including the secret key
# and database URI.
class Config:
    SECRET_KEY = environ.get('SECRET_KEY') #generate with secrets module and secrets.token_hex()
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True