import pandas 



def post_parameter_calculation(bank_sms_df):
	bank_sms_df['TransactionDirectionFlag'] = 'Equal'
	bank_sms_df['TransactionDirectionIndicator'] = 'Multidirectional'
	bank_sms_df['OppeningBalance'] = -9999999999
	bank_sms_df['ClosingBalance'] = -9999999999

	for idx,row in bank_sms_df.iterrows():
		print idx

		if row['TotalCreditTxns'] > row['TotalDebitTxns'] :
			bank_sms_df.at[idx,'TransactionDirectionFlag'] = 'Net_Credit'

		elif row['TotalCreditTxns'] < row['TotalDebitTxns'] :
			bank_sms_df.at[idx,'TransactionDirectionFlag'] = 'Net_Debit'

		else :
			pass

		if row['PercentOfCreditTxns'] in [float(0),float(100)] :
			bank_sms_df.at[idx,'TransactionDirectionIndicator'] = 'Unidirectional'

		elif row['PercentOfCreditTxns'] == float(50) :
			bank_sms_df.at[idx,'TransactionDirectionIndicator'] = 'Bidirectional'

		else :
			pass



	for idx,row in bank_sms_df.iterrows():
		print idx

		if  (  ( row['TransactionDirectionFlag'] == 'Net_Credit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')  ):
			bank_sms_df.at[idx,'OppeningBalance'] = row['MaxBalance'] - row['NetTxnAmt']

		elif(  ( row['TransactionDirectionFlag'] == 'Net_Debit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')   ):
			bank_sms_df.at[idx,'OppeningBalance'] = row['MinBalance'] - row['NetTxnAmt']

		else :
			pass


		if  (  ( row['TransactionDirectionFlag'] == 'Net_Credit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')  ):
			bank_sms_df.at[idx,'ClosingBalance'] = row['MaxBalance']

		elif(  ( row['TransactionDirectionFlag'] == 'Net_Debit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')   ):
			bank_sms_df.at[idx,'ClosingBalance'] = row['MinBalance']

		else :
			pass


	bank_sms_df.to_csv('data_files/intermediate_output_files/Post_CASA_parameters.csv',index = False)
		
	return bank_sms_df


#df = pandas.read_csv('/home/majchinmesh/Bank_sms_analysis_1.1/data_files/intermediate_output_files/CASA_parameters.csv')

#post_parameter_calculation(df)
