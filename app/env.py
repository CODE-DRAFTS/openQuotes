from os import environ


DATABASE_HOST = environ.get("DATABASE_HOST")
DATABASE_PORT =environ.get("DATABASE_PORT")
DATABASE_USER =environ.get("DATABASE_USER")
DATABASE_NAME = environ.get("DATABASE_NAME")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")