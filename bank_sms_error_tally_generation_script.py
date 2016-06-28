import pandas as pd

bank_sms_filtered_flaged = pd.read_csv('data_files/intermediate_output_files/bank_sms_flaged.csv', parse_dates=['MessageTimestamp'])

#Filtering out RepeatedTxnFlag = 1 i.e duplicate sms
bank_sms_filtered_flaged = bank_sms_filtered_flaged[bank_sms_filtered_flaged['RepeatedTxnFlag'] != 1]

bank_sms_filtered_flaged = bank_sms_filtered_flaged[( ( (bank_sms_filtered_flaged['MessageType'] == 'ATM') & (bank_sms_filtered_flaged['Amt_1'] != -1) ) | (bank_sms_filtered_flaged['MessageType'] == 'Balance') | (bank_sms_filtered_flaged['MessageType'] == 'Debit') | (bank_sms_filtered_flaged['MessageType'] == 'Credit') ) & (bank_sms_filtered_flaged['AccountNo'] != "_NA_")]

bank_sms_filtered_flaged.index = range(len(bank_sms_filtered_flaged))

#Creating Amt_2_calculated, Error,ConsecutiveTxnTimespan columns and initializing them with -1, _NA_ and _NA_ resp.
bank_sms_filtered_flaged['Amt_2_calculated'] = -1
bank_sms_filtered_flaged['Error'] = '_NA_'
bank_sms_filtered_flaged['ConsecutiveTxnTimespan'] = '_NA_'


#To consider balance sms in our calculations, we are overwriting Amt_2 of balance message with Amt_1 and making Amt_1 as 0.
for idx, row in bank_sms_filtered_flaged.iterrows():
	if row['MessageType'] == 'Balance':
		bank_sms_filtered_flaged.loc[idx, 'Amt_2'] = row['Amt_1']
		bank_sms_filtered_flaged.loc[idx, 'Amt_1'] = 0


user_account_combinations_dict = {}

for i in range(len(bank_sms_filtered_flaged.index.values) - 1):
	print bank_sms_filtered_flaged.loc[i, 'CustomerID'], '**********'
	print bank_sms_filtered_flaged.loc[i, 'BankName'], '$$$$$$$$$$$$$'
	print bank_sms_filtered_flaged.loc[i, 'AccountNo'], '%%%%%%%%%%%%%%%'
	key = str(bank_sms_filtered_flaged.loc[i, 'CustomerID'])+str(bank_sms_filtered_flaged.loc[i, 'BankName'])+str(bank_sms_filtered_flaged.loc[i, 'AccountNo'])
	if key in user_account_combinations_dict :
		user_account_combinations_dict[key].append(i)
	else :
		user_account_combinations_dict[key] = [i]

#----------------------------------------------------------

for key in user_account_combinations_dict.keys():
	indexes = user_account_combinations_dict[key] 
	
	flag = 0 
	for idx in indexes[:-1] :
		if bank_sms_filtered_flaged.loc[idx,'Amt_2'] == -1 and flag == 0 :
			continue
		else:
			flag = 1 
			current_bal_given = bank_sms_filtered_flaged.loc[idx, 'Amt_2']
			current_bal_calculated = bank_sms_filtered_flaged.loc[idx, 'Amt_2_calculated']
			if current_bal_given != -1 :
				current_bal = current_bal_given 
			elif current_bal_calculated != -1 :
				current_bal = current_bal_calculated 
			else:
				continue
			
			
			next_amt1 = bank_sms_filtered_flaged.loc[idx+1, 'Amt_1']
			
			if bank_sms_filtered_flaged.loc[idx+1, 'MessageType'] in ['ATM', 'Debit', 'Balance']:
				Amt_2_calculated = current_bal - next_amt1
				
			elif bank_sms_filtered_flaged.loc[idx+1, 'MessageType'] == 'Credit':
				Amt_2_calculated = current_bal + next_amt1
			
			bank_sms_filtered_flaged.loc[idx+1, 'Amt_2_calculated'] = Amt_2_calculated
			
			if bank_sms_filtered_flaged.loc[idx+1, 'Amt_2'] != -1 and bank_sms_filtered_flaged.loc[idx+1, 'Amt_2_calculated'] != -1 and bank_sms_filtered_flaged.loc[idx+1, 'MessageType'] != 'Balance':
				error_timespan = (bank_sms_filtered_flaged.loc[idx+1,'MessageTimestamp'] - bank_sms_filtered_flaged.loc[idx,'MessageTimestamp']).days
				error = bank_sms_filtered_flaged.loc[idx+1, 'Amt_2'] - bank_sms_filtered_flaged.loc[idx+1, 'Amt_2_calculated']
				
				if abs(error) < 0.01 :
					error = 0
				
				bank_sms_filtered_flaged.loc[idx+1, 'Error'] = error
				bank_sms_filtered_flaged.loc[idx+1, 'ConsecutiveTxnTimespan'] = error_timespan
				
				
bank_sms_filtered_flaged.to_csv('data_files/intermediate_output_files/bank_sms_filtered_flaged.csv', index=False)
			
		