import pandas as pd
import time

def bank_sms_error_tally_generation_func(bank_sms_df):

	#Filtering out RepeatedTxnFlag = 1 i.e duplicate sms
	bank_sms_df = bank_sms_df[bank_sms_df['RepeatedTxnFlag'] != 1]

	bank_sms_df = bank_sms_df[( ( (bank_sms_df['MessageType'] == 'ATM') & (bank_sms_df['Amt_1'] != -1) ) | (bank_sms_df['MessageType'] == 'Balance') | (bank_sms_df['MessageType'] == 'Debit') | (bank_sms_df['MessageType'] == 'Credit') ) & (bank_sms_df['AccountNo'] != "_NA_")]

	bank_sms_df.index = range(len(bank_sms_df))

	#Creating Amt_2_calculated, Error,ConsecutiveTxnTimespan columns and initializing them with -1, _NA_ and _NA_ resp.
	bank_sms_df['Amt_2_calculated'] = -1
	bank_sms_df['Error'] = '_NA_'
	bank_sms_df['ConsecutiveTxnTimespan'] = '_NA_'


	#To consider balance sms in our calculations, we are overwriting Amt_2 of balance message with Amt_1 and making Amt_1 as 0.
	for idx, row in bank_sms_df.iterrows():
		print 6, '\t\t',idx
		#print row['LinkedDebitCardNumber'], type(row['LinkedDebitCardNumber'])
		#raw_input()
		if row['MessageType'] == 'Balance':
			#print row
			bank_sms_df.at[idx, "Amt_2"] = float(row['Amt_1'])
			bank_sms_df.at[idx, "Amt_1"] = 0
			#print '--------------------------------------------------------------------------------------'


	user_account_combinations_dict = {}

	for idx, row in bank_sms_df.iterrows():
		print 6, '\t\t',idx
		#ti = int(round(time.time() * 1000))
		#row = bank_sms_df.at[i]
		key = str(row['CustomerID'])+str(row['BankName'])+str(row['AccountNo'])
		#tf = int(round(time.time() * 1000))
			
			
		#print "Getting Key time : " , tf - ti 	
		
		#ti = int(round(time.time() * 1000)) 
		try :
			user_account_combinations_dict[key].append(idx)
		except :
			user_account_combinations_dict[key] = [idx]
		
		#tf = int(round(time.time() * 1000))

	#----------------------------------------------------------

	for key in user_account_combinations_dict.keys():
		print 6 , '\t\t' , key 
		indexes = user_account_combinations_dict[key] 
		
		flag = 0 
		for idx in indexes[:-1] :
			#print key,idx
			if float(bank_sms_df.at[idx,'Amt_2']) == -1 and flag == 0 :
				continue
			else:
				flag = 1 
				current_bal_given = float(bank_sms_df.at[idx, 'Amt_2'])
				current_bal_calculated = float(bank_sms_df.at[idx, 'Amt_2_calculated'])
				if current_bal_given != -1 :
					current_bal = current_bal_given 
				elif current_bal_calculated != -1 :
					current_bal = current_bal_calculated 
				else:
					continue
				
				
				next_amt1 = float(bank_sms_df.at[idx+1, 'Amt_1'])
				
				if bank_sms_df.at[idx+1, 'MessageType'] in ['ATM', 'Debit', 'Balance']:
					Amt_2_calculated = current_bal - next_amt1
					
				elif bank_sms_df.at[idx+1, 'MessageType'] == 'Credit':
					Amt_2_calculated = current_bal + next_amt1
				
				bank_sms_df.at[idx+1, 'Amt_2_calculated'] = Amt_2_calculated
				
				if (float(bank_sms_df.at[idx+1, 'Amt_2']) != -1) and (float(bank_sms_df.at[idx+1, 'Amt_2_calculated']) != -1) and (bank_sms_df.at[idx+1, 'MessageType'] != 'Balance'):
					error_timespan = (bank_sms_df.at[idx+1,'MessageTimestamp'] - bank_sms_df.at[idx,'MessageTimestamp']).days
					error = float(bank_sms_df.at[idx+1, 'Amt_2']) - float(bank_sms_df.at[idx+1, 'Amt_2_calculated'])
					
					if abs(error) < 1.0 :
						error = 0
					
					bank_sms_df.at[idx+1, 'Error'] = error
					bank_sms_df.at[idx+1, 'ConsecutiveTxnTimespan'] = error_timespan
					
					
	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_filtered_flaged.csv', index=False)
	bank_sms_df.index = range(len(bank_sms_df.index.values))
	return bank_sms_df
		