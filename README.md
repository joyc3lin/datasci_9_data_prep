# datasci_9_data_prep
Focus on selecting datasets suitable for a machine learning experiment, with an emphasis on data cleaning, encoding, and transformation steps necessary to prepare the data.

# Dataset Selection

+ The first dataset selected from [Data.gov](https://data.gov/): [Office-based Health Care Providers Database](https://catalog.data.gov/dataset/office-based-health-care-providers-database)
  + It calculates the counts of of medical doctors, doctors of osteopathy, nurse practitioners, and physician assistants at the state and county level from 2011 through 2013.
+ The second dataset selected: [Takata Recall](https://catalog.data.gov/dataset/takata-recall)
  + It tracks various progress indicators for the recall of tens of millions of vehicles with Takata air bags. As it had been shown that long-term exposure to high heat and humidity can cause these air bags to explode when deployed. Such explosions have caused injuries and deaths.

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
    +  Clean column names by removing white spaces, special characters, and making all letters lowercase
    +  check data types and change any to match what is needed
    +  Check for missingness and drop rows with missing data
    +  Select columns to keep and to drop based on what will be used for computing
    +  Drop unneeded columns
    +  Change dataframe to only keep columns
    +  

### Takata Recalls Dataset 

+ Intended machine learning task: regression
+ This dataset was used in the <code>model_dev2</code> folder
+ create all folders and pyth0n files 
+ pip install sklearn
+ pip install xgboost

# Dataset Splitting

+ Document each step of your process. Include screenshots of any errors encountered and how you resolved them.
+ Explain your decisions during the data cleaning and transformation process.
