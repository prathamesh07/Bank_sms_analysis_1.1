from datetime import datetime, timedelta
import pandas as pd

balance_sms = pd.read_csv('data_files/intermediate_output_files/bank_sms_classified_account_type_rectified.csv', parse_dates=['MessageTimestamp'])

balance_sms = balance_sms[balance_sms['MessageType'] == 'Balance']

#Truncating time part of datetime to 00:00:00
balance_sms['MessageTimestamp'] = balance_sms['MessageTimestamp'].apply(pd.datetools.normalize_date)
print len(balance_sms.index.values)

#Considering only first balance sms from each day
balance_sms.drop_duplicates(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)
print len(balance_sms.index.values)

#balance_sms['XX'] = balance_sms['MessageTimestamp']-pd.Timedelta(seconds=1)

for idx, row in balance_sms.iterrows():
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
	BankName = row["BankName"]
	LinkedDebitCardNumber = row['LinkedDebitCardNumber']

	timestamp_for_new_row = MessageTimestamp - timedelta(seconds=1)
	
	to_be_appended = pd.DataFrame({'SmsID':SmsID, 'CustomerID':CustomerID, 'Message':pd.Series(Message), 'MessageSource':pd.Series(MessageSource), 'MessageDate':pd.Series(MessageDate), \
	'MessageTimestamp':timestamp_for_new_row, 'MessageType':pd.Series(MessageType), 'Currency_1':pd.Series(Currency_1), 'Amt_1':Amt_1, 'Currency_2':pd.Series(Currency_2), 'Amt_2':Amt_2, 'Currency_3':pd.Series(Currency_3), \
	'Amt_3':Amt_3, 'Vendor':pd.Series(Vendor), 'AccountNo':pd.Series(AccountNo), 'AccountType':pd.Series(AccountType), 'ReferenceNumber':pd.Series(ReferenceNumber), 'BankName':pd.Series(BankName), 'LinkedDebitCardNumber':pd.Series(LinkedDebitCardNumber)})
	
	balance_sms = balance_sms.append(to_be_appended)

balance_sms.sort_values(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)	

print len(balance_sms.index.values)

#Reading orginal finalbanks_with_cat csv and dropping balance sms rows
bank_sms_with_balance_sms_adjusted = pd.read_csv('data_files/intermediate_output_files/bank_sms_classified_account_type_rectified.csv', parse_dates=['MessageTimestamp'])
bank_sms_with_balance_sms_adjusted = bank_sms_with_balance_sms_adjusted[bank_sms_with_balance_sms_adjusted['MessageType'] != 'Balance']

#Appending adjusted balance sms dates dataframe to orginal dataframe
bank_sms_with_balance_sms_adjusted = bank_sms_with_balance_sms_adjusted.append(balance_sms)

#Sorting according to 'CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'
bank_sms_with_balance_sms_adjusted.sort_values(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)

bank_sms_with_balance_sms_adjusted.to_csv('data_files/intermediate_output_files/bank_sms_with_balance_sms_adjusted.csv', index=False)