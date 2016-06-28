import os

bank_dict = {}
fp = open('data_files/sms_classification_level1_keywords/financial/bank_id_to_bank_name_mapping','r')
for bank in fp.read().split('\n'):
	if bank != '':
		bank = bank.split('\t')
		bank_dict[bank[0]]  = bank[1]
