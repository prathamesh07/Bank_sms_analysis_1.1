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
from keyphrases import NetBanking_keyphrases_list

from keyphrases import Account_Number_False_Alarm_keyphrases_list


def isATM(message):
	global ATM_keyphrases_list
	isin = False 
	for key in ATM_keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 


def isDeclined(message):
	global Declined_keyphrases_list
	for key in Declined_keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 


def isDebit(message):
	global Debit_keyphrases_list
	for key in Debit_keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 


def isDebit_2(message):
	global Debit_2_keyphrases_list
	for key in Debit_2_keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isCredit(message):
	global Credit_keyphrases_list
	for key in Credit_keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isBalance(message):
	global Balance_keyphrases_list
	for key in Balance_keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isOTP(message):
	global OTP_keyphrases_list
	for key in OTP_keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 



def isMin_balance(message):
	global Minimum_balance_keyphrases_list
	for key in Minimum_balance_keyphrases_list:
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isInfo(message):
	global Info_keyphrases_list
	for key in Info_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isPayment_due(message):
	global Payment_Due_keyphrases_list
	for key in Payment_Due_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 




def isAdvert(message):
	global Advert_keyphrases_list
	for key in Advert_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 


def isWarning(message):
	global Warning_keyphrases_list
	for key in Warning_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 


def isAcknowledge(message):
	global Acknowledge_keyphrases_list
	for key in Acknowledge_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 





def isCASA(message):
	message = message.upper()
	global CASA_keyphrases_list
	for key in CASA_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 	


def isDebit_Card(message):
	message = message.upper()
	global Debit_Card_keyphrases_list
	for key in Debit_Card_keyphrases_list :
		#key = key.upper()
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 	


def isCredit_Card(message):
	message = message.upper()
	global Credit_Card_keyphrases_list
	for key in Credit_Card_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 	

def isWallet(message):
	message = message.upper()
	global Wallet_keyphrases_list
	for key in Wallet_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 	
	
def isPrepaid_Card(message):
	message = message.upper()
	global Prepaid_Card_keyphrases_list
	for key in Prepaid_Card_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False
	

def isLoan(message):
	message = message.upper()
	global Loan_keyphrases_list
	for key in Loan_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False


def isAccount_Number_False_Alarm(message):
	global Account_Number_False_Alarm_keyphrases_list
	for key in Account_Number_False_Alarm_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False
	
	
def isNEFT(message):
	global NEFT_keyphrases_list
	for key in NEFT_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False
	
def isNetBanking(message):
	global NetBanking_keyphrases_list
	for key in NetBanking_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False
	

