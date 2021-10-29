from flask import Flask
from .config import DevConfig
#initializing the application
app = Flask(__name__)
#setting up configuration
app.config.from_object(DevConfig)
from app import views
