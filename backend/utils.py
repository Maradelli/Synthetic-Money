'''
Different support functions for conversion, logging, etc.
'''
import logging
import xlsxwriter
import pyarrow as pa
import pyarrow.parquet as pq
import io 
import polars as pl
import streamlit as st
import uuid
import numpy as np

def message(message: str, level: str = 'INFO'): #logging function
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    if level == 'INFO':
        logging.info(message)
    elif level == 'WARNING':
        logging.warning(message)
    elif level == 'ERROR':
        logging.error(message)

def save_to_xlsx(data : pl.DataFrame, str : str = 'XLSX') -> str:
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet()

    #writing data to the file - need to work on it
    for i in range(data.shape[0]):
        worksheet.write('')

    workbook.close()
    return 'Data was saved in \'xlsx\' format!'


def save_to_csv(data : pl.DataFrame, str : str = 'CSV') -> str:
    return 'Data was saved in \'CSV\' format!'


def save_to_parquet(data : pl.DataFrame, str : str = 'PARQUET') -> str:
    #schema needs to be added
    table = pa.Table.from_pandas(data, schema=schema, preserve_index = False)
    pq.write_table(table, 'results.parquet')
    return 'Data was saved in \'parquet\' format!'


def generate_uuid() -> str: #for generating unique ids for clients
    return str(uuid.uuid4())

def log_normal_distribution(mu: float, sigma: float, size: int) -> np.ndarray: #log-normal distribution
    return np.random.lognormal(mean=mu, sigma=sigma, size=size)