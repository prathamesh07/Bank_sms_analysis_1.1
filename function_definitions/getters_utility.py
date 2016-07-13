import re

from checkers_utility import isDTH
from checkers_utility import isTelecom
from checkers_utility import isElectricity
from checkers_utility import isGas
from checkers_utility import isHomeService
from checkers_utility import isWater

from checkers_utility import isMobile
from checkers_utility import isInternet
from checkers_utility import isLandline

from checkers_utility import isOTP
from checkers_utility import isBalance
from checkers_utility import isInfo
from checkers_utility import isPayment_due
from checkers_utility import isWarning
from checkers_utility import isAcknowledge
from checkers_utility import isAdvert

from checkers_utility import isRecharge
from checkers_utility import isPaymentDone
'''
from checkers import isCASA
from checkers import isDebit_Card
from checkers import isCredit_Card
from checkers import isWallet
from checkers import isPrepaid_Card
from checkers import isLoan

from checkers import isNEFT
from checkers import isNetBanking
from checkers import isCheque

from checkers import isAccount_Number_False_Alarm'''


'''from regex_extractor_from_pickle import account_number_re_list
from regex_extractor_from_pickle import debit_vendor_re_list
from regex_extractor_from_pickle import debit_2_vendor_re_list
from regex_extractor_from_pickle import credit_vendor_re_list
from regex_extractor_from_pickle import junk_re_list
'''
from regex_extractor_from_pickle import money_re_list
from regex_extractor_from_pickle import reference_number_utility_re_list

from all_dict_generator import utilities_dict

#print utilities_dict

number = re.compile(r'\d') # regular expression for a single digit 
amount_re = re.compile(r'\d+.?\d{0,2}') 
currency_re = re.compile(r'[A-Za-z]+') # regular expression for 1 or more upper or lower case leter
nonalpha = re.compile(r'[^a-zA-Z ]+')  # regular expression for 1 or more non alpha character




def getMoney(message,category):	# returns upto 3 sets of amount and currency if present
	global money_re_list
	global amount_re
	global currency_re
	

	Amount = ['-1','-1','-1']
	Currency = ['-','-','-']

	RS = []
	RS += re.findall(money_re_list[0],message.replace(',','').replace('  ','')) # checks with a particular regex to get ammount
	RS += re.findall(money_re_list[2],message.replace(',','').replace('  ','')) # checks with other
 	if category in ['Balance'] :
		RS += re.findall(money_re_list[1],message.replace(',','').replace('  ','')) # if category is balance, checks with 1 more 
	if category in ['Debit'] :
		RS += re.findall(money_re_list[3],message.replace(',','').replace('  ','')) # if category is debit, checks with 1 more

	if RS == [] :
		try :
			RS = ['INR ' + re.search(money_re_list[4],message.replace(',','').replace('  ','')).group(1)] # if after above tries still nothing is found
		except :																						  # it tries another regex				
			pass

	# if RS == [] :
	# 	for moneypattern in money_re_list[3:]:
	if len(RS) < 3 :                                 # if after above process still we have less then 3 amounts, try remaining regex
		for i in range(5, len(money_re_list)):
			RS += re.findall(money_re_list[i],message.replace(',','').replace('  ',''))
		

	RS = RS[:3] # pick only 1st 3 amounts from them

	for i  in range(len(RS)): # for each amount, split it into its currency and the actual amount
		AMT = re.search(amount_re,RS[i]).group()
		#print RS[i],'-------------------------------'
		CUR = re.search(currency_re,RS[i]).group()
		Amount[i] = str(AMT)

		Currency[i] = str(CUR).replace("BALANCE","INR").replace('IS','INR').replace('X','INR').replace('LEDG','INR').replace('BAL','INR')
	return Currency+Amount # returns a list of currency and corresponding actual amounts '''


def getUtilityType(message): # simple method that just uses the methods from checkers file to return the category of the message
	message = str(message)
	if isDTH(message):
		return "DTH"
	if isElectricity(message):
		return "ELECTRICITY"
	if isGas(message):
		return "GAS"
	if isHomeService(message):
		return "HOME SERVICE"
	if isTelecom(message) :
		return "TELECOM"
	if isWater(message):
		return "WATER"
	else :
		return "_NA_"

		
def getTelecomType(message):
	message= str(message)
	if isTelecom(message):
		if isMobile(message):
			return "MOBILE"
		if isInternet(message):
			return "INTERNET"
		if isLandline(message):
			return "LANDLINE"
		else:
			return " "
	
	
def getPaymentInfo(message):
	if isRecharge(message):
		return "RECHARGE"
	if isPaymentDone(message):
		return "PAYMENT DONE"
	if isPayment_due(message):
		return "PAYMENT DUE"
	else:
		return "_NA_"
	
		
		
def getMessageType(message): # simple method that just uses the methods from checkers file to return the Account_type of the message
	if isOTP(message):
		return "OTP"
	if isBalance(message):
		return "BALANCE"
	if isPayment_due(message) :
		return 'PAYMENT DUE'
	if isInfo(message):
		return "INFO"
	if isAcknowledge(message):
		return "ACK"
	if isAdvert(message):
		return "ADVERTISEMENT"
	if isWarning(message):
		return "WARNING"
	else :
		return "_NA_"
		



'''def getMobileNumber(message): # retuns the account number
	global mobile_number_re_list
	mobile_number = "_NA_"
	for mobile_number_re in mobile_number_re_list : # iterates over the ac no re list from regex to find the account number
		search_object = re.search(mobile_number_re,message)
		if search_object and not isMobile_Number_False_Alarm(message) : # NOW THE Payee Ac No WILL NOT BE EXTRECTED
			
			Mobile_number = ""
			Mobile_number += str(search_object.group(1))
			break										 # only 1st account number is taken

	if len(Mobile_number) < 4 : 						# only last 4 digits of the account number are picked up, if at all the are more digits
		account_number = "0"*(4-len(account_number)) + account_number 
	else :
		account_number = account_number[-4:]

	return account_number'''


'''def getTransactionSource(message , category): # tries to return the transaction source, i.e. vendor , etc 

	global nonalpha

	if category == 'Debit_2':				
		for RE in debit_2_vendor_re_list:		# tries to match the message with each regex and returns the 1st match
			so = re.search(RE,message)					
			if so :
				v = re.sub(nonalpha , '',so.group(1)) # substitues the non alpha characters with '' , i.e. removes the nonalpha chatacters
				for p in junk_re_list :
					v = re.sub( p, '',v)
				return v

		return 'ERROR/Not_Specified'		

	if category == 'Credit':
		for RE in credit_vendor_re_list:
			so = re.search(RE,message)
			if so :
				v = re.sub(nonalpha , '',so.group(1))
				for p in junk_re_list :
					v = re.sub( p, '',v)
				if v == "RS" or v == "R" :
					 v = 'ERROR/Not_Specified'
				return v
		return 'ERROR/Not_Specified'		

	if category == 'Debit':
		for RE in debit_vendor_re_list:
			so = re.search(RE,message)
			if so :
				v = re.sub(nonalpha , '',so.group(1))

				for p in junk_re_list :
					v = re.sub( p, '',v)
				return v
		return 'ERROR/Not_Specified'

	return 'ERROR/Not_Specified'
'''



def getSenderName(message_source): # returns the bank name from the sms senders ID
	global utilities_dict
	message_source = str(message_source)[3:].upper()[:6]
	if message_source in utilities_dict:
		sender_name = utilities_dict[message_source]
	else :
		sender_name = "_NA_"

		
	return sender_name
	
	
def getReferenceNumber(message):	# returns the reference number in the message if present 
	#message = message.replace('/','')
	global reference_number_utility_re_list 
	for pattern in reference_number_utility_re_list :
		search_object = re.search(pattern,message) 
		if search_object : 												
			ref_no =search_object.group(1)
			if re.search(number,ref_no): 	 # the reference number must contain atleast 1 numerical/digit
				return ref_no 
			else :
				return "_NA_"
	return "_NA_"
	
	
'''def getTxnInstrument(message):				# returns the transection instrument
	if isDebit_Card(message):
		return "Debit_Card"
	if isATM(message):
		return "ATM"
	if isNEFT(message):
		return "NEFT"
	if isNetBanking(message):
		return "NetBanking"
	else:
		return '_NA_'
		'''
	




	
def getData(message): # this is the main method that retuns all the data as a list with the help of above functions
	message = str(message)
	message = message.replace('\n','')


	#account_number = getAccountNumber(message)
	sender_name = getSenderName(message)
	UtilType  = getUtilityType(message)
	msg_type = getMessageType(message)

	money_currency = getMoney(message,msg_type)
	#trensection_source = getTransactionSource(message,category)
	reference_number = getReferenceNumber(message)
	#txn_instrument = getTxnInstrument(message)
	telecomType = getTelecomType(message)
	info = getPaymentInfo(message)

	return  [money_currency[0]] + [money_currency[3]]+ [money_currency[1]]+ [money_currency[4]]+ [money_currency[2]]+ [money_currency[5]] + [reference_number]+[msg_type] + [info]


def getUtilityDetails(message_source): # returns the bank name from the sms senders ID
	global utilities_dict
	message_source = str(message_source)[3:].upper()[:6]
	if message_source in utilities_dict:
		utility_det = utilities_dict[message_source]
	else :
		utility_det = "_NA_"

		
	return utility_det

