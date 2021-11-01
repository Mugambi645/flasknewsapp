

from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_news_articles,get_category
#views
@main.route("/")
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
        return redirect(url_for('search', article_name=search_article))
    else:
        return render_template("index.html", general = general_news, sport = sports_news, entertainment = entertainment_news, health = health_news, business = business_news, tech = tech_news, science = science_news)



@main.route('/articles/<id>')
def articles(id):
    '''
    View article function that returns the articles in a source
    '''
    articles = get_news_articles(id)
    return render_template('articles.html', id = id, articles = articles)


@main.route('/category/<tab>')
def category(tab):
    '''
    Category page function that returns the category page and its data
    '''

    source_news = get_news(tab)
    category = get_category(tab)
    return render_template('category.html',news = source_news , category = category)