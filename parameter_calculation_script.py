from datetime import datetime
import pandas as pd

bank_sms_filtered_flaged_CASA = pd.read_csv('data_files/intermediate_output_files/bank_sms_filtered_flaged.csv', parse_dates=['MessageTimestamp'])

bank_sms_filtered_flaged_CASA = bank_sms_filtered_flaged_CASA[bank_sms_filtered_flaged_CASA['AccountType'] == 'CASA' ]
bank_sms_filtered_flaged_CASA = bank_sms_filtered_flaged_CASA.reset_index(drop=True)

#Creating list to store distinct user-bank-account-day combination's indexes
user_bank_acc_day_combination_idx_list=[0]

#Creating empty dataframe to store calculated parameters for each user-bank-account-day combination
CASA_parameters = pd.DataFrame()

#---------------------------------------------------------------------------------------------------

def getNumberOfTxns(l):
	global bank_sms_filtered_flaged_CASA
	TotalDebitTxns = 0
	TotalCreditTxns = 0
	for i in l:
		if bank_sms_filtered_flaged_CASA.loc[i, 'MessageType'] in ['Debit', 'ATM']:
			TotalDebitTxns += 1
		elif bank_sms_filtered_flaged_CASA.loc[i, 'MessageType'] == 'Credit':
			TotalCreditTxns += 1
		
	return (TotalDebitTxns + TotalCreditTxns, TotalDebitTxns, TotalCreditTxns)

	
def getNumberOfBulkTxns(l):
	global bank_sms_filtered_flaged_CASA
	TotalBulkTxns = 0
	for i in l:
		if bank_sms_filtered_flaged_CASA.loc[i, 'BulkTxnFlag']:
			TotalBulkTxns += 1
	return TotalBulkTxns

	
def getPercentOfTxns(TotalDebitTxns, TotalCreditTxns):
	try:
		PercentOfDebitTxns = (TotalDebitTxns/(TotalDebitTxns+TotalCreditTxns))*100
		PercentOfCreditTxns = (TotalCreditTxns/(TotalDebitTxns+TotalCreditTxns))*100
	except ZeroDivisionError:
		PercentOfDebitTxns = 0
		PercentOfCreditTxns = 0
	return (PercentOfDebitTxns, PercentOfCreditTxns)
	
def getNetTxnAmt(l):
	global bank_sms_filtered_flaged_CASA
	NetTxnAmt = 0
	for i in l:
		NetTxnAmt += bank_sms_filtered_flaged_CASA.loc[i, 'TxnAmount']
	return NetTxnAmt
	
def getMaxMinBalance(l):
	global bank_sms_filtered_flaged_CASA
	MaxBalance = -9999999999
	MinBalance = 9999999999
	amount_to_consider = 0 
	for i in l:
		Amt_2 = bank_sms_filtered_flaged_CASA.loc[i, 'Amt_2']
		Amt_2_calculated = bank_sms_filtered_flaged_CASA.loc[i, 'Amt_2_calculated']
		BulkTxnFlag = bank_sms_filtered_flaged_CASA.loc[i, 'BulkTxnFlag']
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

for i in range(len(bank_sms_filtered_flaged_CASA)-1):
	print i
	#print bank_sms_filtered_flaged_CASA.loc[i,'AccountType']

	CustomerID_current = int(bank_sms_filtered_flaged_CASA.loc[i, 'CustomerID'])
	BankName_current = bank_sms_filtered_flaged_CASA.loc[i, 'BankName']
	AccountNo_current = int(bank_sms_filtered_flaged_CASA.loc[i, 'AccountNo'])
	Date_current = bank_sms_filtered_flaged_CASA.loc[i, 'MessageTimestamp'].strftime('%Y-%m-%d')
	
	CustomerID_next = int(bank_sms_filtered_flaged_CASA.loc[i+1, 'CustomerID'])
	BankName_next = bank_sms_filtered_flaged_CASA.loc[i+1, 'BankName']
	AccountNo_next = int(bank_sms_filtered_flaged_CASA.loc[i+1, 'AccountNo'])
	Date_next = bank_sms_filtered_flaged_CASA.loc[i+1, 'MessageTimestamp'].strftime('%Y-%m-%d')
	
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
	
	