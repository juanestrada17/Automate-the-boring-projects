# to make the regex case-insensitive you can use re.I or re.IGNORECASE. Example=
robocop = re.compile(r'robocop', re.I)
robocop.search(
    'RoboCop is part man, part machine, all cop.').group()  # 'RoboCop'

robocop.search('ROBOCOP protects the innocent.').group()  # 'ROBOCOP'

robocop.search(
    'Al, why does your programming book talk about robocop so much?').group()  # 'robocop'

# the sub() method
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED' ## it sustitutes Agent with CENSORED

# example 2
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# A**** told C**** that E**** knew B**** was a double agent.'

# Complex Regexes - ignoring whitespace and comments by using re.VERBOSE
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

#combining re.I, re.VERBOSE and re.DOTALL by using "|""
some_regex_value = re.compile('foo', re.IGNORECASE | re.DOTALL)
