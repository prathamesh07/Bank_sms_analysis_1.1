import pandas as pd

def balance_rectification_func(bank_sms_df):
	#Creating bulk_transaction_flag
	bank_sms_df['BulkTxnFlag'] = 0
	#print bank_sms_df.head()


	user_account_amt2_combination_dict = {}
	prev_key = ''

	for idx, row in bank_sms_df.iterrows():
		print 7, '\t\t' , idx 
		if (row['MessageType'] in ['Debit', 'ATM']) and (row['Amt_1'] != -1) :
			bank_sms_df.at[idx, 'TxnAmount'] = -1 * float(row['Amt_1'])
		else:
			bank_sms_df.at[idx, 'TxnAmount'] = float(row['Amt_1'])
		
		
		if row['Amt_2'] != -1:
			key = str(row['CustomerID'])+str(row['BankName'])+str(row['AccountNo'])+str(row['Amt_2'])
			if key in user_account_amt2_combination_dict:
				user_account_amt2_combination_dict[key].append(idx)	
			else :
				user_account_amt2_combination_dict[key] = [idx]
				try:
					if len(user_account_amt2_combination_dict[prev_key]) == 1:
						del user_account_amt2_combination_dict[prev_key]
				except KeyError:
					pass

			prev_key = key
			
		else:
			continue
			
	#print len(user_account_amt2_combination_dict), '****************************'

	for key in user_account_amt2_combination_dict.keys() :
		print 7, '\t\t' , key 
		indexes = user_account_amt2_combination_dict[key]
			
		error_total = 0
		for idx in indexes:
			try:
				error_total += float(bank_sms_df.at[idx, 'Error'])
			except TypeError:
				#print 'TypeException'
				error_total = 1
			except ValueError:
				#print 'ValueException'
				error_total = 1
		
		if abs(error_total) < 0.001:
			for idx in indexes:
				bank_sms_df.at[idx, 'BulkTxnFlag'] = 2
		else:
			for idx in indexes:
				bank_sms_df.at[idx, 'BulkTxnFlag'] = 1
				
	bank_sms_df = bank_sms_df[['SmsID', 'CustomerID', 'BankName', 'AccountNo', 'LinkedDebitCardNumber', 'AccountType', 'MessageSource', 'Message', 'MessageTimestamp', 'ReferenceNumber', 'MessageType', 'Currency_1', 'Amt_1', 'Currency_2', 'Amt_2', 'Amt_2_calculated', 'Error', 'ConsecutiveTxnTimespan', 'Currency_3', 'Amt_3', 'Vendor', 'TxnAmount', 'RepeatedTxnFlag', 'BulkTxnFlag']]
				
	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_filtered_flaged.csv', index=False)
	bank_sms_df.index = range(len(bank_sms_df.index.values))
	return bank_sms_df