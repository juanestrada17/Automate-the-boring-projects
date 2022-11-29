import re

def strong_password (password):
	strong_pass = re.compile(r'^(?=.*\d)(?=.*[a-zA-Z]).{8,}$')
	if strong_pass.search(password) is None:
		return "Password must be at least 8 characters long and include a number"
	return "Good!"

password = input("Please enter a password: ")
print(strong_password(password))



# strong password detection- 8 characters - at least 1 number - Case insensitiv

# strong_pass = re.compile(r'^(?=.*\d)(?=.*[a-zA-Z]).{8,}$')
# print(strong_pass.search('porkupin1'))

#(?=regex_here) is a positive lookahead. It is a zero-width assertion, meaning that it matches a location that is followed by
# the regex contained within (?= and )

# (?=.*\d). Your example means the match needs to be followed by zero or more characters and then a digit (but again that part isn't captured).

# test_regex= re.compile(r'.*\d')
# print(test_regex.search("x1"))




