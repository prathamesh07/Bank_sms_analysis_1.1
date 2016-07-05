from datetime import datetime
import pandas as pd
import re

from function_definitions.getters_utility import getData
from function_definitions.getters_utility import getSenderName
from function_definitions.sms_level1_classification_func import utility_sms_filtering_func

def utility_sms_attributes_generation_func(utility_sms_df):
	for idx, row in utility_sms_df.iterrows():
		#print 1 , idx 
		
		row['Message'] = str(row['Message']).upper()
		
		extracted_data = getData(row['Message'])
		sender_name = getSenderName(row['MessageSource'])
		#bank_details = getBankDetails(row['MessageSource'])
		try:
			utility_sms_df.at[idx,"MessageTimestamp"] = datetime.fromtimestamp(row['MessageDate']/1000)
		except:
			pass 

		utility_sms_df.at[idx,"MessageType"] = extracted_data[0]
	
		utility_sms_df.at[idx,"Currency_1"] = extracted_data[1]
		utility_sms_df.at[idx,"Amt_1"] = extracted_data[2]
		
		utility_sms_df.at[idx,"Currency_2"] = extracted_data[3]
		utility_sms_df.at[idx,"Amt_2"] = extracted_data[4]
		
		utility_sms_df.at[idx,"Currency_3"] = extracted_data[5]
		utility_sms_df.at[idx,"Amt_3"] = extracted_data[6]
		
		#utility_sms_df.at[idx,"Vendor"] = extracted_data[8]
		#utility_sms_df.at[idx,"AccountNo"] = extracted_data[7]
		#utility_sms_df.at[idx,"AccountType"] = extracted_data[9]
		utility_sms_df.at[idx,"ReferenceNumber"] = extracted_data[7]
		#utility_sms_df.at[idx, "TxnInstrument"] = extracted_data[11]

		#bank_sms_df.at[idx,"BankName"] = bank_name
		'''bank_sms_df.at[idx,"BankName"] = bank_details[0]
		bank_sms_df.at[idx,"SENDER_PARENT"] = bank_details[1]
		bank_sms_df.at[idx,"SENDER_CHILD_1"] = bank_details[2]
		bank_sms_df.at[idx,"SENDER_CHILD_2"] = bank_details[3]
		bank_sms_df.at[idx,"SENDER_CHILD_3"] = bank_details[4]'''

	utility_sms_df = utility_sms_df.sort_values(by=["CustomerID", "MessageTimestamp"], ascending=[True, True])

	utility_sms_df.to_csv('data_files/intermediate_output_files/utility/utility_sms_classified.csv',index = False)
	utility_sms_df.index = range(len(utility_sms_df.index.values))
	return utility_sms_df