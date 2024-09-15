import numpy as np
import pandas as pd
def GPS_Keypoints_Extracter(GPSdata,indexdata,new_file_name):
    GPS_dataset =pd.read_csv(GPSdata,index_col="cts")
    index_dataset=pd.read_csv(indexdata)
    index_dataset.insert(loc=1, column='lat',value='null1') 
    index_dataset.insert(loc=2,column='long',value='null')
    i = 0
    for index in index_dataset['index']:
        index_dataset['lat'][i] =GPS_dataset.loc[index][0]
        i=i+1
    i = 0
    for index in index_dataset['index']:
        index_dataset['lng'][i] =GPS_dataset.loc[index][1]
        i=i + 1
    print(index_dataset)
    index_dataset = index_dataset.drop('index',axis=1)
    index_dataset.to_csv(new_file_name,index=False)
j = 1

while j <= 14:
    gps = ''