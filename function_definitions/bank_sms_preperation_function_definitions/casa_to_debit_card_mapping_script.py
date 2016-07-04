import pandas as pd
from time import sleep 

def casa_to_debit_card_mapping_func(bank_sms_df):
	#Creating a new column LinkedDebitCardNumber and intializing with _NA_
	bank_sms_df['LinkedDebitCardNumber'] = '_NA_'


	#Storing count of each account type for each user-bank-account combination in dictionary
	user_bank_combinations_idx_dict = {}

	for idx, row in bank_sms_df.iterrows():
		print 3 , '\t\t' , idx
		CustomerID = row['CustomerID']
		BankName = row['BankName']
		
		key = str(CustomerID)+'*'+str(BankName)

		if key in user_bank_combinations_idx_dict.keys():
			user_bank_combinations_idx_dict[key].append(idx)
		else:
			user_bank_combinations_idx_dict[key] = [idx]

	#Mapping of account number with account type
	account_number_account_type_dict = {}

	for key in user_bank_combinations_idx_dict.keys():
		print 3 , '\t\t' , key 
		for idx in user_bank_combinations_idx_dict[key]:
			account_number = bank_sms_df.at[idx, 'AccountNo']
			account_type = bank_sms_df.at[idx, 'AccountType']
			if account_type not in account_number_account_type_dict.keys():
				if account_number != '_NA_' :
					account_number_account_type_dict[account_type] = [account_number]
			else:
				if account_number != '_NA_' :
					account_number_account_type_dict[account_type].append(account_number)
		
	
		
		
		
		try:
			account_number_account_type_dict['CASA'] = list(set(account_number_account_type_dict['CASA']))
			account_number_account_type_dict['Debit_Card'] = list(set(account_number_account_type_dict['Debit_Card']))
			
			if len(account_number_account_type_dict['CASA']) == 1 and len(account_number_account_type_dict['Debit_Card']) == 1:
				#print "no_key_error"
				for idx in user_bank_combinations_idx_dict[key]:
					account_type = bank_sms_df.at[idx, 'AccountType']
					if account_type == 'CASA' :
						bank_sms_df.at[idx, 'LinkedDebitCardNumber'] = account_number_account_type_dict['Debit_Card'][0]
					if account_type == 'Debit_Card':
						bank_sms_df.at[idx, 'AccountType'] = 'CASA'
						bank_sms_df.at[idx, 'AccountNo'] = account_number_account_type_dict['CASA'][0]
						bank_sms_df.at[idx, 'LinkedDebitCardNumber'] = account_number_account_type_dict['Debit_Card'][0]
						bank_sms_df.at[idx, 'TxnInstrument'] = 'Debit_Card'
		except KeyError:
			#print "Key_error"
			#print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
			pass
			
		account_number_account_type_dict = {}
		
		
	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_classified_account_type_rectified2.csv', index=False)
	bank_sms_df.index = range(len(bank_sms_df.index.values))
	return bank_sms_df
	
	
	