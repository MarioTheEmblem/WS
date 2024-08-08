import requests
import pandas as pd

def get_stock_data(symbol='IBM'):

    base = 'https://www.alphavantage.co'
    endpoint = '/query'
    URL=  base + endpoint
    
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "full",
        "apikey": 'G6J7BB76C6AR6WKQ'
    }

    res = requests.get(URL,params)
    data = res.json()

    df =pd.DataFrame(data['Time Series (Daily)']).T.astype(float)
    df.columns = ['open', 'high', 'low', 'close', 'volumen']
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df