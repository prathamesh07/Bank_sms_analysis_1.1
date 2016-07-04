import pandas as pd
from time import time 
from function_definitions.sms_level1_classification_func import utility_sms_filtering_func


ti = time()*1000 

#Filtering utility sms from all sms
utility_sms_df = utility_sms_filtering_func("user_sms_pipe.csv") # creates a 'utility_sms_raw.csv' file

tf = time()*1000

print 'THE END',(tf-ti)