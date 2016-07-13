import pandas

bank_dict = {}
utilities_dict = {}


# opens a file containg bank ID to bank name mapping and creates a dictionary out of it 
# later on "sms_level1_classification_func.py" will use this to segregate  bank messages from all the messages



# fp = open('data_files/sms_classification_level1_keywords/financial/bank_id_to_bank_name_mapping','r')
# for bank in fp.read().split('\n'):
# 	if bank != '':
# 		bank = bank.split('\t')
# 		bank_dict[bank[0]]  = [ value for value in bank[1:] ]

df = pandas.read_csv('data_files/sms_classification_level1_keywords/financial/TABLE_20160704_SENDER_CLASSIFICATION_v02.csv')
df = df[df['SENDER_PARENT'] == 'FINANCIAL' ]
df.fillna('_NA_',inplace=True)
for i , row in df.iterrows():
	bank_dict[row['SENDER']] = [row['SENDER_NAME'],row['SENDER_PARENT'],row['SENDER_CHILD_1'],row['SENDER_CHILD_2'],row['SENDER_CHILD_3']]



#print bank_dict


# fp = open('data_files/sms_classification_level1_keywords/financial/bank_id_to_bank_name_mapping','r')
# for bank in fp.read().split('\n'):
# 	if bank != '':
# 		bank = bank.split('\t')
# 		bank_dict[bank[0]]  = [ value for value in bank[1:] ]

'''df = pandas.read_csv('data_files/sms_classification_level1_keywords/financial/TABLE_20160704_SENDER_CLASSIFICATION_v02.csv')
df = df[df['SENDER_PARENT'] == 'FINANCIAL' ]
df.fillna('_NA_',inplace=True)
for i , row in df.iterrows():
	bank_dict[row['SENDER']] = [row['SENDER_NAME'],row['SENDER_PARENT'],row['SENDER_CHILD_1'],row['SENDER_CHILD_2'],row['SENDER_CHILD_3']]'''



#print bank_dict


df = pandas.read_csv('data_files/sms_classification_level1_keywords/financial/TABLE_20160704_SENDER_CLASSIFICATION_v02.csv')
df = df[df['SENDER_PARENT'] == 'UTILITY' ]
df.fillna(' ',inplace=True)
for i , row in df.iterrows():
	utilities_dict[row['SENDER']] = [row['SENDER_NAME'],row['SENDER_PARENT'],row['SENDER_CHILD_1'],row['SENDER_CHILD_2'],row['SENDER_CHILD_3']]

		


