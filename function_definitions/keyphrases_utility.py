import os
import pandas as pd


# this script basically reads from various text files and 
# adds the data to variables in the form of list or dict
# so that checkers can use it later to compare 
#


#LEVEL 1 MAPPING

Water_keyphrases_list = []
fp = open("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utility\Water_List","r")
for key in fp.read().split('\n'):
	if key !="":
		Water_keyphrases_list.append(str(key))

#print Water_keyphrases_list

		
DTH_keyphrases_list = []
fp = open("C:/Users/iisha/Documents/GitHub/Bank_sms_analysis_1.1/data_files/sms_classification_level1_keywords\utility\DTH_List","r")
for key in fp.read().split('\n'):
	if key !="":
		DTH_keyphrases_list.append(str(key))
	#print DTH_keyphrases_list
	


Electricity_keyphrases_list = []
fp = open("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utility\Electricity_List","r")
for key in fp.read().split('\n'):
	if key !="":
		Electricity_keyphrases_list.append(str(key))
#print Electricity_keyphrases_list

Gas_keyphrases_list = []
fp = open("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utility\Gas_List","r")
for key in fp.read().split('\n'):
	if key !="":
		Gas_keyphrases_list.append(str(key))
#print Gas_keyphrases_list

Home_Services_keyphrases_list = []
fp = open("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utility\Home_Services_List","r")
for key in fp.read().split('\n'):
	if key !="":
		Home_Services_keyphrases_list.append(str(key))

#print Home_Services_keyphrases_list

Telecom_keyphrases_list = []
fp = open("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level1_keywords\utility\Telecom_List","r")
for key in fp.read().split('\n'):
	if key !="":
		Telecom_keyphrases_list.append(str(key))
#print Telecom_keyphrases_list


# LEVEL 2 MAPPING

Mobile_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\TelecomType\Mobile_Telecom_Utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Mobile_keyphrases_list.append(str(key))


Internet_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\TelecomType\Internet_Telecom_Utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Internet_keyphrases_list.append(str(key))


Landline_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\TelecomType\Landline_Telecom_Utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Landline_keyphrases_list.append(str(key))

#EXTRACTING TYPE OF MESSAGE

Balance_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\Balance_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Balance_keyphrases_list.append(str(key))

#print Balance_keyphrases_list

Credit_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\Credited_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Credit_keyphrases_list.append(str(key))
#print Credit_keyphrases_list

OTP_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\OTP_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		OTP_keyphrases_list.append(str(key))
print "\n"
#print OTP_keyphrases_list

Payment_Due_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\payment_due_1_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Payment_Due_keyphrases_list.append(str(key))
#print Payment_Due_keyphrases_list

Info_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\Info_messages_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Info_keyphrases_list.append(str(key))
#print Info_keyphrases_list

Debit_keyphrases_list = []
fp = open("C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\spent_online_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Debit_keyphrases_list.append(str(key))

Acknowledge_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\iacknowledge_utility",'r')
for key in fp.read().split('\n'):
	if key !="":

		Acknowledge_keyphrases_list.append(str(key))
		


Advert_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\iadvert_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Advert_keyphrases_list.append(str(key))

Balance_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\min_balance_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Balance_keyphrases_list.append(str(key))


Warning_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\warning_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Warning_keyphrases_list.append(str(key))


# EXTRACTING WHETHER PAYMENT IS DONE OR DUE OR RECHARGE

Payment_Due_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\payment_due_2_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Payment_Due_keyphrases_list.append(str(key))
#print Payment_Due_keyphrases_list

Payment_Done_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\payment_done_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Payment_Done_keyphrases_list.append(str(key))

Recharge_keyphrases_list = []
fp = open( "C:\Users\iisha\Documents\GitHub\Bank_sms_analysis_1.1\data_files\sms_classification_level2_keywords\utility\MessageType\irecharge_utility",'r')
for key in fp.read().split('\n'):
	if key !="":
		Recharge_keyphrases_list.append(str(key))




		
		
		
		
		
		



