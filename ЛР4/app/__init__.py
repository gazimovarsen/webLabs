from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .profile.__init__ import profile as profile_blueprint

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

app.register_blueprint(profile_blueprint)
