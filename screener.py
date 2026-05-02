import yfinance as yf
import pandas as pd

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

    raise NotImplementedError

def ret(mkt_data: pd.DataFrame | pd.Series) -> pd.Series | pd.DataFrame:
    '''
    calculates returns for a stock or list of stocks.

    Parameters: 
    mkt_data: a dataframe containing typical price data for some tickers.
    
    Returns:
    A series or dataframe showing daily percentage returns for some tickers.
    '''

    raise NotImplementedError

def sharpe(mkt_data: pd.DataFrame | pd.Series) -> list[float]:
    '''
    calculates individual EOY Sharpe ratio for a stock or list of stocks.

    Parameters:
    mkt_data: a dataframe containing typical price data for some tickers.

    Returns: 
    A list of floats, showing individualized sharpe ratios for the stocks.
    '''

    raise NotImplementedError
