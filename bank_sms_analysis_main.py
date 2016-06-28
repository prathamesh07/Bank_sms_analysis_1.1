import pandas as pd
from function_definitions.sms_level1_classification_func import bank_sms_filtering_func
from bank_sms_classification_script import bank_sms_attributes_generation_func

#Filtering bank sms from all sms
bank_sms_raw_df = bank_sms_filtering_func("user_sms_pipe.csv") # creates a 'bank_sms_raw.csv' file

#Creating some new attributes in dataframe
bank_sms_raw_df = bank_sms_attributes_generation_func(bank_sms_raw_df)