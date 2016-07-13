from datetime import datetime, timedelta
import pandas as pd


"""
This script adjusts first balance sms of each day as first sms of that day by truncating time part to 00-00-00.
So that this sms can be used to compute opening balance. Also, there is entry of same sms but with prev day date
and time 23-59-59. So that we can compute prev day's closing balance.
"""

def balance_sms_adjustment_func(bank_sms_df):
	bank_sms_df_original = bank_sms_df
	bank_sms_df = bank_sms_df[bank_sms_df['MessageType'] == 'Balance']
	
	#Truncating time part of datetime to 00:00:00
	bank_sms_df['MessageTimestamp'] = bank_sms_df['MessageTimestamp'].apply(pd.datetools.normalize_date)
	#print len(bank_sms_df.index.values)

	#Considering only first balance sms from each day
	bank_sms_df.drop_duplicates(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)
	#print len(bank_sms_df.index.values)


	for idx, row in bank_sms_df.iterrows():
		print 4 , '\t\t' , idx
		SmsID = row['SmsID']
		CustomerID = row['CustomerID']
		Message = row["Message"]
		MessageSource = row["MessageSource"]
		MessageDate = row["MessageDate"]
		MessageTimestamp = row["MessageTimestamp"]
		MessageType = row["MessageType"]
		Currency_1 = row["Currency_1"]
		Amt_1 = row["Amt_1"]
		Currency_2 = row["Currency_2"]
		Amt_2 = row["Amt_2"]
		Currency_3 = row["Currency_3"]
		Amt_3 = row["Amt_3"]
		Vendor = row["Vendor"]
		AccountNo = row["AccountNo"]
		AccountType = row["AccountType"]
		ReferenceNumber = row["ReferenceNumber"]
		TxnInstrument = '_NA_'
		BankName = row["BankName"]
		SENDER_PARENT = row['SENDER_PARENT']
		SENDER_CHILD_1 = row['SENDER_CHILD_1']
		SENDER_CHILD_2 = row['SENDER_CHILD_2']
		SENDER_CHILD_3 = row['SENDER_CHILD_3']
		LinkedDebitCardNumber = row['LinkedDebitCardNumber']

		timestamp_for_new_row = MessageTimestamp - timedelta(seconds=1)
		
		to_be_appended = pd.DataFrame({'SmsID':SmsID, 'CustomerID':CustomerID, 'Message':pd.Series(Message), 'MessageSource':pd.Series(MessageSource), 'MessageDate':pd.Series(MessageDate), \
		'MessageTimestamp':timestamp_for_new_row, 'MessageType':pd.Series(MessageType), 'Currency_1':pd.Series(Currency_1), 'Amt_1':Amt_1, 'Currency_2':pd.Series(Currency_2), 'Amt_2':Amt_2, 'Currency_3':pd.Series(Currency_3), \
		'Amt_3':Amt_3, 'Vendor':pd.Series(Vendor), 'AccountNo':pd.Series(AccountNo), 'AccountType':pd.Series(AccountType), 'ReferenceNumber':pd.Series(ReferenceNumber), 'TxnInstrument':TxnInstrument, 'BankName':pd.Series(BankName), 'SENDER_PARENT':pd.Series(SENDER_PARENT), 'SENDER_CHILD_1':pd.Series(SENDER_CHILD_1), 'SENDER_CHILD_2':pd.Series(SENDER_CHILD_2), 'SENDER_CHILD_3':pd.Series(SENDER_CHILD_3), 'LinkedDebitCardNumber':pd.Series(LinkedDebitCardNumber)})
		
		bank_sms_df = bank_sms_df.append(to_be_appended)

	bank_sms_df.sort_values(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)	

	#print len(bank_sms_df.index.values)

	#Reading orginal dataframe again and dropping balance sms rows
	bank_sms_df_without_balance = bank_sms_df_original[bank_sms_df_original['MessageType'] != 'Balance']

	#Appending adjusted balance sms dates dataframe to orginal dataframe
	bank_sms_df = bank_sms_df.append(bank_sms_df_without_balance)

	#Sorting according to 'CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'
	bank_sms_df.sort_values(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)

	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_with_balance_sms_adjusted.csv', index=False)
	bank_sms_df.index = range(len(bank_sms_df.index.values))
	return bank_sms_df