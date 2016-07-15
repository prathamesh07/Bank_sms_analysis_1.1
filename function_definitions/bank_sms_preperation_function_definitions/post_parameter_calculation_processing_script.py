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
	
	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/Post_'+account_type+'_parameters.csv',index = False)
		
	return bank_sms_df