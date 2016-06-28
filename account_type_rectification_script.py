import pandas as pd
import operator

"""
This script replaces the account type of a account with account type in which majority of the sms for that account are tagged \
if same account  is tagged in more than one type
"""

bank_sms_classified = pd.read_csv('data_files/intermediate_output_files/bank_sms_classified.csv')

#Here, we are not considering _NA_ account number because their type cannot be rectified
account_type_rectified = bank_sms_classified[bank_sms_classified['AccountNo'] != '_NA_']
account_type_rectified.index = range(len(account_type_rectified.index))

#Storing count of each account type for each user-bank-account combination in dictionary
user_account_combinations_dict = {}
user_account_combinations_idx_dict = {}


for i in range(len(account_type_rectified.index.values)):
	CustomerID = account_type_rectified.loc[i, 'CustomerID']
	AccountNo = account_type_rectified.loc[i, 'AccountNo']
	AccountType = account_type_rectified.loc[i, 'AccountType']
	key = str(CustomerID)+'*'+str(AccountNo)
	#print CustomerID, type(CustomerID), '^^^^^^^'
	#print AccountNo, type(AccountNo), '%%%%%%%%'
	#print key, '############'
	
	if key in user_account_combinations_idx_dict.keys():
		user_account_combinations_idx_dict[key].append(i)
	else:
		user_account_combinations_idx_dict[key] = [i]
	
	if user_account_combinations_dict.get(key) == None:
		user_account_combinations_dict[key] = {AccountType:1}
	else:
		if user_account_combinations_dict[key].get(AccountType) == None:
			user_account_combinations_dict[key][AccountType] = 1
		else:
			user_account_combinations_dict[key][AccountType] = user_account_combinations_dict[key].get(AccountType)+1
			

print len(user_account_combinations_dict), '@@@@@@@@@@@@@@@@@'


#Eliminating dictionary keys which has length = 1 because they are correctly classified
for key in user_account_combinations_dict.keys():
	if len(user_account_combinations_dict[key]) == 1 :
		del user_account_combinations_dict[key]
		

#Sorting each dictionary key based on its values
for dict_key in user_account_combinations_dict.keys():
	user_account_combinations_dict[dict_key] = sorted(user_account_combinations_dict[dict_key].items(), key=operator.itemgetter(1), reverse=True)

	
print len(user_account_combinations_dict), '**********'
	
#Account type correction logic
for key in user_account_combinations_dict.keys():
	print key
	if user_account_combinations_dict[key][0][0] == '_NA_':
		actual_account_type = user_account_combinations_dict[key][1][0]
	else:
		actual_account_type = user_account_combinations_dict[key][0][0]
	
	for idx in user_account_combinations_idx_dict[key]:
		account_type_rectified.loc[idx, 'AccountType'] = actual_account_type


#Appending _NA_ accounts to rectified account dataframe
bank_sms_classified = bank_sms_classified[bank_sms_classified['AccountNo'] == '_NA_']
account_type_rectified = account_type_rectified.append(bank_sms_classified)

#Sorting dataframe according to user-bank-account-timestamp
account_type_rectified.sort_values(['CustomerID', 'BankName', 'AccountNo', 'MessageTimestamp'], inplace=True)

	
account_type_rectified.to_csv('data_files/intermediate_output_files/bank_sms_classified_account_type_rectified.csv', index=False)		
