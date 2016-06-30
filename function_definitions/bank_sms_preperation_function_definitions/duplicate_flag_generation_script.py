import pandas as pd
#import function_definitions.bank_sms_preperation_function_definitions.sms_reading_script as sms_reading_script

def duplicate_flag_generation_func(bank_sms_df):
	bank_sms_df['RepeatedTxnFlag'] = 0

	temp = -1	#This variable is used to store index of last duplicate sms.
	count = 0	#To store count of total number of exceptions
	for i in range(len(bank_sms_df.index.values) -1):
		if i <= temp :
			continue

		print i 
		current_row_ref_number = bank_sms_df.at[i, 'ReferenceNumber']
		next_row_ref_number = bank_sms_df.at[i+1, 'ReferenceNumber']

		if current_row_ref_number != next_row_ref_number or current_row_ref_number == '_NA_':
			continue

		else :
			j = 0
			try :
				while bank_sms_df.at[i+j, 'ReferenceNumber'] == bank_sms_df.at[i+j+1, 'ReferenceNumber'] and  bank_sms_df.at[i+j, 'BankName'] == bank_sms_df.at[i+j+1, 'BankName']:
					j+=1 
			except :
				count += 1
				pass
				
			
			#This list holds the indexes of duplicate sms i.e sms for each user-bank-account having same reference number
			duplicate_sms_idx_list = []

			for k in range(j+1):
				duplicate_sms_idx_list.append(i + k)
			
			for idx in duplicate_sms_idx_list :
				if bank_sms_df.at[idx, 'Amt_2'] == -1 :
					bank_sms_df.at[idx,"RepeatedTxnFlag"] = 1 
				else :
					bank_sms_df.at[idx,"RepeatedTxnFlag"] = 2
					
			temp = idx 
			
			
	bank_sms_df = bank_sms_df[['SmsID', 'CustomerID', 'BankName', 'AccountNo', 'LinkedDebitCardNumber', 'AccountType', 'MessageSource', 'Message', 'MessageTimestamp', 'ReferenceNumber', 'MessageType', 'Currency_1', 'Amt_1', 'Currency_2', 'Amt_2', 'Currency_3', 'Amt_3', 'Vendor', 'RepeatedTxnFlag']]

	print 'count =', count
	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_flaged.csv',index = False)
	bank_sms_df.index = range(len(bank_sms_df.index.values))
	return bank_sms_df