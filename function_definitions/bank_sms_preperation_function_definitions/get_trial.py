from datetime import datetime
import pandas as pd
import re

from function_definitions.getters_utility import getData
from function_definitions.getters_utility import getSenderName
from function_definitions.sms_level1_classification_func import utility_sms_filtering_func
from function_definitions.getters_utility import getMessageType
from function_definitions.getters_utility import getUtilityDetails


def utility_sms_attributes_generation_func(utility_sms_df):
	for idx, row in utility_sms_df.iterrows():
		#print 1 , idx 
		
		row['Message'] = str(row['Message']).upper()
		
		extracted_data = getData(row['Message'])
		sender_name = getSenderName(row['MessageSource'])
		message_type = getMessageType(row['MessageSource'])
		utility_details = getUtilityDetails(row['MessageSource'])
		
		print extracted_data[0]
		print extracted_data[1]
		print extracted_data[2]
		print extracted_data[3]
		print extracted_data[4]
		print extracted_data[5]
		print extracted_data[6]
		print extracted_data[7]
		print extracted_data[8]
		print extracted_data[9]
