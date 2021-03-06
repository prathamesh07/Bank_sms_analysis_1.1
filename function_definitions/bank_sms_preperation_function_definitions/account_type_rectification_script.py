import pandas as pd
from time import sleep
import operator

"""
This script replaces the account type of a account with account type in which majority of the sms for that account are tagged \
if same account  is tagged in more than one type
"""

def account_type_rectification_func(bank_sms_df):

	#Here, we are not considering _NA_ account number because their type cannot be rectified
	account_type_rectified = bank_sms_df[bank_sms_df['AccountNo'] != '_NA_']
	account_type_rectified.index = range(len(account_type_rectified.index))

	#Storing count of each account type for each user-bank-account combination in dictionary
	user_account_combinations_dict = {}
	user_account_combinations_idx_dict = {}


	for idx, row in account_type_rectified.iterrows():
		print 2 , "\t\t" , idx
		CustomerID = row['CustomerID']
		AccountNo = row['AccountNo']
		AccountType = row['AccountType']
		key = str(CustomerID)+'*'+str(AccountNo)
		#print CustomerID, type(CustomerID), '^^^^^^^'
		#print AccountNo, type(AccountNo), '%%%%%%%%'
		#print key, '############'
		
		try:
			user_account_combinations_idx_dict[key].append(idx)
		except KeyError:
			user_account_combinations_idx_dict[key] = [idx]
		
		if user_account_combinations_dict.get(key) == None:
			user_account_combinations_dict[key] = {AccountType:1}
		else:
			if user_account_combinations_dict[key].get(AccountType) == None:
				user_account_combinations_dict[key][AccountType] = 1
			else:
				user_account_combinations_dict[key][AccountType] = user_account_combinations_dict[key].get(AccountType)+1
				

	#print len(user_account_combinations_dict), '@@@@@@@@@@@@@@@@@'


	#Eliminating dictionary keys which has length = 1 because they are correctly classified
	for key in user_account_combinations_dict.keys():
		if len(user_account_combinations_dict[key]) == 1 :
			del user_account_combinations_dict[key]
			

	#Sorting each dictionary key based on its values
	for dict_key in user_account_combinations_dict.keys():
		user_account_combinations_dict[dict_key] = sorted(user_account_combinations_dict[dict_key].items(), key=operator.itemgetter(1), reverse=True)

		
	#print len(user_account_combinations_dict), '**********'
		
	#Account type correction logic
	for key in user_account_combinations_dict.keys():
		actual_account_type = ""
		if user_account_combinations_dict[key][0][0] == '_NA_':
			actual_account_type = user_account_combinations_dict[key][1][0]
		else:
			actual_account_type = user_account_combinations_dict[key][0][0]
		
		for idx in user_account_combinations_idx_dict[key]:
			account_type_rectified.at[idx, 'AccountType'] = actual_account_type
		
	
	#Appending accounts having account number _NA_ (which were previously filtered out above) to rectified account dataframe
	bank_sms_df_NA = bank_sms_df[bank_sms_df['AccountNo'] == '_NA_']
	account_type_rectified = account_type_rectified.append(bank_sms_df_NA)

	#Sorting dataframe according to user-bank-account-timestamp
	account_type_rectified.sort_values(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)
	account_type_rectified.to_csv('data_files/intermediate_output_files/banks/bank_sms_classified_account_type_rectified.csv', index=False)
	account_type_rectified.index = range(len(account_type_rectified.index.values))
	return account_type_rectified
