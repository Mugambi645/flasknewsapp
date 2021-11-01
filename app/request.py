from os import name
from app import app
import urllib.request,json
from newsapi import NewsApiClient
from .models import news
from .models.news import Articles
News = news.News

#getting api key
api_key = app.config["NEWS_API_KEY"]
articles_url = app.config["ARTICLES_URL"]
#getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def process_results(news_list):
    """
    Function that processes the news results and transform them into a list of objects
    Args:
    news_list: a list of dictionaries that contain news details
    Returns:
    News_results: A list of news objects
    """
    news_results = []
    for news_item in news_list:
        id = news_item.get("id")
        name = news_item.get("name")
        url = news_item.get("url")
        description = news_item.get("description")
        country = news_item.get("country")
        urlToImage = news_item.get("urlToImage")
        #overview = news_item.get("overview")
        #poster = news_item.get("poster_path")

        if url:
            news_object = News(id,name, url, description, country, urlToImage)
            news_results.append(news_object)
    
    return news_results



    


def get_news(category):
    """
    function that gets the json response to our url request
    """
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None

        if get_news_response["sources"]:
            news_results_list = get_news_response["sources"]
            news_results = process_results(news_results_list)
    
    return news_results


def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(api_key, article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            search_article_list = search_article_response['results']
            search_article_results = process_results(search_article_list)


    return search_article_results



def get_news_articles(id):
    get_news_articles_url = articles_url.format(id, api_key)
    
    with urllib.request.urlopen(get_news_articles_url ) as url:
        news_articles_data = url.read()
        news_articles_response = json.loads(news_articles_data)
        
        articles_results = None
        if news_articles_response['articles']:
            articles_results_list = news_articles_response['articles']
            articles_results = process_articles(articles_results_list)
            
    return articles_results


def process_articles(articles_list):
    '''
    method for processing the response
    '''
    articles_results = []
    for article_item in articles_list:
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item['description']
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
            # (self, title, description, urlToImage, publishedAt, author, url):
            if urlToImage:
                articles_object = Articles(title, description, urlToImage, publishedAt, author,url)
                articles_results.append(articles_object)
            
    return articles_results
