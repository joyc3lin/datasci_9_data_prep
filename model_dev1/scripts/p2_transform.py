import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## get data raw
df = pd.read_pickle('model_dev1/data/raw/health_providers.pkl')

## get column names
df.columns

## do some data cleaning of column names, 
## make them all lower case, replmove white spaces and replace with _ 
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.columns

## get data types
df.dtypes # nice combination of numbers and strings/objects 
df.shape

## drop columns
to_drop = [
    'region_code',
    'state_fips',
    'county_fips',
    'fips'
]
df.drop(to_drop, axis=1, inplace=True, errors='ignore')

# keep columns 
to_keep = [
    'region',
    'period',
    'all_providers',
    'all_primary_care_providers',
    'all_physicians',
    'all_primary_care_physicians',
    'all_nurse_practitioners',
    'all_primary_care_nurse_practitioners'
]

# changing dataframe to only to keep columns 
df = df[to_keep]

## looking for missing data 
df.isnull().sum()




## perform ordinal encoding on region
enc = OrdinalEncoder()
enc.fit(df[['region']])
df['region'] = enc.transform(df[['region']])
df['region']

## create dataframe with mapping
df_mapping_region = pd.DataFrame(enc.categories_[0], columns=['region'])
df_mapping_region['region_ordinal'] = df_mapping_region.index
df_mapping_region

## save mapping to csv
df_mapping_region.to_csv('model_dev1/data/processed/mapping_region.csv', index=False)




## period --> will need to encode this
df.period.value_counts()

## perform orindla encoding on area_name
enc = OrdinalEncoder()
enc.fit(df[['period']])
df['period'] = enc.transform(df[['period']])

## create dataframe with mapping
df_mapping_period = pd.DataFrame(enc.categories_[0], columns=['period'])
df_mapping_period['period_ordinal'] = df_mapping_period.index
df_mapping_period

# save mapping to csv
df_mapping_period.to_csv('model_dev1/data/processed/mapping_period.csv', index=False)

len(df)

#### save a temporary csv file of 1000 rows to test the model
df.to_csv('model_dev1/data/processed/health_providers_processed.csv', index=False)