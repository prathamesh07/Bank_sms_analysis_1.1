import os
import pandas as pd


# this script basically reads from various text files and 
# adds the data to variables in the form of list or dict
# so that checkers can use it later to compare 
#

DTH_keyphrases_list = []
fp = pd.read_csv("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utilities\DTH_Mapping.csv")
for key in fp.iterrows():
	if key !="":
		DTH_keyphrases_list.append(str(key))


Electricity_keyphrases_list = []
fp = pd.read_csv("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utilities\Electricity_Mapping.csv")
for key in fp.iterrows():
	if key !="":
		Electricity_keyphrases_list.append(str(key))

Gas_keyphrases_list = []
fp = pd.read_csv("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utilities\Gas_Mapping.csv")
for key in fp.iterrows():
	if key !="":
		Gas_keyphrases_list.append(str(key))


Home_Services_keyphrases_list = []
fp = pd.read_csv("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utilities\Home_Services_Mapping.csv")
for key in fp.iterrows():
	if key !="":
		Home_Services_keyphrases_list.append(str(key))

Internet_keyphrases_list = []
fp = pd.read_csv("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utilities\Internet_Mapping.csv")
for key in fp.iterrows():
	if key !="":
		Internet_keyphrases_list.append(str(key))


Telecom_keyphrases_list = []
fp = pd.read_csv("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utilities\Telecom_mapping.csv")
for key in fp.iterrows():
	if key !="":
		Telecom_keyphrases_list.append(str(key))

Water_keyphrases_list = []
fp = pd.read_csv("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utilities\Water_mapping.csv")
for key in fp.iterrows():
	if key !="":
		Water_keyphrases_list.append(str(key))

'''OTP_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/OTP",'r')
for key in fp.read().split('\n'):
	if key !="":
		OTP_keyphrases_list.append(str(key))


Payment_Due_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/payment_due",'r')
for key in fp.read().split('\n'):
	if key !="":
		Payment_Due_keyphrases_list.append(str(key))


Info_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/Info_messages",'r')
for key in fp.read().split('\n'):
	if key !="":
		Info_keyphrases_list.append(str(key))


Minimum_balance_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/min_balance",'r')
for key in fp.read().split('\n'):
	if key !="":
		Minimum_balance_keyphrases_list.append(str(key))


Warning_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/warning",'r')
for key in fp.read().split('\n'):
	if key !="":
		Warning_keyphrases_list.append(str(key))


Acknowledge_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/acknowledge",'r')
for key in fp.read().split('\n'):
	if key !="":
		Acknowledge_keyphrases_list.append(str(key))


Advert_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/Advert",'r')
for key in fp.read().split('\n'):
	if key !="":
		Advert_keyphrases_list.append(str(key))




		
		
		
		
		
		

CASA_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/account_type_keywords/CASA",'r')
for key in fp.read().split('\n'):
	if key !="":
		CASA_keyphrases_list.append(str(key))




Debit_Card_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/account_type_keywords/Debit_card",'r')
for key in fp.read().split('\n'):
	if key !="":
		Debit_Card_keyphrases_list.append(str(key))





Credit_Card_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/account_type_keywords/Credit_card",'r')
for key in fp.read().split('\n'):
	if key !="":
		Credit_Card_keyphrases_list.append(str(key))

Wallet_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/account_type_keywords/Wallet",'r')
for key in fp.read().split('\n'):
	if key !="":
		Wallet_keyphrases_list.append(str(key))

		
Prepaid_Card_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/account_type_keywords/Prepaid_card",'r')
for key in fp.read().split('\n'):
	if key !="":
		Prepaid_Card_keyphrases_list.append(str(key))


Loan_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/account_type_keywords/Loan",'r')
for key in fp.read().split('\n'):
	if key !="":
		Loan_keyphrases_list.append(str(key))


		
NEFT_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/transaction_instrument_keywords/NEFT",'r')
for key in fp.read().split('\n'):
	if key !="":
		NEFT_keyphrases_list.append(str(key))	
		
		
NetBanking_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/transaction_instrument_keywords/Net_banking",'r')
for key in fp.read().split('\n'):
	if key !="":
		NetBanking_keyphrases_list.append(str(key))
		

Cheque_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/transaction_instrument_keywords/Cheque",'r')
for key in fp.read().split('\n'):
	if key !="":
		Cheque_keyphrases_list.append(str(key))		




Account_Number_False_Alarm_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/false_account_number_keywords/Ac_No_False_keyphrases_list",'r')
for key in fp.read().split('\n'):
	if key !="":
		Account_Number_False_Alarm_keyphrases_list.append(str(key))'''
