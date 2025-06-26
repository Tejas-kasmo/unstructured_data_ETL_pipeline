import extract
import transformation
import load
import pymongo
import update_meta_data as umd

print("extaracting data...")
data = extract.get_data()
print("data extracted.")

print("transforming and  cleaning Data...")
data = transformation.to_data_frame(data)
data = transformation.clean(data)
print("transformation and cleaning done.")

print("loading data to ssms...")
load.connect(data=data, Table_name='project')
print("loaded to ssms.")

print('loading log table to ssms database....')
meta_data = umd.get_meta_data()
load.connect(data=meta_data, Table_name='log_table')
print('log table loaded to ssms database')
