import pandas as pd
import configparser as cp
from sqlalchemy import create_engine
import urllib
import update_meta_data as umd

def connect(data, Table_name):

    config = cp.ConfigParser()
    config.read(r'C:\Users\mysur\OneDrive\Desktop\python_tutorial\venv1\config.config')

    DRIVER = config['ssms']['DRIVER']
    SERVER = config['ssms']['SERVER']
    DATABASE = config['ssms']['DATABASE']
    UID = config['ssms']['UID']
    PWD = config['ssms']['PWD']

    connection_string = (
        f'DRIVER={DRIVER};'
        f'SERVER={SERVER};'
        f'DATABASE={DATABASE};'
        f'UID={UID};'
        f'PWD={PWD}'
    )

    params = urllib.parse.quote_plus(connection_string)

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

    data.to_sql(
        name=Table_name,
        con=engine,
        index=False,
        if_exists='replace'
    )

    umd.update_log(action='data loaded' , destination='ssms database')

