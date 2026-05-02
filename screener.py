import yfinance as yf
import pandas as pd

def typical_price(price: pd.Series) -> list:
    '''
    Calculates typical price of an index on a certain day. 

    Parameters: 
    price: A DataFrame object with ticker price data

    Returns: 
    Series of typical prices for the tickers.
    '''
    tickers: list[str] = price.index.get_level_values(1).unique().tolist()

    typical_prices: list[float] = []

    # input is a series of the COHL prices for one day per ticker. 
    for t in tickers:
        tp = (price["Close", t]  + price["High", t] + price["Low", t]) / 3
        typical_prices.append(tp)

    return typical_prices

def load(ticker: list[str] | str, start: str, end: str) -> pd.Series | pd.DataFrame:
    '''
    loads price history of a stock ticker (or list of stock tickers). 

    Parameters:
    ticker: list or string of stock tickers
    start: string for starting date, formatted yyyy-mm-dd.
    end: string for ending date, formatted yyyy-mm-dd.

    Returns:
    A series or Dataframe of daily typical price data for the given tickers.
    '''

    df = yf.download(ticker, start, end)

    if type(ticker) == list:
        for t in ticker:
            df["typ", t] = df.apply(lambda row: typical_price(row)[tickers.index(t)], axis = 1)
    else:
        df["typ", t] = df.apply(lambda row: typical_price(row), axis = 1).

    return df["typ"]



def ret(mkt_data: pd.DataFrame | pd.Series) -> pd.Series | pd.DataFrame:
    '''
    calculates returns for a stock or list of stocks.

    Parameters: 
    mkt_data: a dataframe containing typical price data for some tickers.
    
    Returns:
    A series or dataframe showing daily percentage returns for some tickers.
    '''
    


def sharpe(mkt_data: pd.DataFrame | pd.Series) -> list[float]:
    '''
    calculates individual EOY Sharpe ratio for a stock or list of stocks.

    Parameters:
    mkt_data: a dataframe containing typical price data for some tickers.

    Returns: 
    A list of floats, showing individualized sharpe ratios for the stocks.
    '''

    raise NotImplementedError
