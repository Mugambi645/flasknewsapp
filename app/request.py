from os import name
from app import app
import urllib.request,json
from newsapi import NewsApiClient
from .models import news
News = news.News
#getting api key
api_key = app.config["NEWS_API_KEY"]

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
        #overview = news_item.get("overview")
        #poster = news_item.get("poster_path")

        if url:
            news_object = News(id,name, url)
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


