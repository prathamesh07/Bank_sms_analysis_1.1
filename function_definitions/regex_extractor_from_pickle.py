import pickle

fileobjet = open('function_definitions/regex.pkl','rb')
regex = pickle.load(fileobjet)
fileobjet.close()


account_number_re_list = regex['account_number_regex']
debit_vendor_re_list = regex['debit_vendor_regex']
debit_2_vendor_re_list = regex['debit_2_vendor_regex']
credit_vendor_re_list = regex['credit_vendor_regex']
money_re_list  = regex['money_regex']
junk_re_list = regex['junk_regex']
reference_number_re_list = regex['reference_number_regex']