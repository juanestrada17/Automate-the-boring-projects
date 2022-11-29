import re 

# MAKE something case insensitive 

specific_regex= re.compile(r'(?i)(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.')


print(specific_regex.search('Alice throws Apples.'))

# Matches a first name with Nakamoto, the string has to be capitalized
# nakamoto_regex= re.compile(r'[A-Z][a-z]+([A-Z][a-z]+)? Nakamoto') # [A-Z] takes the first letter [a-z]+ takes the rest of the string THE SECOND one is inside ()? because it can have cap letts inside
# print(nakamoto_regex.search('RoboCop Nakamoto'))


# Matches every three numbers separated by a comma 
# comma_regex = re.compile(r'^\d{1,3}(,\d{3})*$')# asterisk so \d{3} goes infinite
# print(comma_regex.search("62,368,743,563")) # it works with search but not findall()



