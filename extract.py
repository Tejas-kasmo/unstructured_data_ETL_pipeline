import pymongo as pm
import update_meta_data as umd

def get_data():

    client = pm.MongoClient(r'mongodb://localhost:27017/')

    db = client["practice_data"]
    collection = db["project"]

    data = list(collection.find())

    umd.update_log(action='data extracted', source='mongodb_data_base')

    return data
