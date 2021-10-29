class Config:
    """
    General configurations parent class
    """
    pass

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
    Config:The parent configuration class with parent config settings
    """
    MOVIE_API_BASE_URL ="https://newsapi.org/v2/everything{}?&apiKey={}"


class DevConfig(Config):
    """
    Development configuration child class
    Args:
    Config: Parent configuration class 
    """
    DEBUG = True
