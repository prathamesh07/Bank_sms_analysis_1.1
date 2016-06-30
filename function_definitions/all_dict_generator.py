bank_dict = {}
utilities_dict = {}


# opens a file containg bank ID to bank name mapping and creates a dictionary out of it 
# later on "sms_level1_classification_func.py" will use this to segregate  bank messages from all the messages
fp = open('data_files/sms_classification_level1_keywords/financial/bank_id_to_bank_name_mapping','r')
for bank in fp.read().split('\n'):
	if bank != '':
		bank = bank.split('\t')
		bank_dict[bank[0]]  = bank[1]



fp = open('data_files/sms_classification_level1_keywords/utilities/sender_id_to_sender_name_mapping','r')
for utility in fp.read().split('\n'):
	if utility != '':
		utility = utility.split('\t')
		utilities_dict[utility[0]]  = utility[1]

