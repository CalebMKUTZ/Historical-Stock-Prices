import json
import matplotlib.pyplot as plt
import requests


url = "https://global-market-data.p.rapidapi.com/stock/historical_data"

headers = {
	"X-RapidAPI-Key": "7e13738764mshf269b65b399187fp1b41e2jsnbdf68f29276b",
	"X-RapidAPI-Host": "global-market-data.p.rapidapi.com"
}


class ApiCall:
    def __init__(self, method, url, headers, params):
        self.method = method
        self.url = url
        self.headers = headers
        self.params = params
        self.response = requests.request(self.method, self.url, headers=self.headers, params=self.params)

    def get_response(self):
        return self.response


class MakeGraph:
    def __init__(self, title, x_label, y_label, x_data, y_data):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.x_data = x_data
        self.y_data = y_data
    
    def make_graph(self):
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.plot(self.x_data, self.y_data)
        plt.show()



def make_request(ticker):
    querystring = {"from_date":"2021-01-01","stock":ticker,"country":"united states","to_date":"2021-12-31","interval":"Daily"}
    request = ApiCall("GET", url, headers, querystring)
    response = request.get_response()
    return response.json()


def get_prices(ticker):
    prices = []
    data = make_request(ticker)

    for d in data:
        prices.append(d["close"])
    
    return prices


def get_dates(ticker):
    dates = []
    data = make_request(ticker)

    for d in data:
        dates.append(d["date"])
    
    return dates


def make_graph(ticker):
    prices = get_prices(ticker)
    dates = get_dates(ticker)
    graph = MakeGraph(f"{ticker} HISTORICAL DATA", "DATES", "PRICES", dates, prices)
    graph.make_graph()


if __name__ == "__main__":
    ticker = input("ENTER THE TICKER SYMBOL OF ANY STOCK: ")
    print(f"[GRAPHING] making new graph for {ticker}")
    make_graph(ticker)