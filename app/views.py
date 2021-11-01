

from flask import render_template,request,redirect,url_for
from .request import get_news,search_article,get_news_articles,get_category
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
        return redirect(url_for('search', article_name=search_article))
    else:
        return render_template("index.html", general = general_news, sport = sports_news, entertainment = entertainment_news, health = health_news, business = business_news, tech = tech_news, science = science_news)



@app.route('/articles/<id>')
def articles(id):
    '''
    View article function that returns the articles in a source
    '''
    articles = get_news_articles(id)
    return render_template('articles.html', id = id, articles = articles)
@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',article = searched_articles)
   


@app.route('/category/<tab>')
def category(tab):
    '''
    Category page function that returns the category page and its data
    '''

    source_news = get_news(tab)
    category = get_category(tab)
    return render_template('category.html',news = source_news , category = category)