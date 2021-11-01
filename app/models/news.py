class News:
    '''
    News class to define news objects
    '''

    def __init__(self,id,name,url,description,country,urlToImage):
        self.id =id
        self.name = name
        self.url = url
        self.description = description
        self.country = country
        self.urlToImage = urlToImage
    
class Articles:
    '''
    class that defines the behaviour of the articles
    '''
    def __init__(self, title, description, urlToImage, publishedAt, author, url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.author = author
        self.url = url        
                   