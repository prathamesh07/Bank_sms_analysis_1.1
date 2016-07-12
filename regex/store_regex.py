import re
import pickle

debit_vendor_re_list = []
debit_vendor_re_list.append(re.compile(r' \d{1,2}-\d{1,2}-\d{4} ON ACCOUNT OF(.+?)\. COMBINED AVAILABLE '))
debit_vendor_re_list.append(re.compile(r' \d{1,2}-\d{1,2}-\d{4} TOWARDS (.+?)\. COMBINED AVAILABLE '))
debit_vendor_re_list.append(re.compile(r' AT (.+?) ON '))
debit_vendor_re_list.append(re.compile(r'AT (.+?) IN USING CARD NO'))
debit_vendor_re_list.append(re.compile(r' AT (.+?)\. AVBL'))
debit_vendor_re_list.append(re.compile(r' AT (.+?)\. AVAILABLE'))
debit_vendor_re_list.append(re.compile(r' AT (.+?) OF KARNATAKA'))
debit_vendor_re_list.append(re.compile(r' AT (.+?) ?\.AVL BAL'))
debit_vendor_re_list.append(re.compile(r' AT (.+?) TXN'))
debit_vendor_re_list.append(re.compile(r'\d+\.\d+ AT (.+?) WITH YOUR '))
debit_vendor_re_list.append(re.compile(r'\d{1,2}[A-Z]{3} AT (.+?) \. CALL '))
debit_vendor_re_list.append(re.compile(r'\d+AT(.+?) ?TXN#'))
debit_vendor_re_list.append(re.compile(r' FOR (.+?) ?TXN'))
debit_vendor_re_list.append(re.compile(r' FOR (.+?) ?PAYMENT '))
debit_vendor_re_list.append(re.compile(r' FOR (.+?)\.MAINTAIN'))
debit_vendor_re_list.append(re.compile(r' FOR (.+?) - ACCOUNT '))
debit_vendor_re_list.append(re.compile(r' INFO ?[\.-](.+?)\. YOUR'))
debit_vendor_re_list.append(re.compile(r' AT (.+?)\. FINAL'))
debit_vendor_re_list.append(re.compile(r' -(.+?)\. AVL'))
debit_vendor_re_list.append(re.compile(r' FROM (.+?)\. AVAILABLE '))
debit_vendor_re_list.append(re.compile(r' AT (.+?)[\.:] ?COMBINED'))
debit_vendor_re_list.append(re.compile(r' (?:TOWARDS|ACCOUNT OF) (.+?)[\.:] ?COMBINED'))
debit_vendor_re_list.append(re.compile(r' AT (.+?)\. CALL'))
debit_vendor_re_list.append(re.compile(r' FROM (.+?) ON '))
debit_vendor_re_list.append(re.compile(r' AT (.+?) USING'))
debit_vendor_re_list.append(re.compile(r' AT (.+?)\. TOLLFREE '))
debit_vendor_re_list.append(re.compile(r' DET:(.+?)\. ?A/C'))
debit_vendor_re_list.append(re.compile(r' DETAILS: (.+?)TOT BAL'))
debit_vendor_re_list.append(re.compile(r' DETAILS: (.+?) TXN'))
debit_vendor_re_list.append(re.compile(r' DETAILS: (.+?) TO ACCOUNT'))
debit_vendor_re_list.append(re.compile(r' DET:(.+?)\. ?IF NOT '))
debit_vendor_re_list.append(re.compile(r' AT (.+?) ?IS APP'))
debit_vendor_re_list.append(re.compile(r'/-(.+?)-CLEAR'))
debit_vendor_re_list.append(re.compile(r'/(.+?)CLEAR BALANCE'))
debit_vendor_re_list.append(re.compile(r'-POS-(.+?)-BALANCE'))
debit_vendor_re_list.append(re.compile(r'-ECOM-(.+?)-BALANCE'))
debit_vendor_re_list.append(re.compile(r'ECOM/(.+?)\. GIVE A '))
debit_vendor_re_list.append(re.compile(r'-NFS-(.+?)-BALANCE'))
debit_vendor_re_list.append(re.compile(r'\. (.+?)\. CLEAR BAL '))
debit_vendor_re_list.append(re.compile(r' AT(.+?)\.AVAILABLE'))
debit_vendor_re_list.append(re.compile(r' ON ACCOUNT OF (.+?) @'))
debit_vendor_re_list.append(re.compile(r' (CHQ PAID .+?) VALUE'))
debit_vendor_re_list.append(re.compile(r' TOWARDS (.+?) VALUE'))
debit_vendor_re_list.append(re.compile(r' AT (.+?)\.  ?THIS'))
debit_vendor_re_list.append(re.compile(r'TXN:(.+?)\. ?A/C'))
debit_vendor_re_list.append(re.compile(r' ON(.+?) FOR RS\.'))
debit_vendor_re_list.append(re.compile(r' TRANSACTION ON (.+?) IS'))
debit_vendor_re_list.append(re.compile(r' AT(.+?) IND '))
debit_vendor_re_list.append(re.compile(r' TRANSACTION (.+?) IS:'))
debit_vendor_re_list.append(re.compile(r' TO PAY YOUR (.+?) BILL FOR\. TOTAL '))
debit_vendor_re_list.append(re.compile(r' \d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2} [Ii]nfo: ?(.+?)$'))
debit_vendor_re_list.append(re.compile(r' RS \d+\.?\d+ INFO: ?(.+?)$'))
debit_vendor_re_list.append(re.compile(r'RS \d+\.\d+ ON \d+-\w+-\d+ AT (.+?)$'))
debit_vendor_re_list.append(re.compile(r'^YOUR (.+?) OF '))
debit_vendor_re_list.append(re.compile(r' INFO: ?(.+?)\. TOTAL'))
debit_vendor_re_list.append(re.compile(r'\d{1,2}:\d{1,2}:\d{1,2} INFO: ?(.+?)$'))
debit_vendor_re_list.append(re.compile(r'RS \d+\.?\d{0,2} INFO: ?(.+?)$'))
debit_vendor_re_list.append(re.compile(r'\d{1,2}-\w{3}-\d{1,2} AT (.+?).$'))
debit_vendor_re_list.append(re.compile(r'-DD ISSUE,(.+?)TOT AVBL '))
# debit_vendor_re_list.append(re.compile(r' at (.+?)\.$'))
# debit_vendor_re_list.append(re.compile(r' at (.+?)$'))
# debit_vendor_re_list.append(re.compile(r' for ?(.+?)\.$'))



debit_2_vendor_re_list = []
debit_2_vendor_re_list.append(re.compile(r'TOWARDS ?(.+?) ?VAL'))
debit_2_vendor_re_list.append(re.compile(r' BENEFICIARY : ?(.+?) ?ON'))
debit_2_vendor_re_list.append(re.compile(r'ISSUE,(.+?) TOT '))
debit_2_vendor_re_list.append(re.compile(r' FOR (.+?) TXN '))
debit_2_vendor_re_list.append(re.compile(r'^(.+?) TRANSACTION '))
# debit_2_vendor_re_list.append(re.compile(r''))
# debit_2_vendor_re_list.append(re.compile(r''))
# debit_2_vendor_re_list.append(re.compile(r''))
# debit_2_vendor_re_list.append(re.compile(r''))
# debit_2_vendor_re_list.append(re.compile(r''))
# debit_2_vendor_re_list.append(re.compile(r''))
# debit_2_vendor_re_list.append(re.compile(r''))

credit_vendor_re_list = []
credit_vendor_re_list.append(re.compile(r'TOWARDS ?(.+?) ?VAL'))
credit_vendor_re_list.append(re.compile(r'INFO[\.:](.+?) .YOUR'))
credit_vendor_re_list.append(re.compile(r'BY (.+?) ON'))
#credit_vendor_re_list.append(re.compile(r'Det:(.+?)\. Ac'))
credit_vendor_re_list.append(re.compile(r'DET:(.+?)\. A/?C'))
credit_vendor_re_list.append(re.compile(r'BY (.+?)'))
#credit_vendor_re_list.append(re.compile(r'Info:(.+?)$'))
credit_vendor_re_list.append(re.compile(r'RS \d+\.?\d{0,2} INFO: ?(.+?)$'))






account_number_re_list  = []
account_number_re_list.append(re.compile(r'A/C ?\d+-\d+[\*-]+(\d+)'))
account_number_re_list.append(re.compile(r' \*\*\d+\.\.\.(\d+)'))
account_number_re_list.append(re.compile(r'A/C \d+-\d+[X\*\.]-(\d+)'))
account_number_re_list.append(re.compile(r'ACCOUNT [X\*\.]+\d+[X\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'A/C NO [X\*\.]+\d+[X\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'CARD ACCOUNT \d+[X\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'YOUR A?/?C? [X\*\.]+\d+[X\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'ACCT XX+(\d+)'))
account_number_re_list.append(re.compile(r'CARD ENDING -?(\d+)'))
account_number_re_list.append(re.compile(r'CARD ENDING WITH -?(\d+)'))
account_number_re_list.append(re.compile(r'CREDIT CARD \d+[NX\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'AC NO \d+[NX\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'A/C \d+[NX\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'A/C\.? NO[\.:]? ?XX(\d+)'))
account_number_re_list.append(re.compile(r'CREDIT CARD XX+(\d+)'))
account_number_re_list.append(re.compile(r'CREDITCARD NUMBER XX+(\d+)'))
account_number_re_list.append(re.compile(r' A/C NO\.[X]+(\d+)'))
account_number_re_list.append(re.compile(r'A/C NO\. [NXx\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'A/C [NXx\*\.]*(\d+)'))
account_number_re_list.append(re.compile(r'CARD NO [NXx\*\.]+(\d+)'))
account_number_re_list.append(re.compile(r'CARD [NX\*]+ ?(\d+)'))
account_number_re_list.append(re.compile(r'CARD NO\. [Nx\*X]+(\d+)'))
account_number_re_list.append(re.compile(r'CREDITCARD NUMBER X+(\d+)'))
account_number_re_list.append(re.compile(r' CARD \d+[NX\*/]+(\d+)'))
account_number_re_list.append(re.compile(r' CARD (\d+)'))
account_number_re_list.append(re.compile(r'AC :? ?[NX\*/]+(\d+)'))
account_number_re_list.append(re.compile(r'ACCOUNT NUMBER [NX\*]*(\d+)'))
account_number_re_list.append(re.compile(r' LOAN A/C [A-Z]{3}(\d+)'))
account_number_re_list.append(re.compile(r' ACCOUNT (\d+)'))
account_number_re_list.append(re.compile(r'A/C-X(\d+)X'))
account_number_re_list.append(re.compile(r'[Ss][bB]-(\d+)'))
account_number_re_list.append(re.compile(r'ENDING IN (\d+) IS'))
account_number_re_list.append(re.compile(r'ENDING IN (\d+) WAS'))
account_number_re_list.append(re.compile(r'[X\*]{2,16} ? ?(\d+)'))
account_number_re_list.append(re.compile(r'[N\*]{2,16} ? ?(\d+)'))
# account_number_re_list.append(re.compile(r''))
# account_number_re_list.append(re.compile(r''))
# account_number_re_list.append(re.compile(r''))
# account_number_re_list.append(re.compile(r''))
# account_number_re_list.append(re.compile(r''))
# account_number_re_list.append(re.compile(r''))






junk_re_list = []
junk_re_list.append(re.compile(r' ?HTTP ?'))
junk_re_list.append(re.compile(r' ?WWW ?'))
junk_re_list.append(re.compile(r'^WWW ?'))
junk_re_list.append(re.compile(r' ?COM '))
junk_re_list.append(re.compile(r' ?COM$'))
junk_re_list.append(re.compile(r'^VIN'))
junk_re_list.append(re.compile(r'^VPS'))
junk_re_list.append(re.compile(r'^ ? ?TPT'))
junk_re_list.append(re.compile(r'^ ? ?IIN'))
junk_re_list.append(re.compile(r'^ ? ?INB'))
junk_re_list.append(re.compile(r'^ ? ?IPS'))
junk_re_list.append(re.compile(r'^ ? ?VISAPOS'))
junk_re_list.append(re.compile(r'^ +'))
junk_re_list.append(re.compile(r'^.{1,2}$'))
junk_re_list.append(re.compile(r' PVT '))
junk_re_list.append(re.compile(r' INDI?A?(?: |$)'))
junk_re_list.append(re.compile(r' SELLE?R?(?: |$)'))
junk_re_list.append(re.compile(r' SERVICES?(?: |$)'))
junk_re_list.append(re.compile(r' PRIVATE?(?: |$)'))
junk_re_list.append(re.compile(r' PVT '))
junk_re_list.append(re.compile(r' LIMITED '))
junk_re_list.append(re.compile(r' LTD '))
junk_re_list.append(re.compile(r' IN '))
junk_re_list.append(re.compile(r'     .+'))
junk_re_list.append(re.compile(r' INTERNET '))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))
# junk_re_list.append(re.compile(r''))








money_re_list = []
money_re_list.append(re.compile(r"(?:^| |:|\W)(?:INR|RS|USD|SGD)\W?\W?\d+\.?\d{0,2}")) #proper 
money_re_list.append(re.compile(r"(?:BALANCE ?I?S?:? | IS:? ?)\W?\W?\d+\.?\d{0,2}"))
money_re_list.append(re.compile(r'(?:^| |:|\W)\d+\.?\d{0,2} (?:INR|RS|USD|SGD)'))# proper
money_re_list.append(re.compile(r"BALANCE ?I?S?:? \W?\W?\d+\.?\d{0,2}"))
money_re_list.append(re.compile(r'X\d+: (\d+.?\d*) \* USE'))

money_re_list.append(re.compile(r"LEDG BAL \d+\.?\d{0,2}"))
money_re_list.append(re.compile(r'BAL ?\W ?\d+\.?\d{0,2}'))


reference_number_re_list = []

reference_number_re_list.append(re.compile(r"REFERENCE NUMBER IS:([A-Z0-9]+)",re.IGNORECASE))
reference_number_re_list.append(re.compile(r"REF NO- XXXX(\d+)"))
reference_number_re_list.append(re.compile(r"REFERENCE NUMBER ?([A-Z0-9]+)"))
reference_number_re_list.append(re.compile(r"NEFT IN UTR ([A-Z0-9]+)"))
reference_number_re_list.append(re.compile(r"REF\.? NO\.? ([A-Z0-9]+)"))
reference_number_re_list.append(re.compile(r"REF\.? NO ?\.?:? ?([A-Z0-9/-]+)"))
reference_number_re_list.append(re.compile(r"REF(\d+)"))
reference_number_re_list.append(re.compile(r"REFNO\. IS (\d+)"))
reference_number_re_list.append(re.compile(r"REF ID ([A-Z0-9]+)"))
reference_number_re_list.append(re.compile(r"REF ?# ([A-Z0-9]+)"))
reference_number_re_list.append(re.compile(r"([A-Z0-9]+)IS YOUR REFERENCE NUMBER"))
reference_number_re_list.append(re.compile(r"REFERENCE NO IS ([A-Z0-9-]+)"))
reference_number_re_list.append(re.compile(r"REF\.? NO\.? ?IS ([A-Z0-9]+)"))
reference_number_re_list.append(re.compile(r" REF\. ([A-Z0-9-]+)"))
reference_number_re_list.append(re.compile(r'REF COMP #? ([A-Z0-9-]+)'))
reference_number_re_list.append(re.compile(r"REF\. No\. [A-Za-z]+ IS:(\d+)"))
reference_number_re_list.append(re.compile(r"REF ID ([A-Z0-9-]+)"))
reference_number_re_list.append(re.compile(r"REF:? ?([A-Z0-9-]+)"))
reference_number_re_list.append(re.compile(r"MMT\*(\d+)\*\*"))
# reference_number_re_list.append(re.compile(r""))
# reference_number_re_list.append(re.compile(r""))
# reference_number_re_list.append(re.compile(r""))
# reference_number_re_list.append(re.compile(r""))


credit_card_limit_re_list = []

credit_card_limit_re_list.append(re.compile(r'TOTAL CRE?D?I?T? LI?MI?T ?:? ?((?:INR|RS|USD|SGD)\W{0,2}\d+\.?\d{0,2})'))











regex = {}
regex['account_number_regex'] = account_number_re_list
regex['debit_vendor_regex'] = debit_vendor_re_list
regex['debit_2_vendor_regex'] = debit_2_vendor_re_list
regex['credit_vendor_regex'] = credit_vendor_re_list
regex['money_regex'] = money_re_list
regex['junk_regex'] = junk_re_list
regex['reference_number_regex'] = reference_number_re_list
regex['credit_card_limit_regex'] =  credit_card_limit_re_list


try :
	fileobject = open('../function_definitions/regex.pkl','wb')
except :
	fileobject = open('regex.pkl','wb')


pickle.dump(regex,fileobject)
fileobject.close()











