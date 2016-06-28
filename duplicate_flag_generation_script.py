import pandas as pd

bank_sms_flaged = pd.read_csv('data_files/intermediate_output_files/bank_sms_with_balance_sms_adjusted.csv', parse_dates=['MessageTimestamp'])
bank_sms_flaged['RepeatedTxnFlag'] = 0

temp = -1	#This variable is used to store index of last duplicate sms.
count = 0	#To store count of total number of exceptions
for i in range(len(bank_sms_flaged.index.values) -1):
	if i <= temp :
		continue

	print i 
	current_row = bank_sms_flaged.loc[i]
	next_row = bank_sms_flaged.loc[i+1]

	if current_row['ReferenceNumber'] != next_row['ReferenceNumber'] or current_row['ReferenceNumber'] == '_NA_':
		continue

	else :
		j = 0
		try :
			while bank_sms_flaged.loc[i+j]['ReferenceNumber'] == bank_sms_flaged.loc[i+j+1]['ReferenceNumber'] and  bank_sms_flaged.loc[i+j]['BankName'] == bank_sms_flaged.loc[i+j+1]['BankName']:
				j+=1 
		except :
			count += 1
			pass
			
		
		#This list holds the indexes of duplicate sms i.e sms for each user-bank-account having same reference number
		duplicate_sms_idx_list = []

		for k in range(j+1):
			duplicate_sms_idx_list.append(i + k)
		
		for idx in duplicate_sms_idx_list :
			if bank_sms_flaged.loc[idx]['Amt_2'] == -1 :
				bank_sms_flaged.loc[idx,"RepeatedTxnFlag"] = 1 
			else :
				bank_sms_flaged.loc[idx,"RepeatedTxnFlag"] = 2
				
		temp = idx 
		
		
bank_sms_flaged = bank_sms_flaged[['SmsID', 'CustomerID', 'BankName', 'AccountNo', 'LinkedDebitCardNumber', 'AccountType', 'MessageSource', 'Message', 'MessageTimestamp', 'ReferenceNumber', 'MessageType', 'Currency_1', 'Amt_1', 'Currency_2', 'Amt_2', 'Currency_3', 'Amt_3', 'Currency_3', 'Vendor', 'RepeatedTxnFlag']]

print 'count =', count
bank_sms_flaged.to_csv('data_files/intermediate_output_files/bank_sms_flaged.csv',index = False)