xmas_regex = re.compile(r'\d+\s\w+')
xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

vowel_regex = re.compile(r'[aeiouAEIOU]') # creating your own character class
vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')
#['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
# ANOTHER example is  [a-zA-Z0-9] takes a range

#Negative character class, you need to use "^" take all characters that are not in the brackets

consonant_regex = re.compile(r'[^aeiouAEIOU]')
consonant_regex.findall('RoboCop eats baby food. BABY FOOD')
#['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
#', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

# you can use ^ to make it so that an expression starts with something. You can use $ to make it so that an
# expression ends with something 

ends_with_number= re.complie(r'\d$')
ends_with_number.search('Your number is 42')

# the wildcard character 
at_regex = re.compile(r'.at') # MATCHES any character but a white line
at_regex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat'] the dot represents the letter before at, it matches that character

# MATCH everything with Dot-Star (.*) anything that goes after for example "First Name:"
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1) # Al
mo.group(2) # Sweigart

# MATCH ALL CHARACTERS even newlines WITH re.DOTALL
no_new_line_regex = re.compile('.*')
no_new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# Serve the public trust

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'



