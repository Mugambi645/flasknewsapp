from flask import Flask
#initializing the application
app = Flask(__name__)
from app import views
