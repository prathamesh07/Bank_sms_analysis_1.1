from datetime import datetime
import pandas as pd

#---------------------------------------------------------------------------------------------------

bank_sms_filtered_flaged = pd.DataFrame()

def getNumberOfTxns(l):

	global bank_sms_filtered_flaged
	TotalDebitTxns = 0
	TotalCreditTxns = 0
	
	for i in l:
		messageType = bank_sms_filtered_flaged.at[i, 'MessageType'] 
		#print messageType 
		if messageType == 'Debit':
			TotalDebitTxns += 1
		elif messageType == 'Credit':
			TotalCreditTxns += 1
		
	#print 	messageType, TotalCreditTxns 
	
	return (TotalCreditTxns + TotalDebitTxns , TotalDebitTxns, TotalCreditTxns)

	
def getNumberOfBulkTxns(l):
	global bank_sms_filtered_flaged
	TotalBulkTxns = 0
	for i in l:
		if bank_sms_filtered_flaged.at[i, 'BulkTxnFlag']:
			TotalBulkTxns += 1
	return TotalBulkTxns

	
def getPercentOfTxns(TotalDebitTxns, TotalCreditTxns):
	try:
		
		PercentOfDebitTxns = (float(TotalDebitTxns)/(TotalDebitTxns+TotalCreditTxns))*100
		PercentOfCreditTxns = (float(TotalCreditTxns)/(TotalDebitTxns+TotalCreditTxns))*100
	except ZeroDivisionError:
		PercentOfDebitTxns = 0
		PercentOfCreditTxns = 0
	return (PercentOfDebitTxns, PercentOfCreditTxns)
	
def getNetTxnAmt(l):
	global bank_sms_filtered_flaged
	NetTxnAmt = 0
	for i in l:
		NetTxnAmt += float(bank_sms_filtered_flaged.at[i, 'TxnAmount'])
	return NetTxnAmt
	
def getMaxMinBalance(l):
	global bank_sms_filtered_flaged
	MaxBalance = -99999999
	MinBalance = +99999999
	amount_to_consider = 0 
	for i in l:
		Amt_2 = float(bank_sms_filtered_flaged.at[i, 'Amt_2'])
		Amt_2_calculated = float(bank_sms_filtered_flaged.at[i, 'Amt_2_calculated'])
		BulkTxnFlag = bank_sms_filtered_flaged.at[i, 'BulkTxnFlag']
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
		
	if abs(MaxBalance + 99999999 ) < 0.001 :
		MaxBalance = "_NA_"
	if abs(MinBalance - 99999999 ) < 0.001 :
		MinBalance = "_NA_"
			
	return (MaxBalance, MinBalance)
	
			
def parameterCalculationFunc(l):
	TotalNumberOfTxns, TotalDebitTxns, TotalCreditTxns  = getNumberOfTxns(l)
	TotalBulkTxns = getNumberOfBulkTxns(l)
	PercentOfDebitTxns, PercentOfCreditTxns = getPercentOfTxns(TotalDebitTxns, TotalCreditTxns)
	NetTxnAmt= getNetTxnAmt(l)
	MaxBalance, MinBalance = getMaxMinBalance(l)
	return (TotalNumberOfTxns, TotalDebitTxns, TotalCreditTxns, TotalBulkTxns, PercentOfDebitTxns, PercentOfCreditTxns, NetTxnAmt, MaxBalance, MinBalance)
	
 #-------------------------------------------------------------------------------------------------
def parameter_calculation_func(bank_sms_df,account_type):
	
	global bank_sms_filtered_flaged
	bank_sms_filtered_flaged = bank_sms_df[bank_sms_df['AccountType'] == account_type ]
	bank_sms_filtered_flaged = bank_sms_filtered_flaged.reset_index(drop=True)

	bank_sms_df['DummySMSCount'] = -1 
	bank_sms_df['TotalSMSCount'] = -1 
 
	#Creating list to store distinct user-bank-account-day combination's indexes
	user_bank_acc_day_combination_idx_list=[0]

	#Creating empty dataframe to store calculated parameters for each user-bank-account-day combination
	parameters = pd.DataFrame()
	DummyFlag_current = 0

	flag = 1 

	for i in range(len(bank_sms_filtered_flaged)-1):
		print 9 , '\t\t' ,  i
		#print bank_sms_filtered_flaged.at[i,'AccountType']

		if flag == 1 :
			AllSMSOnADayCounter = 1
			DummySMSCounter = 0



		CustomerID_current = int(bank_sms_filtered_flaged.at[i, 'CustomerID'])
		BankName_current = bank_sms_filtered_flaged.at[i, 'BankName']
		SENDER_PARENT_current = bank_sms_filtered_flaged.at[i, 'SENDER_PARENT']
		SENDER_CHILD_1_current = bank_sms_filtered_flaged.at[i, 'SENDER_CHILD_1']
		SENDER_CHILD_2_current = bank_sms_filtered_flaged.at[i, 'SENDER_CHILD_2']
		SENDER_CHILD_3_current = bank_sms_filtered_flaged.at[i, 'SENDER_CHILD_3']
		
		AccountType = bank_sms_filtered_flaged.at[i, 'AccountType']
		AccountNo_current = int(bank_sms_filtered_flaged.at[i, 'AccountNo'])
		Date_current = bank_sms_filtered_flaged.at[i, 'MessageTimestamp'].strftime('%Y-%m-%d')
		
		CustomerID_next = int(bank_sms_filtered_flaged.at[i+1, 'CustomerID'])
		BankName_next = bank_sms_filtered_flaged.at[i+1, 'BankName']
		AccountNo_next = int(bank_sms_filtered_flaged.at[i+1, 'AccountNo'])
		Date_next = bank_sms_filtered_flaged.at[i+1, 'MessageTimestamp'].strftime('%Y-%m-%d')
		
		if CustomerID_current == CustomerID_next and BankName_current == BankName_next and AccountNo_current == AccountNo_next and Date_current == Date_next:
			AllSMSOnADayCounter += 1 
			user_bank_acc_day_combination_idx_list.append(i+1)
			if bank_sms_filtered_flaged.at[i+1, 'DummyFlag'] == 1:
				DummyFlag_current = 1
				DummySMSCounter += 1
				
			flag = 0 
			continue


		else:
			flag = 1 
			TotalNumberOfTxns, TotalDebitTxns, TotalCreditTxns, TotalBulkTxns, PercentOfDebitTxns, PercentOfCreditTxns, NetTxnAmt, MaxBalance, MinBalance = parameterCalculationFunc(user_bank_acc_day_combination_idx_list)
			user_bank_acc_day_combination_idx_list = [i+1]
			
		Date = datetime.strptime(Date_current, '%Y-%m-%d')
		
		percentOfDummyEntries = (float(DummySMSCounter)/float(AllSMSOnADayCounter))*100

		to_be_appended = pd.DataFrame({'TotalSMSCount':AllSMSOnADayCounter,'DummySMSCount':DummySMSCounter,'PercentOfDummyEntries':percentOfDummyEntries,'DummyFlag':DummyFlag_current,'CustomerID':CustomerID_current, 'BankName':pd.Series(BankName_current), 'SENDER_PARENT':pd.Series(SENDER_PARENT_current), 'SENDER_CHILD_1':pd.Series(SENDER_CHILD_1_current), 'SENDER_CHILD_2':pd.Series(SENDER_CHILD_2_current), 'SENDER_CHILD_3':pd.Series(SENDER_CHILD_3_current), 'AccountNumber':AccountNo_current, 'AccountType':AccountType, 'Date':Date, 'TotalNumberOfTxns':TotalNumberOfTxns, 'TotalDebitTxns':TotalDebitTxns, \
		'TotalCreditTxns':TotalCreditTxns, 'TotalBulkTxns':TotalBulkTxns, 'PercentOfDebitTxns':PercentOfDebitTxns, 'PercentOfCreditTxns':PercentOfCreditTxns, 'NetTxnAmt':NetTxnAmt, 'MaxBalance':MaxBalance, 'MinBalance':MinBalance})
		
		DummyFlag_current = 0


		parameters = parameters.append(to_be_appended)
		
	parameters.index = range(len(parameters.index.values))	

	
	parameters = parameters[['AccountNumber','AccountType','BankName','CustomerID','Date','DummyFlag','DummySMSCount','TotalSMSCount','PercentOfDummyEntries','MaxBalance','MinBalance','NetTxnAmt','PercentOfCreditTxns','PercentOfDebitTxns','SENDER_CHILD_1','SENDER_CHILD_2','SENDER_CHILD_3','SENDER_PARENT','TotalBulkTxns','TotalCreditTxns','TotalDebitTxns','TotalNumberOfTxns']]


	parameters.to_csv('data_files/intermediate_output_files/banks/'+account_type+'_parameters.csv', index=False)
	return parameters
	