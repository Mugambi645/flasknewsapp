

from flask import render_template
from .request import get_news
from app import app
#views
@app.route("/")
def index():
    """
    View root page that returns the index page and its data
    """
    #getting news
    general_news = get_news("general")
    sports_news = get_news("sports")
    
    return render_template("index.html", general = general_news, sport = sports_news)
