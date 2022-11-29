# CREATING the strip function by using a regex 

import re 

def regex_strip (nowhite, remove = " "):
	return re.sub(remove, '', nowhite)

print(regex_strip("holis", "i"))































# strip_regex = re.compile(r'^(\s*)\w*(\s*)'$)
# strip_regex = re.compile(r'\S+')

# def regex_strip(nowhite):
# 	strip_regex = re.compile(r'\S+')
# 	mo = strip_regex.findall(nowhite)
# 	return "".join(mo)
# print(regex_strip("     disk     "))

# #REMOVE 1 from string
# org_string = "This is a sample string"
# patter = r's'
# mod_string = re.sub(pattern, '', org_string)

#REMOVE multiple from string 

# namesRegex = re.compile(r'Agent \w+')
# namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED.'

