import pandas as pd 

## get data 

# data download link: 
datalink = 'https://www.healthit.gov/sites/default/files/data/datasets/SKA_State_County_Data_2011-2013.csv'

df = pd.read_csv(datalink)
df.size
df.sample(5)


## save as csv to model_dev1/data/raw/
df.to_csv('model_dev1/data/raw/health_providers.csv', index=False)

## save as pickle to model_dev1/data/raw/
df.to_pickle('model_dev1/data/raw/health_providers.pkl')

