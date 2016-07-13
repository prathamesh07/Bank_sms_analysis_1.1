from keyphrases import Declined_keyphrases_list
from keyphrases import ATM_keyphrases_list
from keyphrases import Debit_keyphrases_list
from keyphrases import Debit_2_keyphrases_list
from keyphrases import Balance_keyphrases_list
from keyphrases import Credit_keyphrases_list
from keyphrases import OTP_keyphrases_list
from keyphrases import Payment_Due_keyphrases_list
from keyphrases import Info_keyphrases_list
from keyphrases import Minimum_balance_keyphrases_list
from keyphrases import Warning_keyphrases_list
from keyphrases import Acknowledge_keyphrases_list
from keyphrases import Advert_keyphrases_list


from keyphrases import CASA_keyphrases_list
from keyphrases import Debit_Card_keyphrases_list
from keyphrases import Credit_Card_keyphrases_list
from keyphrases import Wallet_keyphrases_list
from keyphrases import Prepaid_Card_keyphrases_list
from keyphrases import Loan_keyphrases_list

from keyphrases import NEFT_keyphrases_list
from keyphrases import IMPS_keyphrases_list
from keyphrases import NetBanking_keyphrases_list
from keyphrases import Cheque_keyphrases_list

from keyphrases import Account_Number_False_Alarm_keyphrases_list
# Basically all the functions use keys from 'keyphrases' file and return true if the message has any of those key phrases


keyphrases_dict = {'ATM':ATM_keyphrases_list, 'Declined':Declined_keyphrases_list, 'Debit':Debit_keyphrases_list, 'Debit_2':Debit_2_keyphrases_list, \
'Credit':Credit_keyphrases_list, 'Balance':Balance_keyphrases_list, 'OTP':OTP_keyphrases_list, 'Min_balance':Minimum_balance_keyphrases_list, \
'Info':Info_keyphrases_list, 'Payment_due':Payment_Due_keyphrases_list, 'Advert':Advert_keyphrases_list, 'Warning':Warning_keyphrases_list, \
'Acknowledge':Acknowledge_keyphrases_list, 'CASA':CASA_keyphrases_list, 'Debit_Card':Debit_Card_keyphrases_list, 'Credit_Card':Credit_Card_keyphrases_list, \
'Wallet':Wallet_keyphrases_list, 'Prepaid_Card':Prepaid_Card_keyphrases_list, 'Loan':Loan_keyphrases_list, 'Account_Number_False_Alarm':Account_Number_False_Alarm_keyphrases_list, \
'NEFT':NEFT_keyphrases_list, 'IMPS':IMPS_keyphrases_list, 'NetBanking':NetBanking_keyphrases_list, 'Cheque':Cheque_keyphrases_list}


def checkers_func(message, word):
	
	keyphrases_list = keyphrases_dict[word]
	
	for key in keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 
	return False 