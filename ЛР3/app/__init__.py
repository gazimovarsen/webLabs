from flask import Flask

app = Flask(__name__)

from .profile import profile as profile_blueprint
app.register_blueprint(profile_blueprint)
