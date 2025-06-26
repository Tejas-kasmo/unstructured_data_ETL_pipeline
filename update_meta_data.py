import pandas as pd
import datetime

def update_log(date_time=None, action:str = None, source:str = None, destination:str = None):

    meta_data = pd.read_csv(r"C:\Users\mysur\OneDrive\Desktop\python_tutorial\data\meta_data.csv")

    if date_time is None:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        date_time = pd.to_datetime(date)

    df = {'date_time':date_time,
          'action': action,
          'source': source,
          'destination':destination}
    
    meta_data = pd.concat([meta_data,
                           pd.DataFrame([df])], 
                           ignore_index=True)
    
    meta_data.to_csv(r"C:\Users\mysur\OneDrive\Desktop\python_tutorial\data\meta_data.csv", index=False)

def get_meta_data():

    meta_data = pd.read_csv(r"C:\Users\mysur\OneDrive\Desktop\python_tutorial\data\meta_data.csv")

    return meta_data
