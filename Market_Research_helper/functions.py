from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm
import pandas as pd
import numpy as np


from Market_Research_helper.config import PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def get_return_Ndays(
    df: pd.DataFrame,
    days: int, # Days over which to compute return
    log: bool = False, # Whether log return should be computed or not
):
    logger.info(f"Computing{' log ' if log else ' '}return over {days}")


    if not log:
        Return = df["Close"].pct_change(days)
        colname = f'RTN_D{days}'
    else:
        Return = np.log(df["Close"]).diff(days)
        colname = f'LOGRTN_D{days}'
        
    Return.dropna(inplace=True)
        
    Return.rename(colname, inplace=True)
    

    return Return


if __name__ == "__main__":
    app()
