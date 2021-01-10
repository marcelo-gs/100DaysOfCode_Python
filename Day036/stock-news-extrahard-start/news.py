# "http://newsapi.org/v2/everything"
# ?
# q=apple
# from typing import NoReturn
# from=2021-01-09
# to=2021-01-09
# sortBy=popularity
# apiKey=
# everything or top-headlines
import requests

class News():

    NEWSAPI_APIKEY = "NewsAPIKEY"
    def __init__(self, news_about, news_date) -> None:
        self.news_date = news_date
        self.news_about = news_about
        self.url = "http://newsapi.org/v2/everything"
        self.parameters ={ 
            "q" : self.news_about, 
            "from": self.news_date, 
            "to": self.news_date,
            "sortBy":"popularity", 
            "apiKey": self.NEWSAPI_APIKEY
        }
        self.get_news()

    def get_news(self):
        self.data = requests.get(self.url, self.parameters).json()
        self.articles = [str(article["title"]) + " By " + str(article["author"]) + " - (" + str(article["source"]["name"]) + ")"  for article in self.data["articles"]]
        self.totalResults = int(self.data["totalResults"])
    
    def get_top3_news(self) -> list[str]:
        if self.totalResults > 3:
            return self.articles[:3]
        else:
            return self.articles

    def get_display_info(self):
        """***** Used only for information about the Class, no functional propose *****"""
        print("Show information about this Class -- Just for debuging")
        display = f"""
        News About: {self.news_about}
        News Date: {self.news_date}
        URL: {self.url}
        Parameters: {self.parameters}
        ----------------------------------------
        Values:
        ----------------------------------------
        Total Results: {self.totalResults}
        Top3 : {self.get_top3_news()}
        ----------------------------------------
        Articles: {self.articles}

        """
        print(display)
