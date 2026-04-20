'''
The kernel of generation of data (Polars + Numpy & DL)
'''
import polars as pl
import numpy as np
from random import shuffle
# import pytorch as PT <- Install this shit later


def generate_data(params: dict) -> pl.DataFrame:
    '''
    Generating data without fraud transactions.
    '''

    return normal_data

def generate_fraud_data(params: dict) -> pl.DataFrame:
    '''
    Fraud data generation function. There are 3 params that can help to recognise fraud data:
    - a lot of small transactions in a short period of time
    - unusual time of transaction (between certain hours, e.g. 12:00 pm - 06:00 am)
    - a huge amount transactioned in once
    '''

    return fraud

def united_data(normal_data: pl.DataFrame, fraud_data: pl.DataFrame) -> pl.DataFrame: #combining normal data with fraud data
    return shuffle(normal_data + fraud_data)

