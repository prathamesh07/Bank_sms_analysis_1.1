import re

from checkers import checkers_func


from regex_extractor_from_pickle import account_number_re_list
from regex_extractor_from_pickle import debit_vendor_re_list
from regex_extractor_from_pickle import debit_2_vendor_re_list
from regex_extractor_from_pickle import credit_vendor_re_list
from regex_extractor_from_pickle import money_re_list
from regex_extractor_from_pickle import junk_re_list
from regex_extractor_from_pickle import reference_number_re_list
from regex_extractor_from_pickle import credit_card_limit_re_list

from all_dict_generator import bank_dict


number = re.compile(r'\d') # regular expression for a single digit 
amount_re = re.compile(r'\d+.?\d{0,2}') 
currency_re = re.compile(r'[A-Za-z]+') # regular expression for 1 or more upper or lower case leter
nonalpha = re.compile(r'[^a-zA-Z ]+')  # regular expression for 1 or more non alpha character


#------------------------------------------------------------------------------------------------------

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

	credit_limit = [] # replce the last amount with the 1st amount found from the credit card limit re list 
	for credit_limit_re in credit_card_limit_re_list :
		#print credit_limit_re, '*********', type(credit_limit_re)
		credit_limit += re.findall(credit_limit_re,message)

	try :
		RS[2] = credit_limit[0] 
	except IndexError :
		RS = RS[:2]
		pass 

	for i  in range(len(RS)): # for each amount, split it into its currency and the actual amount
		AMT = re.search(amount_re,RS[i]).group()
		#print RS[i],'-------------------------------'
		CUR = re.search(currency_re,RS[i]).group()
		Amount[i] = str(AMT)

		Currency[i] = str(CUR).replace("BALANCE","INR").replace('IS','INR').replace('X','INR').replace('LEDG','INR').replace('BAL','INR')
	return Currency+Amount # returns a list of currency and corresponding actual amounts 

#--------------------------------------------------------------------------------------------

def getCategory(message): # simple method that just uses the methods from checkers file to return the category of the message
	message = str(message)
	#print(message[:10])
	if checkers_func(message, 'Declined'):
		return "Declined"
	if checkers_func(message, 'ATM') and not checkers_func(message, 'Credit'):
		return "ATM"
		#return 'Debit'
	if checkers_func(message, 'OTP') :
		return "OTP"
	if checkers_func(message, 'Balance') and not checkers_func(message, 'Credit') and not checkers_func(message, 'Debit') and not checkers_func(message, 'Debit_2'):
		return "Balance"
	if checkers_func(message, 'Debit_2') and not checkers_func(message, 'Credit'):
		return "Debit"
		#return "Debit_2"
	if checkers_func(message, 'Credit'):
		return "Credit"
	if checkers_func(message, 'Debit'):
		return "Debit"
	if checkers_func(message, 'Min_balance'):
		return "Minimum_balance"
	if checkers_func(message, 'Payment_due'):
		return "Payment_due"
	if checkers_func(message, 'Warning'):
		return "Warning"
	if checkers_func(message, 'Acknowledge'):
		return "Acknowledge"
	if checkers_func(message, 'Advert'):
		return "Advert"
	if checkers_func(message, 'Info'):
		return "Info"
	else :
		return "None"
		
#-------------------------------------------------------------------------------------------------

def getAccountType(message): # simple method that just uses the methods from checkers file to return the Account_type of the message
	if checkers_func(message, 'Debit_Card'):
		return "Debit_Card"
	if checkers_func(message, 'Credit_Card'):
		return "Credit_Card"
	if checkers_func(message, 'CASA'):
		return "CASA"
	if checkers_func(message, 'Wallet') :
		return 'Wallet'
	if checkers_func(message, 'Prepaid_Card'):
		return 'Prepaid_Card'
	if checkers_func(message, 'Loan'):
		return 'Loan'
	else:
		return "_NA_"

#-------------------------------------------------------------------------------------------------------

def getTxnInstrument(message):				# returns the transection instrument
	if checkers_func(message, 'Debit_Card'):
		return "Debit_Card"
	if checkers_func(message, 'ATM'):
		return "ATM"
	if checkers_func(message, 'NEFT'):
		return "NEFT"
	if checkers_func(message, 'IMPS'):
		return "IMPS"
	if checkers_func(message, 'NetBanking'):
		return "NetBanking"
	else:
		return '_NA_'

#-------------------------------------------------------------------------------	
		
def getAccountNumber(message): # retuns the account number
	global account_number_re_list
	account_number = "_NA_"
	for account_number_re in account_number_re_list : # iterates over the ac no re list from regex to find the account number
		search_object = re.search(account_number_re,message)
		if search_object and not checkers_func(message, 'Account_Number_False_Alarm') : # NOW THE Payee Ac No WILL NOT BE EXTRECTED
			
			account_number = ""
			account_number += str(search_object.group(1))
			break										 # only 1st account number is taken

	if len(account_number) < 4 : 						# only last 4 digits of the account number are picked up, if at all the are more digits
		account_number = "0"*(4-len(account_number)) + account_number 
	else :
		account_number = account_number[-4:]

	return account_number

#--------------------------------------------------------------------------------

def getTransactionSource(message , category): # tries to return the transaction source, i.e. vendor , etc 

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

#---------------------------------------------------------------------------------

def getBankName(message_source): # returns the bank name from the sms senders ID
	global bank_dict
	message_source = str(message_source)[3:].upper()[:6]
	if message_source in bank_dict:
		bank_name = bank_dict[message_source]
	else :
		bank_name = "_NA_"
	return bank_name
	
#--------------------------------------------------------------------------------------
	
def getReferenceNumber(message):	# returns the reference number in the message if present 
	#message = message.replace('/','')
	global reference_number_re_list 
	for pattern in reference_number_re_list :
		search_object = re.search(pattern,message) 
		if search_object : 												
			ref_no =search_object.group(1)
			if re.search(number,ref_no): 	 # the reference number must contain atleast 1 numerical/digit
				return ref_no 
	return "_NA_"
	
#---------------------------------------------------------------------------------------

	
def getData(message): # this is the main method that retuns all the data as a list with the help of above functions
	global debit_vendor_re_list
	global debit_2_vendor_re_list
	global credit_vendor_re_list
	global nonalpha
	global junk_re_list

	message = str(message)
	message = message.replace('\n','')


	account_number = getAccountNumber(message)
	category  = getCategory(message)
	money_currency = getMoney(message,category)
	trensection_source = getTransactionSource(message,category)
	account_type = getAccountType(message)
	reference_number = getReferenceNumber(message)
	txn_instrument = getTxnInstrument(message)

	return [category] + [money_currency[0]] + [money_currency[3]]+ [money_currency[1]]+ [money_currency[4]]+ [money_currency[2]]+ [money_currency[5]]+ [account_number]+ [trensection_source] + [account_type] + [reference_number] + [txn_instrument]

#-----------------------------------------------------------------------------------------------------

def getBankDetails(message_source): # returns the bank name from the sms senders ID
	global bank_dict
	message_source = str(message_source)[3:].upper()[:6]
	if message_source in bank_dict:
		bank_det = bank_dict[message_source]
	else :
		bank_det = "_NA_"

	return bank_det

