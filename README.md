# datasci_9_data_prep
Focus on selecting datasets suitable for a machine learning experiment, with an emphasis on data cleaning, encoding, and transformation steps necessary to prepare the data.

# Dataset Selection

+ The first dataset selected from [Data.gov](https://data.gov/): [Office-based Health Care Providers Database](https://catalog.data.gov/dataset/office-based-health-care-providers-database)
  + It calculates the counts of of medical doctors, doctors of osteopathy, nurse practitioners, and physician assistants at the state and county level from 2011 through 2013.
+ The second dataset selected: [Takata Recall](https://catalog.data.gov/dataset/takata-recall)
  + It tracks various progress indicators for the recall of tens of millions of vehicles with Takata air bags. As it had been shown that long-term exposure to high heat and humidity can cause these air bags to explode when deployed. Such explosions have caused injuries and deaths.

</br>

# Data Cleaning and Transformation Plan

+ Before anything else, ensure tht Sklearn is installed with <code>pip install sklearn</code> in the terminal

</br>

### Health Care Providers Dataset 

+ Intended machine learning task: classification
  
+ This dataset was used in the <code>model_dev1</code> folder
+ In <code>model_dev1</code>, create 3 folders named <code>data</code>, <code>model</code>, and <code>scripts</code>
  + In <code>data</code>, create two more folders named <code>processed</code> and <code>raw</code>
  + In <code>scripts</code>, create three python files named <code>p1_extract.py</code>, <code>p2_transform.py</code>, and <code>p3_compute.py</code>

  + In [p1_extract.py](https://github.com/joyc3lin/datasci_9_data_prep/blob/main/model_dev1/scripts/p1_extract.py), load in the dataset and save it as both a csv file and a pickle file to the <code>raw</code> folder
  +  In [p2_transform.py](https://github.com/joyc3lin/datasci_9_data_prep/blob/main/model_dev1/scripts/p2_transform.py), load in the pickle file from the <code>raw</code> folder


**To clean data:**

+ Clean column names by removing white spaces, special characters, and making all letters lowercase
+ Check data types and change any to match what is needed
+ Check for missingness and drop rows with missing data
+ Select columns to keep and to drop based on what will be used for computing
+ Drop unneeded columns
+ Change dataframe to only keep columns

**To transform data:**

+ Perform ordinal encoding on selected columns with categorical values
+ Create a dataframe for the encoding with mapping
+ Save the mapping as a csv file in <code>processed</code>
+ Repeat the process for columns needed
+ Save a temporary csv file of the encoded dataframe to <code>processed</code>
  + All values in the new dataframe should be numerical
    
</br>

### Takata Recalls Dataset 

+ Intended machine learning task: regression
+ This dataset was used in the <code>model_dev2</code> folder
+ Repeat the same steps as for the "Health Care Providers Dataset", except everything should be done in <code>model_dev2</code>

</br>

# Dataset Splitting

*Note: this applies to both datasets*

+ In <code>p3_compute.py</code>, load in the previously processed dataframe
+ Define the independent (features) and dependent (target) variables
  + The features should be all the columns other than the target variable
+ Initalize the standard scaler and fit it to the features
+ Save the scaler as a pickle file in <code>model</code> for later use
+ Fit the scaler to the feauers and transform
+ Split the scaled data into training, validation, and testing sets
+ Pickle <code>X_train</code> and <code>X.columns</code> to <code>model</code> to save for later use

</br>

## Additional Documentation

+ No additional errors or challenges were encountered
