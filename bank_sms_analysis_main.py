import pandas as pd
from time import time 

from function_definitions.sms_level1_classification_func import bank_sms_filtering_func
from function_definitions.bank_sms_preperation_function_definitions.bank_sms_attributes_generation_script import bank_sms_attributes_generation_func
from function_definitions.bank_sms_preperation_function_definitions.classified_vs_nonclassified_tally_generation_script import classified_vs_nonclassified_tally_generation_func
from function_definitions.bank_sms_preperation_function_definitions.account_type_rectification_script import account_type_rectification_func
from function_definitions.bank_sms_preperation_function_definitions.casa_to_debit_card_mapping_script import casa_to_debit_card_mapping_func
from function_definitions.bank_sms_preperation_function_definitions.balance_sms_adjustment_script import balance_sms_adjustment_func
from function_definitions.bank_sms_preperation_function_definitions.duplicate_flag_generation_script import duplicate_flag_generation_func
from function_definitions.bank_sms_preperation_function_definitions.bank_sms_error_tally_generation_script import bank_sms_error_tally_generation_func
from function_definitions.bank_sms_preperation_function_definitions.balance_rectification_script import balance_rectification_func
from function_definitions.bank_sms_preperation_function_definitions.balance_error_based_dummy_entry_generation_script import balance_error_based_dummy_entry_generation_func
from function_definitions.bank_sms_preperation_function_definitions.parameter_calculation_script import parameter_calculation_func
from function_definitions.bank_sms_preperation_function_definitions.post_parameter_calculation_processing_script import post_parameter_calculation_func


ti = time()*1000 

#Filtering bank sms from all sms
bank_sms_df = bank_sms_filtering_func("user_sms_pipe.csv") # creates a 'bank_sms_raw.csv' file
#Storing none type sms type to a another csv



#Creating some new attributes in dataframe
bank_sms_df = bank_sms_attributes_generation_func(bank_sms_df)


#Creating data classified vs nonclassified tally
classified_vs_nonclassified_tally_generation_func(bank_sms_df)

#Rectifying the account type tag for each sms
bank_sms_df = account_type_rectification_func(bank_sms_df)

#Mapping of CASA account to its linked debit card
bank_sms_df = casa_to_debit_card_mapping_func(bank_sms_df)

#Adjusting balance sms so that we can consider them to calculate daily opening and closing balance
bank_sms_df = balance_sms_adjustment_func(bank_sms_df)

#Generating duplicate transaction flag
bank_sms_df = duplicate_flag_generation_func(bank_sms_df)

#Calculating error tally between consecutive transactions
bank_sms_df = bank_sms_error_tally_generation_func(bank_sms_df)

#Identifying bulk transactions and rectifying balance for those transactions
bank_sms_df = balance_rectification_func(bank_sms_df)

#Generating dummy sms entries based on balance error so as to compensate error.
bank_sms_df = balance_error_based_dummy_entry_generation_func(bank_sms_df)

#Calculating some CASA parameters 
casa_parameter_data = parameter_calculation_func(bank_sms_df,'CASA')

#Calculating rest of the CASA parameters
casa_parameter_data = post_parameter_calculation_func(casa_parameter_data,'CASA')



#Calculating some Credit_Card parameters 
casa_parameter_data = parameter_calculation_func(bank_sms_df,'Credit_Card')

#Calculating rest of the Credit_Card parameters
casa_parameter_data = post_parameter_calculation_func(casa_parameter_data,'Credit_Card')




tf = time()*1000

print 'THE END',(tf-ti)