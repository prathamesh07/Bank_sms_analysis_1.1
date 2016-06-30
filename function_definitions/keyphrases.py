import os

Declined_keyphrases_list = []
fp = open("data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/declined",'r')
for key in fp.read().split('\n'):
	if key !="":
		Declined_keyphrases_list.append(str(key))


ATM_keyphrases_list = []
fp = open("data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/atm",'r')
for key in fp.read().split('\n'):
	if key !="":
		ATM_keyphrases_list.append(str(key))


Debit_keyphrases_list = []
fp = open("data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/spent_online",'r')
for key in fp.read().split('\n'):
	if key !="":
		Debit_keyphrases_list.append(str(key))


Debit_2_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/deposited_to_others_account",'r')
for key in fp.read().split('\n'):
	if key !="":
		Debit_2_keyphrases_list.append(str(key))


Balance_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/Balance",'r')
for key in fp.read().split('\n'):
	if key !="":
		Balance_keyphrases_list.append(str(key))


Credit_keyphrases_list = []
fp = open( "data_files/sms_classification_level2_keywords/financial/bank_level2_classification/message_type_keywords/Credited",'r')
for key in fp.read().split('\n'):
	if key !="":
		Credit_keyphrases_list.append(str(key))


OTP_keyphrases_list = []
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
		Account_Number_False_Alarm_keyphrases_list.append(str(key))
