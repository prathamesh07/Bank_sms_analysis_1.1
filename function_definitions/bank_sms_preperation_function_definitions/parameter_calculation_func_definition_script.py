import pandas as pd

def get_relevant_dataframe(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	if TransactionType == 'both' :
		TransactionTypelist = ['Credit','Debit']
	else :
		TransactionTypelist = [TransactionType] 

	if AccountNumber >=0 :
		new_df = df[ (df['MessageType'].map(lambda x : x in TransactionTypelist ) ) & (df['AccounTransactionTypeype'] == at) & (df['AccountNo'] == AccountNumber) & (df['BankName'] == SenderName) ]
	else :
		new_df = df[ (df['MessageType'].map(lambda x : x in TransactionTypelist ) ) & (df['AccounTransactionTypeype'] == at) & (df['BankName'] == SenderName) ]

	last_date = new_df.tail(1)['Date']
	last_valid_date = last_date - timedelta64(m,'M')

	new_df = new_df[ new_df['Date'] > last_valid_date ]

	return new_df


def get_no_of_transactions(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	df = get_relevant_dataframe(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	return len(df)
	

def getAvgTransactions(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	TotalTxns = get_no_of_transactions(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	AvgTransactions = float(TotalTxns)/Month
	return AvgTransactions
	
#Intermediate func
def get_net_transaction(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	df = get_relevant_dataframe(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	NetTxnAmt  = 0 
	for idx , row in df.iterrows():
		NetTxnAmt+= float(row['NetTxnAmt'])
	return NetTxnAmt
	
	
def getAvgSpendPerMonth(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	NetTxn = get_net_transaction(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	AvgSpendPerMonth = float(NetTxn)/Month
	return AvgSpendPerMonth
	
def getAvgSpendPerTxn(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	NetTxn = get_net_transaction(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	TotalTxns = get_no_of_transactions(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	try:
		AvgSpendPerTxn = float(NetTxn)/TotalTxns
	except ZeroDivisionError:
		AvgSpendPerTxn = 0
	return AvgSpendPerTxn
	

def get_maximum_balance(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	df = get_relevant_dataframe(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	maxbal = -99999999
	for idx,row in df.iterrows():
		if row['MaxBalance'] > maxbal and str(row['MaxBalance']).isdigit():
			maxbal = row['MaxBalance']
	
	if maxbal == -99999999:
		return '_NA_'
	return maxbal


def getAvgMaxBal(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	MaxBalList = []
	df = get_relevant_dataframe(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	last_date = df.tail(1)['Date']
	for i in range(Month):
		last_valid_date = last_date - timedelta64(1,'M')
		df = df[ (df['Date'] > last_valid_date) & (df['Date'] < last_date) ]
		maxbal = -99999999
		for idx,row in df.iterrows():
			if row['MaxBalance'] > maxbal and str(row['MaxBalance']).isdigit():
				maxbal = row['MaxBalance']
	
		if maxbal == -99999999:
			continue
		MaxBalList.append(maxbal)
		last_date = last_valid_date
	
	try:
		AvgMaxBal = float(sum(MaxBalList))/len(MaxBalList)
	except ZeroDivisionError:
		AvgMaxBal = '_NA_'
	return AvgMaxBal
	
	
	
	
def get_minimum_balance(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	df = get_relevant_dataframe(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	minbal = 99999999
	for idx,row in df.iterrows():
		if row['MinBalance'] < minbal and str(row['MinBalance']).isdigit():
			minbal = row['MaxBalance']
			
	if minbal == 99999999:
		return '_NA_'
	return minbal
	
	
def getAvgMinBal(df,TransactionType='both',AccountType='CASA',Month=1,AccountNumber=0,SenderName=''):
	MinBalList = []
	df = get_relevant_dataframe(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	last_date = df.tail(1)['Date']
	for i in range(Month):
		last_valid_date = last_date - timedelta64(1,'M')
		df = df[ (df['Date'] > last_valid_date) & (df['Date'] < last_date) ]
		minbal = 99999999
		for idx,row in df.iterrows():
			if row['MinBalance'] < minbal and str(row['MinBalance']).isdigit():
				minbal = row['MaxBalance']
			
		if minbal == 99999999:
			continue
		MinBalList.append(minbal)
		last_date = last_valid_date
	
	try:
		AvgMinBal = float(sum(MinBalList))/len(MinBalList)
	except ZeroDivisionError:
		AvgMinBal = '_NA_'
	return AvgMinBal




		
def getUtilization(df,TransactionType='both',AccountType='Credit_Card',Month=1,AccountNumber=0,SenderName=''):
	df = get_relevant_dataframe(df,TransactionType=TransactionType,AccountType=AccountType,Month=Month,AccountNumber=AccountNumber,SenderName=SenderName)
	minbal = get_minimum_balance(df,TransactionType='both',AccountType='Credit_Card',Month=1,AccountNumber=0,SenderName='')
	
	Amt_3 = -99999999
	for idx, row in df.iterrows():
		if row['Amt_3'].isdigit() and row['Amt_3'] > Amt_3 :
			Amt_3 = row['Amt_3']
			
	if Amt_3 == -99999999:
		Amt_3 = '_NA_'
		
	try:
		Utilization = (float(Amt_3)-float(minbal))/float(Amt_3)
	except ValueError:
		Utilization = '_NA_'
	except ZeroDivisionError:
		Utilization = '_NA_'
	return Utilization