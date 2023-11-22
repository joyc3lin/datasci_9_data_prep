import pandas as pd 
import re
from sklearn.preprocessing import OrdinalEncoder

## get data raw
df = pd.read_pickle('model_dev2/data/raw/takata.pkl')

## get column names
df.columns

## do some data cleaning of column names
def clean_value(value):
    cleaned_value = re.sub(r'\s+|[^a-zA-Z0-9]', '', str(value))
    return cleaned_value

df.rename(mapper=clean_value, axis=1, inplace=True)
df.columns

df.columns = df.columns.str.lower()


## get data types
df.dtypes # nice combination of numbers and strings/objects 
df.shape

## drop columns
to_drop = [
    'reportdate',
    'prioritygroup',
    'driverpassenger',
    'other',
    'affirmativerefusal',
    'aftermarketmodification',
    'aftermarketmodification',
    'netairbagsaffected',
    'netairbagsremaining',
    'completionrate'
]
df.drop(to_drop, axis=1, inplace=True, errors='ignore')

# keep columns 
to_keep = [
    'manufacturer',
    'recallcampaign',
    'totalairbagsaffected',
    'totalairbagsrepaired',
    'scrapped',
    'exported',
    'stolen',
    'nonresponsive',

]

# changing dataframe to only to keep columns 
df = df[to_keep]

## looking for missing data 
df.isnull().sum()



## perform ordinal encoding on manufacturer
enc = OrdinalEncoder()
enc.fit(df[['manufacturer']])
df['manufacturer'] = enc.transform(df[['manufacturer']])
df['manufacturer']

## create dataframe with mapping
df_mapping_manufacturer = pd.DataFrame(enc.categories_[0], columns=['manufacturer'])
df_mapping_manufacturer['manufacturer_ordinal'] = df_mapping_manufacturer.index
df_mapping_manufacturer

## save mapping to csv
df_mapping_manufacturer.to_csv('model_dev2/data/processed/mapping_manufacturer.csv', index=False)




## period --> will need to encode this
df.recallcampaign.value_counts()

## perform orindla encoding on recallcampaign
enc = OrdinalEncoder()
enc.fit(df[['recallcampaign']])
df['recallcampaign'] = enc.transform(df[['recallcampaign']])

## create dataframe with mapping
df_mapping_recallcampaign = pd.DataFrame(enc.categories_[0], columns=['recallcampaign'])
df_mapping_recallcampaign['recallcampaign_ordinal'] = df_mapping_recallcampaign.index
df_mapping_recallcampaign

# save mapping to csv
df_mapping_recallcampaign.to_csv('model_dev2/data/processed/mapping_recallcampaign.csv', index=False)

len(df)

#### save a temporary csv file of 1000 rows to test the model
df.to_csv('model_dev2/data/processed/takata_processed.csv', index=False)