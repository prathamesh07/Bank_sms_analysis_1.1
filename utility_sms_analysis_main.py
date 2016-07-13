import pandas as pd
from time import time 
from function_definitions.sms_level1_classification_func import utility_sms_filtering_func
from function_definitions.bank_sms_preperation_function_definitions.utility_sms_attributes_generation_script import utility_sms_attributes_generation_func


ti = time()*1000 

#Filtering utility sms from all sms
utility_sms_df = utility_sms_filtering_func("user_sms_pipe.csv") # creates a 'bank_sms_raw.csv' file

#further classification
utility_sms_df = utility_sms_attributes_generation_func(utility_sms_df)

tf = time()*1000

print 'THE END',(tf-ti)