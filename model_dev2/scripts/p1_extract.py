import pandas as pd 

## get data 

# data download link: 
datalink = 'https://data.transportation.gov/api/views/8u28-hw9f/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size


## save as csv to model_dev1/data/raw/
df.to_csv('model_dev2/data/raw/takata.csv', index=False)

## save as pickle to model_dev1/data/raw/
df.to_pickle('model_dev2/data/raw/takata.pkl')

