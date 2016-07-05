from datetime import datetime
import pandas as pd
import re

from function_definitions.getters import getData
from function_definitions.getters import getBankName
from function_definitions.getters import getBankDetails
from function_definitions.sms_level1_classification_func import bank_sms_filtering_func

message_id_re = re.compile(r'\w+-\w+')



def bank_sms_attributes_generation_func(bank_sms_df):
	for idx, row in bank_sms_df.iterrows():
		print 1 , idx
		
		try :	
			try:
				CustomerID = int(row['CustomerID'])
			except Exception as e:
				raise type(e)(e.message + " >>> " + 'Found for CustomerID ' + str(row['CustomerID']))

			try:
				SmsID = int(row['SmsID'])
			except Exception as e:
				raise type(e)(e.message + " >>> " + 'Found for CustomerID ' + str(row['CustomerID']) + ' at SmsID ' + str(row['SmsID']))


			try:
				row['Message'] = str(row['Message']).upper()
			except Exception as e:
				raise type(e)(e.message + " >>> " + 'Found for CustomerID ' + str(row['CustomerID']) + ' at row having SmsID '+str(row['SmsID'])+' and column "Message"')
			

			try:
				bank_sms_df.at[idx,"MessageTimestamp"] = datetime.fromtimestamp(row['MessageDate']/1000)
			except Exception as e:
				raise type(e)(e.message + " >>> " + 'Found for CustomerID ' + str(row['CustomerID']) + ' at row having SmsID '+str(row['SmsID'])+' and column "MessageDate"')


			if re.search(message_id_re,row['MessageSource']):
				pass 
			else :
				raise Exception("MessageSource ID was not having format xx-xxx... for CustomerID "  + str(row['CustomerID']) +  ' at row having SmsID '+str(row['SmsID']))

		except Exception  as e:
			print e 
			continue 




		extracted_data = getData(row['Message'])
		bank_name = getBankName(row['MessageSource'])
		bank_details = getBankDetails(row['MessageSource'])	



		bank_sms_df.at[idx,"MessageType"] = extracted_data[0]

		bank_sms_df.at[idx,"Currency_1"] = extracted_data[1]
		bank_sms_df.at[idx,"Amt_1"] = extracted_data[2]
		
		bank_sms_df.at[idx,"Currency_2"] = extracted_data[3]
		bank_sms_df.at[idx,"Amt_2"] = extracted_data[4]
		
		bank_sms_df.at[idx,"Currency_3"] = extracted_data[5]
		bank_sms_df.at[idx,"Amt_3"] = extracted_data[6]
		
		bank_sms_df.at[idx,"Vendor"] = extracted_data[8]
		bank_sms_df.at[idx,"AccountNo"] = extracted_data[7]
		bank_sms_df.at[idx,"AccountType"] = extracted_data[9]
		bank_sms_df.at[idx,"ReferenceNumber"] = extracted_data[10]
		bank_sms_df.at[idx, "TxnInstrument"] = extracted_data[11]

		#bank_sms_df.at[idx,"BankName"] = bank_name
		bank_sms_df.at[idx,"BankName"] = bank_details[0]
		bank_sms_df.at[idx,"SENDER_PARENT"] = bank_details[1]
		bank_sms_df.at[idx,"SENDER_CHILD_1"] = bank_details[2]
		bank_sms_df.at[idx,"SENDER_CHILD_2"] = bank_details[3]
		bank_sms_df.at[idx,"SENDER_CHILD_3"] = bank_details[4]

	bank_sms_df = bank_sms_df.sort_values(by=["CustomerID", "AccountNo", "MessageTimestamp"], ascending=[True, True, True])

	#Storing none type sms type to a another csv as non-classified
	non_classified_sms = bank_sms_df[bank_sms_df['MessageType'] == 'None']
	non_classified_sms = non_classified_sms[['SmsID', 'CustomerID', 'Message', 'MessageSource', 'MessageDate']]
	non_classified_sms.to_csv('data_files/Non_classified/non_classified_sms.csv', index=False)

	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_classified.csv',index = False)
	bank_sms_df.index = range(len(bank_sms_df.index.values))
	return bank_sms_df