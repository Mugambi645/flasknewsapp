from instance.config import NEWS_API_KEY
import os
class Config:
    """
    General configurations parent class
    """
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
    Config:The parent configuration class with parent config settings
    """
    pass


class DevConfig(Config):
    """
    Development configuration child class
    Args:
    Config: Parent configuration class 
    """
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
    }   