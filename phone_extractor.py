# phone_extractor.py - Finds phone numbers and email addresses on the clipboard.

# THE PIPE means "or"
import pyperclip
import re

#phone regex
phone_regex = re.compile(r'''(     # group 0
	(\d{3}|\(\d{3}\))?             # group 1 - area code, question mark because it is optional, the pipe to separate the parenthesis
	(\s|-|\.)?                     # group 2 separator 
	(\d{3})						   # group 3 first 3 digits
	(\s|-|\.)                      # group 4 separator 
	(\d{4})                        # group 5 last 4 digits 
	(\s*(ext|x|ext.)\s*(\d{2,5}))? # group 6 - group 7 ext x ext - group 8 d 2, 5 extension 
	)''', re.VERBOSE)

# email regex

email_regex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+   #username
	@					#@ symbol
	[a-zA-Z0-9.-]+		#domain name
	(\.[a-zA-Z]{2,4})	#dot-something
	)''', re.VERBOSE)

#find all matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text): 
	phone_num = '_'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phone_num+= 'x' + groups[8]
		matches.append(phone_num)
for groups in email_regex.findall(text):
	matches.append(groups[0])

#Copy results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print ('Copied to clipboard: ')
	print ('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')