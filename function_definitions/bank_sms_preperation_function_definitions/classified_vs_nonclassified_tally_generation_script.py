import pandas as pd

def classified_vs_nonclassified_tally_generation_func(bank_sms_df):

	#Creating dictionary of user-bank-account as key and its indexes as values.
	user_bank_account_combination_dict = {}
	for idx, row in bank_sms_df.iterrows():
		CustomerID = row['CustomerID']
		AccountNo = row['AccountNo']
		
		key = str(CustomerID) + '*' + str(AccountNo)
		
		try:
			user_bank_account_combination_dict[key].append(idx)
		except KeyError:
			user_bank_account_combination_dict[key] = [idx]
	

	#Creating empty dataframe to store the result
	df = pd.DataFrame()
	for key in user_bank_account_combination_dict:
		CustomerID = key.split('*')[0]
		AccountNo =  key.split('*')[1]
		if AccountNo != '_NA_':
			index_list = user_bank_account_combination_dict[key]
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
	df.to_csv('data_files/intermediate_output_files/banks/classified_vs_nonclassified_tally.csv', index=False)
		