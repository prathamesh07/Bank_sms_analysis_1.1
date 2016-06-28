import pandas as pd

bank_sms_classified_account_type_rectified = pd.read_csv('data_files/intermediate_output_files/bank_sms_classified_account_type_rectified.csv', parse_dates=['MessageTimestamp'])

#Creating a new column LinkedDebitCardNumber and intializing with _NA_
bank_sms_classified_account_type_rectified['LinkedDebitCardNumber'] = '_NA_'


#Storing count of each account type for each user-bank-account combination in dictionary
user_bank_combinations_idx_dict = {}

for i in range(len(bank_sms_classified_account_type_rectified.index.values)):
	CustomerID = bank_sms_classified_account_type_rectified.loc[i, 'CustomerID']
	BankName = bank_sms_classified_account_type_rectified.loc[i, 'BankName']
	
	key = str(CustomerID)+'*'+str(BankName)

	if key in user_bank_combinations_idx_dict.keys():
		user_bank_combinations_idx_dict[key].append(i)
	else:
		user_bank_combinations_idx_dict[key] = [i]

#Mapping of account number with account type
account_number_account_type_dict = {}

for key in user_bank_combinations_idx_dict.keys():
	print key, '*********', len(user_bank_combinations_idx_dict[key])
	for idx in user_bank_combinations_idx_dict[key]:
		account_number = bank_sms_classified_account_type_rectified.loc[idx, 'AccountNo']
		account_type = bank_sms_classified_account_type_rectified.loc[idx, 'AccountType']
		if account_number not in account_number_account_type_dict.keys():
			account_number_account_type_dict[account_type] = [account_number]
		else:
			account_number_account_type_dict[account_type].append(account_number)
	
	try:
		if len(account_number_account_type_dict['CASA']) == 1 and len(account_number_account_type_dict['Debit_Card']) == 1:
			for idx in user_bank_combinations_idx_dict[key]:
				account_type = bank_sms_classified_account_type_rectified.loc[idx, 'AccountType']
				if account_type == 'CASA':
					bank_sms_classified_account_type_rectified.loc[idx, 'LinkedDebitCardNumber'] = account_number_account_type_dict['Debit_Card'][0]
				if account_type == 'Debit_Card':
					bank_sms_classified_account_type_rectified.loc[idx, 'AccountType'] = 'CASA'
					bank_sms_classified_account_type_rectified.loc[idx, 'TxnInstrument'] = 'Debit_Card'
	except KeyError:
		pass
		
	account_number_account_type_dict = {}
	
	
bank_sms_classified_account_type_rectified.to_csv('data_files/intermediate_output_files/bank_sms_classified_account_type_rectified.csv', index=False)
		
	
	
	