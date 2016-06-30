from datetime import datetime
import pandas as pd
#import function_definitions.bank_sms_preperation_function_definitions as .

#---------------------------------------------------------------------------------------------------

bank_sms_filtered_flaged_CASA = pd.DataFrame()

def getNumberOfTxns(l):

	global bank_sms_filtered_flaged_CASA
	TotalDebitTxns = 0
	TotalCreditTxns = 0
	
	for i in l:
		messageType = bank_sms_filtered_flaged_CASA.at[i, 'MessageType'] 
		print messageType 
		if messageType in ['Debit', 'ATM']:
			TotalDebitTxns += 1
		elif messageType == 'Credit':
			TotalCreditTxns += 1
		
	print 	messageType, TotalCreditTxns 
	
	return (TotalCreditTxns + TotalDebitTxns , TotalDebitTxns, TotalCreditTxns)

	
def getNumberOfBulkTxns(l):
	global bank_sms_filtered_flaged_CASA
	TotalBulkTxns = 0
	for i in l:
		if bank_sms_filtered_flaged_CASA.at[i, 'BulkTxnFlag']:
			TotalBulkTxns += 1
	return TotalBulkTxns

	
def getPercentOfTxns(TotalDebitTxns, TotalCreditTxns):
	try:
		print type(TotalDebitTxns) , TotalDebitTxns , "--------------------"
		print type(TotalCreditTxns) , TotalCreditTxns , "--------------------"
	
		PercentOfDebitTxns = (float(TotalDebitTxns)/(TotalDebitTxns+TotalCreditTxns))*100
		PercentOfCreditTxns = (float(TotalCreditTxns)/(TotalDebitTxns+TotalCreditTxns))*100
	except ZeroDivisionError:
		PercentOfDebitTxns = 0
		PercentOfCreditTxns = 0
	return (PercentOfDebitTxns, PercentOfCreditTxns)
	
def getNetTxnAmt(l):
	global bank_sms_filtered_flaged_CASA
	NetTxnAmt = 0
	for i in l:
		NetTxnAmt += bank_sms_filtered_flaged_CASA.at[i, 'TxnAmount']
	return NetTxnAmt
	
def getMaxMinBalance(l):
	global bank_sms_filtered_flaged_CASA
	MaxBalance = -9999999999
	MinBalance = 9999999999
	amount_to_consider = 0 
	for i in l:
		Amt_2 = bank_sms_filtered_flaged_CASA.at[i, 'Amt_2']
		Amt_2_calculated = bank_sms_filtered_flaged_CASA.at[i, 'Amt_2_calculated']
		BulkTxnFlag = bank_sms_filtered_flaged_CASA.at[i, 'BulkTxnFlag']
		if BulkTxnFlag in  [1,2] :
			if Amt_2_calculated != -1:
				amount_to_consider = Amt_2_calculated
			else :
				continue  
		else :
			if  Amt_2 != -1 :
				amount_to_consider = Amt_2
			elif Amt_2_calculated != -1:
				amount_to_consider = Amt_2_calculated
			else :
				continue  
		
		if amount_to_consider > MaxBalance :
			MaxBalance = amount_to_consider 
		if amount_to_consider < MinBalance :
			MinBalance = amount_to_consider 

	return (MaxBalance, MinBalance)
	
			
def parameterCalculationFunc(l):
	TotalNumberOfTxns, TotalDebitTxns, TotalCreditTxns  = getNumberOfTxns(l)
	TotalBulkTxns = getNumberOfBulkTxns(l)
	PercentOfDebitTxns, PercentOfCreditTxns = getPercentOfTxns(TotalDebitTxns, TotalCreditTxns)
	NetTxnAmt= getNetTxnAmt(l)
	MaxBalance, MinBalance = getMaxMinBalance(l)
	return (TotalNumberOfTxns, TotalDebitTxns, TotalCreditTxns, TotalBulkTxns, PercentOfDebitTxns, PercentOfCreditTxns, NetTxnAmt, MaxBalance, MinBalance)
	
 #-------------------------------------------------------------------------------------------------
def parameter_calculation_func(bank_sms_df):
	
	global bank_sms_filtered_flaged_CASA
	bank_sms_filtered_flaged_CASA = bank_sms_df[bank_sms_df['AccountType'] == 'CASA' ]
	bank_sms_filtered_flaged_CASA = bank_sms_filtered_flaged_CASA.reset_index(drop=True)

	#Creating list to store distinct user-bank-account-day combination's indexes
	user_bank_acc_day_combination_idx_list=[0]

	#Creating empty dataframe to store calculated parameters for each user-bank-account-day combination
	CASA_parameters = pd.DataFrame()

	for i in range(len(bank_sms_filtered_flaged_CASA)-1):
		print i
		#print bank_sms_filtered_flaged_CASA.at[i,'AccountType']

		CustomerID_current = int(bank_sms_filtered_flaged_CASA.at[i, 'CustomerID'])
		BankName_current = bank_sms_filtered_flaged_CASA.at[i, 'BankName']
		AccountNo_current = int(bank_sms_filtered_flaged_CASA.at[i, 'AccountNo'])
		Date_current = bank_sms_filtered_flaged_CASA.at[i, 'MessageTimestamp'].strftime('%Y-%m-%d')
		
		CustomerID_next = int(bank_sms_filtered_flaged_CASA.at[i+1, 'CustomerID'])
		BankName_next = bank_sms_filtered_flaged_CASA.at[i+1, 'BankName']
		AccountNo_next = int(bank_sms_filtered_flaged_CASA.at[i+1, 'AccountNo'])
		Date_next = bank_sms_filtered_flaged_CASA.at[i+1, 'MessageTimestamp'].strftime('%Y-%m-%d')
		
		if CustomerID_current == CustomerID_next and BankName_current == BankName_next and AccountNo_current == AccountNo_next and Date_current == Date_next:
			user_bank_acc_day_combination_idx_list.append(i+1)
			continue
		else:
			TotalNumberOfTxns, TotalDebitTxns, TotalCreditTxns, TotalBulkTxns, PercentOfDebitTxns, PercentOfCreditTxns, NetTxnAmt, MaxBalance, MinBalance = parameterCalculationFunc(user_bank_acc_day_combination_idx_list)
			user_bank_acc_day_combination_idx_list = [i+1]
			
		Date = datetime.strptime(Date_current, '%Y-%m-%d')
		
		to_be_appended = pd.DataFrame({'CustomerID':CustomerID_current, 'BankName':pd.Series(BankName_current), 'AccountNumber':AccountNo_current, 'Date':Date, 'TotalNumberOfTxns':TotalNumberOfTxns, 'TotalDebitTxns':TotalDebitTxns, \
		'TotalCreditTxns':TotalCreditTxns, 'TotalBulkTxns':TotalBulkTxns, 'PercentOfDebitTxns':PercentOfDebitTxns, 'PercentOfCreditTxns':PercentOfCreditTxns, 'NetTxnAmt':NetTxnAmt, 'MaxBalance':MaxBalance, 'MinBalance':MinBalance})
		
		CASA_parameters = CASA_parameters.append(to_be_appended)
		
	CASA_parameters.to_csv('data_files/intermediate_output_files/CASA_parameters.csv', index=False)
	return CASA_parameters
	