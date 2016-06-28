import pandas as pd
from bank_dict_generator import bank_dict

def new_line_eliminator_func(Message):
	Message = str(Message).strip()
	return Message

def utf_8_encoder_func(sms):
	try :
		SMS = str(sms.encode('utf-8'))
		#print SMS
	except :
		SMS = str(sms)
	return SMS

def isbank(message_source):
	global bank_dict
	message_source = message_source[3:].upper()
	message_source = message_source[:6]
	if message_source in bank_dict :
		return True 
	return False 

def bank_sms_filtering_func(filename):
	user_sms_raw_df = pd.read_csv(filename,sep='|', lineterminator='~', converters = {'Message':new_line_eliminator_func})
	user_sms_raw_df.drop_duplicates('Message',inplace=True)
	#user_sms_raw_df['Message'] = user_sms_raw_df['Message'].map(lambda x: str(x).strip())
	user_sms_raw_df['Message'] = user_sms_raw_df['Message'].apply(utf_8_encoder_func)
	bank_sms_raw_df = user_sms_raw_df[user_sms_raw_df['MessageSource'].map(isbank) == True ]
	bank_sms_raw_df.to_csv('data_files/intermediate_output_files/bank_sms_raw.csv', index = False)
	return bank_sms_raw_df