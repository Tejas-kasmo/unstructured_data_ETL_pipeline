import extract
import pandas  as pd
import update_meta_data as umd

def to_data_frame(data):

    structured_data = pd.DataFrame(data)
    umd.update_log(action='unstructured data converted to pandas dataframe')

    return structured_data

def clean(data):

    data['start_date'] = pd.to_datetime(data['start_date'])
    data['end_date'] = pd.to_datetime(data['end_date'])

    data['technologies'] = data['technologies'].astype(str).str.replace(r'[\[\]]','', regex=True)

    data['_id'] = data['_id'].astype(str)

    umd.update_log(action='data cleaned and transformed')

    return data
