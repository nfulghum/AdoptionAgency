from flask import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(self):
    db.app = app
    db.init_app(app)
