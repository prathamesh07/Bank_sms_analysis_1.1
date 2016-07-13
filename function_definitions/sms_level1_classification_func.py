import pandas as pd
from all_dict_generator import bank_dict
from all_dict_generator import utilities_dict

"""
This scirpt contains functions wich are used to filter out the desired sms(for e.g. Bank sms, Utility sms, etc.) from given sms.
"""


def new_line_eliminator_func(Message): # gets rid of white spaces
	Message = str(Message).strip()
	return Message

def utf_8_encoder_func(sms):  # encodes the message text with 'utf-8' encoding and returns, if at all some other encoding was used
	try :
		SMS = str(sms.encode('utf-8'))
		#print SMS
	except :
		SMS = str(sms)
	return SMS

def isbank(message_source):		# uses the dictionary provided by all_dict_generator and returns true if the message is from bank
	global bank_dict
	message_source = message_source[3:].upper()
	message_source = message_source[:6]
	if message_source in bank_dict :
		return True 
	return False 


def isutility(message_source):		# uses the dictionary provided by all_dict_generator and returns true if the message is from utility
	global utilities_dict
	message_source = message_source[3:].upper()
	message_source = message_source[:6]
	if message_source in utilities_dict :
		return True 
	return False 




def bank_sms_filtering_func(filename):		# filters out the bank messages
	user_sms_raw_df = pd.read_csv(filename,sep='|', lineterminator='~', converters = {'Message':new_line_eliminator_func})
	# temp
	#user_sms_raw_df.to_csv('data_files/intermediate_output_files/banks/All_sms_raw.csv', index = False)

	#user_sms_raw_df = pd.read_csv(filename)

	user_sms_raw_df.drop_duplicates('Message',inplace=True)
	#user_sms_raw_df['Message'] = user_sms_raw_df['Message'].map(lambda x: str(x).strip())
	#user_sms_raw_df['Message'] = user_sms_raw_df['Message'].apply(utf_8_encoder_func)
	bank_sms_raw_df = user_sms_raw_df[user_sms_raw_df['MessageSource'].map(isbank) == True ]
	bank_sms_raw_df.to_csv('data_files/intermediate_output_files/banks/bank_sms_raw.csv', index = False)
	return bank_sms_raw_df


def utility_sms_filtering_func(filename):		# filters out the utility messages
	user_sms_raw_df = pd.read_csv(filename,sep='|', lineterminator='~', converters = {'Message':new_line_eliminator_func})
	user_sms_raw_df.drop_duplicates('Message',inplace=True)
	#user_sms_raw_df['Message'] = user_sms_raw_df['Message'].map(lambda x: str(x).strip())
	#user_sms_raw_df['Message'] = user_sms_raw_df['Message'].apply(utf_8_encoder_func)
	utility_sms_raw_df = user_sms_raw_df[user_sms_raw_df['MessageSource'].map(isutility) == True ]
	utility_sms_raw_df.to_csv('data_files/intermediate_output_files/utility/utility_sms_raw.csv', index = False)
	return utility_sms_raw_df












