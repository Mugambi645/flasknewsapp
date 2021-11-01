

from flask import render_template,request,redirect,url_for
from .request import get_news,search_article
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
    entertainment_news = get_news('entertainment')
    health_news = get_news('health')
    business_news = get_news('business')
    tech_news = get_news('technology')
    science_news = get_news('science')

    search_article = request.args.get('news_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
        return render_template("index.html", general = general_news, sport = sports_news)

