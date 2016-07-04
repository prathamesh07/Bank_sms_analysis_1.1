import pandas as pd
from datetime import datetime, timedelta

def balance_error_based_dummy_entry_generation_func(bank_sms_df):

	#Creating empty dataframe to store dummy sms
	#dummy_sms = pd.DataFrame()
	dummy_sms_df = pd.DataFrame()
	for idx, row in bank_sms_df.iterrows():
		print 8 , '\t\t' ,  idx
		if idx == 0 or row['Error'] == '_NA_' or str(row['Error']) == '0':
			continue
		else:
			#Storing row attributes in variables so that we can use them to fill dummy entry
			SmsID = -1*int(row['SmsID'])
			CustomerID = row['CustomerID']
			BankName = row['BankName']
			AccountNo = row['AccountNo']
			LinkedDebitCardNumber = row['LinkedDebitCardNumber']
			AccountType = row['AccountType']
			MessageSource = row['MessageSource']
			ReferenceNumber = '_NA_'
			MessageType = 'Credit' if float(row['Error']) >=0 else 'Debit'
			Currency_1 = row['Currency_1']
			Amt_1 = abs(float(row['Error']))
			Message = 'Dummy entry of '+Currency_1+str(Amt_1)+' is added.'
			Currency_2 = row['Currency_2']
			Amt_2 = float(row['Error']) + float(bank_sms_df.at[idx-1, 'Amt_2'])
			Amt_2_calculated = Amt_2
			Error = 0
			ConsecutiveTxnTimespan = '_NA_'
			Currency_3 = '-'
			Amt_3 = -1
			Vendor = '_NA_'
			TxnAmount = Amt_1
			RepeatedTxnFlag = 0
			BulkTxnFlag = 0
			
			current_date = row['MessageTimestamp']
			prev_date = bank_sms_df.at[idx-1, 'MessageTimestamp']
			date_difference = (current_date-prev_date).days
			
			if date_difference > 1:
				dummy_entry_datetime = current_date - timedelta(1)
			else:
				dummy_entry_datetime = (current_date - prev_date)/2 + prev_date
				
			to_be_appended = pd.DataFrame({'SmsID':SmsID, 'CustomerID':CustomerID, 'BankName':pd.Series(BankName), 'AccountNo':AccountNo, 'LinkedDebitCardNumber':pd.Series(LinkedDebitCardNumber), \
			'AccountType':pd.Series(AccountType), 'MessageSource':pd.Series(MessageSource), 'Message':pd.Series(Message), 'MessageTimestamp':dummy_entry_datetime, 'ReferenceNumber':pd.Series(ReferenceNumber), \
			'MessageType':pd.Series(MessageType), 'Currency_1':pd.Series(Currency_1), 'Amt_1':Amt_1, 'Currency_2':pd.Series(Currency_2), 'Amt_2_calculated':Amt_2_calculated, 'Error':Error, \
			'ConsecutiveTxnTimespan':pd.Series(ConsecutiveTxnTimespan), 'Currency_3':pd.Series(Currency_3), 'Amt_3':Amt_3, 'Vendor':pd.Series(Vendor), 'TxnAmount':TxnAmount, \
			'RepeatedTxnFlag':RepeatedTxnFlag, 'BulkTxnFlag':BulkTxnFlag})
			
			#Appending dummy sms to main dataframe
			bank_sms_df = bank_sms_df.append(to_be_appended)
			
			#making a seperate df of dummy entries
			dummy_sms_df = dummy_sms_df.append(to_be_appended)
	
	#Sorting the dataframe
	bank_sms_df.sort_values(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)
	
	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_with_dummy_entries.csv', index=False)
	bank_sms_df.index = range(len(bank_sms_df.index.values))
	
	dummy_sms_df.to_csv('data_files/intermediate_output_files/banks/only_dummy_entries.csv', index=False)
	
	return bank_sms_df
	
	
#df = pd.read_csv('D:/Prathamesh/sms_data_analytics/chinmesh_data/Bank_sms_analysis_1.1/data_files/intermediate_output_files/banks/bank_sms_filtered_flaged.csv', parse_dates=['MessageTimestamp'])			
#balance_error_based_dummy_entry_generation_func(df)