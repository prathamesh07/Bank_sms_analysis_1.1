import pandas 



def post_parameter_calculation_func(bank_sms_df):
	bank_sms_df['TransactionDirectionFlag'] = 'Equal'
	bank_sms_df['TransactionDirectionIndicator'] = 'Multidirectional'
	bank_sms_df['OppeningBalance'] = '_NA_'
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
			if float(row['MaxBalance']) != '_NA_' :
				bank_sms_df.at[idx,'OppeningBalance'] = float(row['MaxBalance']) - float(row['NetTxnAmt'])

		elif(  ( row['TransactionDirectionFlag'] == 'Net_Debit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')   ):
			if float(row['MinBalance']) != '_NA_' :
				bank_sms_df.at[idx,'OppeningBalance'] = float(row['MinBalance']) - float(row['NetTxnAmt'])

		else :
			pass


		if  (  ( row['TransactionDirectionFlag'] == 'Net_Credit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')  ):
			if float(row['MaxBalance']) != '_NA_':
				bank_sms_df.at[idx,'ClosingBalance'] = float(row['MaxBalance'])

		elif(  ( row['TransactionDirectionFlag'] == 'Net_Debit'  ) and (row['TransactionDirectionIndicator'] == 'Unidirectional')   ):
			if float(row['MinBalance']) != '_NA_' :
				bank_sms_df.at[idx,'ClosingBalance'] = float(row['MinBalance'])

		else :
			pass


	bank_sms_df.to_csv('data_files/intermediate_output_files/banks/Post_CASA_parameters.csv',index = False)
		
	return bank_sms_df


#df = pandas.read_csv('/home/majchinmesh/Bank_sms_analysis_1.1/data_files/intermediate_output_files/banks/CASA_parameters.csv')

#post_parameter_calculation_func(df)
