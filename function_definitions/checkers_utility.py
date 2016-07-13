from keyphrases_utility import Electricity_keyphrases_list
from keyphrases_utility import Gas_keyphrases_list
from keyphrases_utility import Home_Services_keyphrases_list
from keyphrases_utility import Telecom_keyphrases_list
from keyphrases_utility import Water_keyphrases_list
from keyphrases_utility import DTH_keyphrases_list

from keyphrases_utility import Mobile_keyphrases_list
from keyphrases_utility import Internet_keyphrases_list
from keyphrases_utility import Landline_keyphrases_list

from keyphrases_utility import OTP_keyphrases_list
from keyphrases_utility import Payment_Due_keyphrases_list
from keyphrases_utility import Info_keyphrases_list
from keyphrases_utility import Warning_keyphrases_list
from keyphrases_utility import Balance_keyphrases_list
from keyphrases_utility import Acknowledge_keyphrases_list
from keyphrases_utility import Advert_keyphrases_list

from keyphrases_utility import Payment_Done_keyphrases_list
from keyphrases_utility import Recharge_keyphrases_list

'''
from keyphrases import CASA_keyphrases_list
from keyphrases import Debit_Card_keyphrases_list
from keyphrases import Credit_Card_keyphrases_list
from keyphrases import Wallet_keyphrases_list
from keyphrases import Prepaid_Card_keyphrases_list
from keyphrases import Loan_keyphrases_list

from keyphrases import NEFT_keyphrases_list
from keyphrases import NetBanking_keyphrases_list
from keyphrases import Cheque_keyphrases_list

from keyphrases import Account_Number_False_Alarm_keyphrases_list'''
# Basically all the functions use keys from 'keyphrases' file and return true if the message has any of thoes key phrases


def isDTH(message):
	global DTH_keyphrases_list
	isin = False
	for key in DTH_keyphrases_list:
		key = key.split('\n')
		truthvalue = [keyword in message for keyword in key ]
		if False not in truthvalue :
			return True 

	return False

def isElectricity(message):
	global Electricity_keyphrases_list
	isin = False 
	for key in Electricity_keyphrases_list:
		key = key.split('\n')
		truthvalue = [keyword in message for keyword in key ]
		if False not in truthvalue :
			return True 

	return False 

def isGas(message):
	global Gas_keyphrases_list
	isin = False 
	for key in Gas_keyphrases_list:
		key = key.split('\n')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isHomeService(message):
	global Home_Services_keyphrases_list
	isin = False 
	for key in Home_Services_keyphrases_list:
		key = key.split('\n')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

	
def isTelecom(message):
	global Telecom_keyphrases_list
	isin = False 
	for key in Telecom_keyphrases_list:
		key = key.split('\n')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isWater(message):
	global Water_keyphrases_list
	isin = False 
	for key in Water_keyphrases_list:
		key = key.split('\n')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isMobile(message):
	global Mobile_keyphrases_list
	isin = False 
	for key in Mobile_keyphrases_list:
		key = key.split('\n')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isInternet(message):
	global Internet_keyphrases_list
	isin = False 
	for key in Internet_keyphrases_list:
		key = key.split('\n')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 

def isLandline(message):
	global Landline_keyphrases_list
	isin = False 
	for key in Landline_keyphrases_list:
		key = key.split('\n')
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





def isRecharge(message):
	message = message.upper()
	global Recharge_keyphrases_list
	for key in Recharge_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 	


def isPaymentDone(message):
	message = message.upper()
	global Payment_Done_keyphrases_list
	for key in Payment_Done_keyphrases_list:
		#key = key.upper()
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False 	


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

def isCheque(message):
	global Cheque_keyphrases_list
	for key in Cheque_keyphrases_list :
		key = key.split('|')
		truthvalue = [keyword in message for keyword in key]
		if False not in truthvalue :
			return True 

	return False
