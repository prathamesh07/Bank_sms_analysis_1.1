import pandas as pd
from parameter_calculation_func_definition_script import get_net_transaction


Months = [1, 3, 6, 12]
TxnTypes = ['Credit', 'Debit', 'Both']

def user_bank_account_combination_generation_func(df):
	result = pd.DataFrame()
	df_unique = df.drop_duplicates(['CustomerID', 'BankName', 'AccountNo'], inplace=True)
	
	for idx, row in df_unique .iterrows():
		CustomerID = row['CustomerID']
		BankName = row['BankName']
		AccountNo = row['AccountNo']
		AccountType = row['AccountType']
		
		for Month in Months:
			for TxnType in TxnTypes:
				AvgSpendPerMonth = getAvgSpendPerMonth(df,TransactionType=TxnType,AccountType=AccountType,Month=Month,AccountNumber=AccountNo,SenderName=BankName)
				MaxBal = get_maximum_balance(df,TransactionType=TxnType,AccountType=AccountType,Month=Month,AccountNumber=AccountNo,SenderName=BankName)
				AvgMaxBal = getAvgMaxBal(df,TransactionType=TxnType,AccountType=AccountType,Month=Month,AccountNumber=AccountNo,SenderName=BankName)
				MinBal = get_minimum_balance(df,TransactionType=TxnType,AccountType=AccountType,Month=Month,AccountNumber=AccountNo,SenderName=BankName)
				AvgMinBal = getAvgMinBal(df,TransactionType=TxnType,AccountType=AccountType,Month=Month,AccountNumber=AccountNo,SenderName=BankName)
				Utilization = getUtilization(df,TransactionType=TxnType,AccountType=AccountType,Month=Month,AccountNumber=AccountNo,SenderName=BankName)
				
				to_be_appended = pd.DataFrame({'AvgMonthlySpendInLast'+Month+'MonthsForAccountType'+AccountType:pd.Series(AvgSpendPerMonth), \
				'MaxBalInLast'+Month+'MonthsForAccountType'+AccountType:pd.Series(MaxBal)})
		
		