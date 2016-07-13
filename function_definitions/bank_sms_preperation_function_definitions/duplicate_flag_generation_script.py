import pandas as pd

"""
This script generates RepeatedTxnFlag column which indicates duplicate sms based on txn reference number.
If txn is uniuque -> flag 0
If txn is duplicate but balance (Amt_2) is not given by bank -> flag 1
If txn is duplicate but balance (Amt_2) is given by bank -> flag 2
"""


def duplicate_flag_generation_func(bank_sms_df):

	#Creating RepeatedTxnFlag column and initializing with zero.
	bank_sms_df['RepeatedTxnFlag'] = 0

	temp = -1	#This variable is used to store index of last duplicate sms.
	count = 0	#To store count of total number of exceptions
	for i in range(len(bank_sms_df.index.values) -1):
		print 5 , "\t\t", i 
		
		if i <= temp :
			continue

		
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
			
			flag = 0
			for idx in duplicate_sms_idx_list :
				if abs(float(bank_sms_df.at[idx, 'Amt_2']) + 1) < 0.001 : #float(bank_sms_df.at[idx, 'Amt_2']) == -1
					bank_sms_df.at[idx,"RepeatedTxnFlag"] = 1 
				elif flag == 0 :
					bank_sms_df.at[idx,"RepeatedTxnFlag"] = 2
					flag = 1
				else :
					bank_sms_df.at[idx,"RepeatedTxnFlag"] = 1 
			temp = idx 
			
			
	bank_sms_df = bank_sms_df[['SmsID', 'CustomerID', 'BankName', 'SENDER_PARENT' , 'SENDER_CHILD_1' , 'SENDER_CHILD_2' , 'SENDER_CHILD_3' ,'AccountNo', 'LinkedDebitCardNumber', 'AccountType', 'MessageSource', 'Message', 'MessageTimestamp', 'ReferenceNumber', 'TxnInstrument', 'MessageType', 'Currency_1', 'Amt_1', 'Currency_2', 'Amt_2', 'Currency_3', 'Amt_3', 'Vendor', 'RepeatedTxnFlag']]

	#print 'count =', count
	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_flaged.csv',index = False)
	bank_sms_df.index = range(len(bank_sms_df.index.values))
	return bank_sms_df