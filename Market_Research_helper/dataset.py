from pathlib import Path

import typer
from tqdm import tqdm
from loguru import logger
import datetime as dt
import yfinance as yf
import pandas as pd
from Market_Research_helper.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def get_stock_dataset(
    stock: str,
    end_date: list,
    days: int,
    WholeData: bool=False,
):
    if WholeData:
        end = dt.datetime(*end_date)
        start = end - dt.timedelta(days=36500)
    else:    
        end = dt.datetime(*end_date)
        start = end - dt.timedelta(days=days)
    logger.info(f"Loading {stock} data from {start} to {end_date}.")
    df = yf.download(stock, start=start, end=end).stack(future_stack=True)
    logger.success(f"Success loading {stock} data.") 
    df = df.xs(stock, level=1)
 
    return df 


if __name__ == "__main__":
    app()
