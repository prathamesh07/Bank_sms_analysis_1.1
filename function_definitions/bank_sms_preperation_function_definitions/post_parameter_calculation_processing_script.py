import pandas 
from numpy import timedelta64
from datetime import datetime,timedelta


def post_parameter_calculation_func(bank_sms_df,account_type):
	bank_sms_df['TransactionDirectionFlag'] = 'Equal'
	bank_sms_df['TransactionDirectionIndicator'] = 'Multidirectional'
	bank_sms_df['OpeningBalance'] = '_NA_'
	bank_sms_df['ClosingBalance'] = '_NA_'

	for idx,row in bank_sms_df.iterrows():
		print 10 , '\t\t' , idx

		if int(row['TotalCreditTxns']) > int(row['TotalDebitTxns']) :
			bank_sms_df.at[idx,'TransactionDirectionFlag'] = 'Net_Credit'

		elif int(row['TotalCreditTxns']) < int(row['TotalDebitTxns']) :
			bank_sms_df.at[idx,'TransactionDirectionFlag'] = 'Net_Debit'

		else :
			pass

		if float(row['PercentOfCreditTxns']) in [float(0),float(100)] :
			bank_sms_df.at[idx,'TransactionDirectionIndicator'] = 'Unidirectional'

		elif float(row['PercentOfCreditTxns']) == float(50) :
			bank_sms_df.at[idx,'TransactionDirectionIndicator'] = 'Bidirectional'

		else :
			pass

	#print bank_sms_df.index.values
	#raw_input()

	for idx,row in bank_sms_df.iterrows():
		print 10 , '\t\t' , idx

		if  (  ( row['TransactionDirectionFlag'] == 'Net_Credit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')  ):
			try :
				if float(row['MaxBalance']) != '_NA_' :
					bank_sms_df.at[idx,'OpeningBalance'] = float(row['MaxBalance']) - float(row['NetTxnAmt'])
			except :
				pass

		elif(  ( row['TransactionDirectionFlag'] == 'Net_Debit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')   ):
			try :
				if float(row['MinBalance']) != '_NA_' :
					bank_sms_df.at[idx,'OpeningBalance'] = float(row['MinBalance']) - float(row['NetTxnAmt'])
			except :
				pass
		else :
			pass


		if  (  ( row['TransactionDirectionFlag'] == 'Net_Credit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')  ):
			try :
				if float(row['MaxBalance']) != '_NA_':
					bank_sms_df.at[idx,'ClosingBalance'] = float(row['MaxBalance'])
			except ValueError :
				pass

		elif(  ( row['TransactionDirectionFlag'] == 'Net_Debit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')   ):
			try :
				if float(row['MinBalance']) != '_NA_' :
					bank_sms_df.at[idx,'ClosingBalance'] = float(row['MinBalance'])
			except ValueError :
				pass

		else :
			pass

	

	# temp = 0
	
	# #Creating entries for the days not present in  sms data
	# for idx,row in bank_sms_df.iterrows():
	# 	print 10, '\t\t', idx
	# 	current_user = str(row["CustomerID"]) + "*" +  str(row["BankName"]) + "*" + str(row["AccountNumber"])
	# 	if temp == 0 :
	# 		temp = 1
	# 		prev_user = current_user
	# 		continue 
	# 	if current_user != prev_user :
	# 		prev_user = current_user
	# 		continue 
			
	# 	current_date = row['Date'] 
	# 	prev_date = pandas.to_datetime(bank_sms_df.at[idx-1 , 'Date'])
	# 	days = (current_date - prev_date).days
		
	# 	if days <= 1 :
	# 		prev_user = current_user
	# 		continue
		
	# 	prev_closing_bal = bank_sms_df.at[idx-1,'ClosingBalance']
		
		
	# 	for d in range(1,days+1):
	# 		newdate = timedelta(d) +  current_date 
	# 		newRow = row 
	# 		newRow['Date'] = newdate 
	# 		newRow['MaxBalance'] = prev_closing_bal
	# 		newRow['MinBalance'] = prev_closing_bal
	# 		newRow['NetTxnAmt'] = float(0)
	# 		newRow['PercentOfCreditTxns'] = float(0)
	# 		newRow['PercentOfDebitTxns'] = float(0)
	# 		newRow['TotalBulkTxns'] = float(0)
	# 		newRow['TotalCreditTxns'] = float(0)
	# 		newRow['TotalDebitTxns'] = float(0)
	# 		newRow['TotalNumberOfTxns'] = float(0)
	# 		newRow['TransactionDirectionFlag'] = '_NA_'
	# 		newRow['TransactionDirectionIndicator'] = '_NA_'
	# 		newRow['OpeningBalance'] = prev_closing_bal
	# 		newRow['ClosingBalance'] = prev_closing_bal
	# 		newRow = pandas.DataFrame(newRow)
			
	# 		bank_sms_df = bank_sms_df.append(newRow)
		
	# 	prev_user = current_user 
	
	
	# bank_sms_df.sort_values(['CustomerID','BankName','AccountNumber','Date'], inplace=True)
	# bank_sms_df.index = range(len(bank_sms_df.index.values))
	
	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/Post_'+account_type+'_parameters.csv',index = False)
		
	return bank_sms_df






def get_relaviant_dataframe(df,tt='both',at='CASA',m=1,an=0,sn=''):

	if tt == 'both' :
		ttlist = ['Credit','Debit']
	else :
		ttlist = [tt] 

	new_df = df[ (df['MessageType'].map(lembda x : x in ttlist ) ) & (df['AccountType'] == at) & (df['AccountNo'] == an) & (df['BankName'] == sn) ]

	last_date = new.tail(1)['Date']
	last_valid_date = last_date - timedelta64(m,'M')

	new_df = new_df[ new_df['Date'] > last_valid_date ]

	return new_df


def get_no_of_Transaction(df,tt='both',at='CASA',m=1,an=0,sn=''):

	rdf = get_relaviant_dataframe(df,tt=tt,at=at,m=m,an=an,sn=sn)

	return len(rdf)

def get_net_transaction(df,tt='both',at='CASA',m=1,an=0,sn=''):

	rdf = get_relaviant_dataframe(df,tt=tt,at=at,m=m,an=an,sn=sn)

	NetTxnAmt  = 0 

	for idx , row in rdf.iterrows():
		NetTxnAmt+= float(row['NetTxnAmt'])

	return NetTxnAmt


def get_amount_per_transaction(df,tt='both',at='CASA',m=1,an=0,sn=''):

	NetTxnAmt = get_net_transactio(df,tt=tt,at=at,m=m,an=an,sn=sn)
	no_of_txn = get_no_of_Transaction(df,tt=tt,at=at,m=m,an=an,sn=sn)

	if (no_of_txn > 0 ):
		return NetTxnAmt/no_of_txn
	return 0.0 	

def get_amount_per_month(df,tt='both',at='CASA',m=1,an=0,sn=''):
	NetTxnAmt = get_net_transactio(df,tt=tt,at=at,m=m,an=an,sn=sn)

	return NetTxnAmt/m

def get_maximum_balance(df,tt='both',at='CASA',m=1,an=0,sn=''):
	rdf = get_relaviant_dataframe(df,tt=tt,at=at,m=m,an=an,sn=sn)

	maxbal = -99999999

	for idx,row in rdf.iterrows():

		if row['MaxBalance'] > maxbal :
			maxbal = row['MaxBalance']

	return maxbal 

def get_minimum_balance(df,tt='both',at='CASA',m=1,an=0,sn=''):
	rdf = get_relaviant_dataframe(df,tt=tt,at=at,m=m,an=an,sn=sn)

	minbal = 99999999

	for idx,row in rdf.iterrows():

		if row['MinBalance'] < minbal :
			minbal = row['MaxBalance']

	return minbal 
