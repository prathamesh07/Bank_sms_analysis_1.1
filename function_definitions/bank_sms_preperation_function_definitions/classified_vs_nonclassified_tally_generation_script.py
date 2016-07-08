import pandas as pd

def classified_vs_nonclassified_tally_generation_func(bank_sms_df):

	#Creating following two dictionaries- 
	#1. User-bank-account as key and its indexes as values.
	#2. BankName as key and its indexes as values.
	user_bank_account_combination_idx_dict = {}
	bank_name_idx_dict = {}
	
	for idx, row in bank_sms_df.iterrows():
		CustomerID = row['CustomerID']
		AccountNo = row['AccountNo']
		
		key1 = str(CustomerID) + '*' + str(AccountNo)
		key2 = str(row['BankName'])
		
		try:
			user_bank_account_combination_idx_dict[key1].append(idx)
		except KeyError:
			user_bank_account_combination_idx_dict[key1] = [idx]
			
		try:
			bank_name_idx_dict[key2].append(idx)
		except KeyError:
			bank_name_idx_dict[key2] = [idx]
	

	#Creating empty dataframe to store the result
	df = pd.DataFrame()
	for key in user_bank_account_combination_idx_dict:
		CustomerID = key.split('*')[0]
		AccountNo =  key.split('*')[1]
		if AccountNo != '_NA_':
			index_list = user_bank_account_combination_idx_dict[key]
			ClassifiedCounter = 0
			NonClassifiedCounter = 0
			for index in index_list:
				MessageType = bank_sms_df.at[index, 'MessageType']
				if MessageType == 'None':
					NonClassifiedCounter += 1
				else:
					ClassifiedCounter += 1
			
			PercentOfSmsClassified = (float(ClassifiedCounter)/(float(ClassifiedCounter)+float(NonClassifiedCounter)))*100
			
			to_be_appended = pd.DataFrame({'CustomerID':pd.Series(CustomerID), 'AccountNo':pd.Series(AccountNo), 'TotalSmsClassified':ClassifiedCounter, \
			'TotalSmsNonClassified':NonClassifiedCounter, 'PercentOfSmsClassified':PercentOfSmsClassified})
		
			df = df.append(to_be_appended)
		
	df = df[['CustomerID', 'AccountNo', 'TotalSmsClassified', 'TotalSmsNonClassified', 'PercentOfSmsClassified']]
	df.to_csv('data_files/intermediate_output_files/banks/classified_vs_nonclassified_userwise_tally.csv', index=False)
	
	
	#Creating empty dataframe to store the result
	df = pd.DataFrame()
	for key in bank_name_idx_dict:
		index_list = bank_name_idx_dict[key]
		ClassifiedCounter = 0
		NonClassifiedCounter = 0
		for index in index_list:
			MessageType = bank_sms_df.at[index, 'MessageType']
			if MessageType == 'None':
				NonClassifiedCounter += 1
			else:
				ClassifiedCounter += 1
		
		PercentOfSmsClassified = (float(ClassifiedCounter)/(float(ClassifiedCounter)+float(NonClassifiedCounter)))*100
		
		to_be_appended = pd.DataFrame({'BankName':pd.Series(key), 'TotalSmsClassified':ClassifiedCounter, \
		'TotalSmsNonClassified':NonClassifiedCounter, 'PercentOfSmsClassified':PercentOfSmsClassified})
	
		df = df.append(to_be_appended)
		
	df = df[['BankName', 'TotalSmsClassified', 'TotalSmsNonClassified', 'PercentOfSmsClassified']]
	df.to_csv('data_files/intermediate_output_files/banks/classified_vs_nonclassified_bankwise_tally.csv', index=False)
	
