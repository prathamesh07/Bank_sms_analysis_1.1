from function_definitions.sms_level1_classification_func import bank_sms_filtering_func
import pandas as pd

"""
This script reads all the sms in a dataframe and filters out only bank sms.
"""

#Filtering bank sms from all sms
bank_sms_df = bank_sms_filtering_func("user_sms_pipe.csv") # creates a 'bank_sms_raw.csv' file