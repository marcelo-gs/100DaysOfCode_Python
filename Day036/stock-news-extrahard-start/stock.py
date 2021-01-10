import requests

class Stock():

    ALPLHAVANTAGE_API_KEY = "AplhaAPIKEY"

    def __init__(self, symbol:str, company_name="") -> None:
        self.symbol = symbol
        self.company_name = company_name
        self.URL = "https://www.alphavantage.co/query"
        self.data = ""
        self.function = "TIME_SERIES_DAILY_ADJUSTED"
        self.parameters = {
            "function"  : self.function,
            "symbol": self.symbol,
            "apikey": self.ALPLHAVANTAGE_API_KEY
        }
        self.variation = 0.0
        self.yestarday_open = 0.0
        self.before_yestarday_close = 0.0
        self.percent_variation = 0
        self.direction = "up"
        self.direction_symbol = "🔺"
        self.yestarday_date = ""

    def get_stock(self):
        self.data = requests.get(self.URL, self.parameters)
        self.data.raise_for_status()
        self.iter_stock = iter(self.data.json()["Time Series (Daily)"].values())
        self.yestarday_date = next(iter(self.data.json()["Time Series (Daily)"]))
        self.yestarday_stock = next(self.iter_stock)
        self.before_yestarday_stock = next(self.iter_stock)
        
    def get_variation(self) -> float:
        self.get_stock()
        self.before_yestarday_close = float(self.before_yestarday_stock["5. adjusted close"])
        self.yestarday_open = float(self.yestarday_stock["1. open"])
        # Test only 
        # self.yestarday_open = 10.0
        self.variation = round(self.yestarday_open - self.before_yestarday_close,2)
        self.direction = "up"
        self.direction_symbol = "🔺"
        if self.variation < 0:
            self.variation *= -1
            self.direction = "down"
            self.direction_symbol = "🔻"
        self.percent_variation = round(self.variation / self.yestarday_open,2)
        return self.percent_variation

    def get_display_info(self):
        """***** Used only for information about the Class, no functional propose *****"""
        print("Show information about this Class -- Just for debuging")
        display = f"""
        Symbol: {self.symbol}
        Company Name: {self.company_name}
        URL: {self.URL}
        Parameters: {self.parameters}
        ----------------------------------------
        Values:
        ----------------------------------------
        Yestarday date: {self.yestarday_date}
        Yestarday Open Value: {self.yestarday_open}
        Before yestarday close value: {self.before_yestarday_close}
        Variation {self.variation} -> {self.direction}
        Percent of Variation: {self.percent_variation}% {self.direction_symbol}
        """
        print(display)


# c = Stock("TSLA")
# c.get_variation()
# c.get_display_info()