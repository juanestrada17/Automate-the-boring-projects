#MULTIPLY 3 times first 3 letters of a string 

def front3(str):
	return str[:3]*3

front3('Chocolate')


# ##LONGER unecessary way of doing it 

# def makes10(a,b):
# 	if a == 10 or b == 10:
# 		return True 
# 	elif a+b == 10:
# 		return True
# 	else:
# 		return False

# print(makes10(9,1)) 

# ##SHORTER BETTER WAY TO DO IT 

# def makes10(a,b):
# 	return (a == 10 or b == 10 or a+b == 10)




# def sum_double(a,b):
# 	if a == b:
# 		return (a+b)*2
# 	else:
# 		return a+b

# print(sum_double(2,2))

# # BETTER VERSION 

# def sum_double(a,b):
# 	suma = a + b
# 	if a == b:
# 		return suma*2
# 	else:
# 		return suma

# print(sum_double(2,2))


# #front_back changing position of string letters

# def front_back(string):
# 	if len (string) <= 1: # Necessary for not having error if 1 or less
# 		return string
# 	return string[-1] + string[1:-1] + string[0] # access the body

# print(front_back(""))

# # RETURN A WORD with NOT at the beggining

# def not_string(str):
# 	if str[:3] == "not":
# 		return str
# 	else:
# 		return "not " + str 

# print(not_string("nohthing"))


##NEGATIVE numbers 
# def pos_neg(a,b,negative):
# 	if negative: 
# 		return (a< 0 and b <0)
# 	else:
# 		return ((a<0 and b>0) or (a>0 and b<0))

# # PARROT_TROUBLE exercise. Return something depending on the hour

# def parrot_trouble(talking, hour):
# 	if talking and hour < 7:
# 		return True 
# 	elif talking and hour> 20:
# 		return True
# 	else:
# 		return False

# print(parrot_trouble(False, 21))

# # short solution for PARROT_TROUBLE - better

# def parrot_trouble(talking,hour):
# 	return(talking and (hour>7 or hour>20))



# monkey_trouble if the two monkeys smile return True 

# def monkey_trouble(a_smile, b_smile):
# 	if a_smile == True and b_smile == True:
# 		return True 
# 	elif a_smile == False and b_smile == False:
# 		return True
# 	else:
# 		return False


# print(monkey_trouble(False, False))


#SOLUTION 1 - ELIMINATE some letter from a string  

# def missing_char(string,n):
# 	st =  list(string) 
# 		st.pop(n) 
# 		return "".join(st)
	

# # print(missing_char('kitten', 9))
# #SOLUTION 2

# def missing_char(string, n):
# 	front = string[:n]
# 	back = string[n+1:]
# 	return front + back

# print(missing_char('kitten', 1))



#Number is within 10 of 100 or 200

# def near_hundred(n):
# 	if abs(100-n) <= 10 or abs(200-n) <= 10: # IF the number es lesser or equal to ten it's true
# 		return True
# 	return False

# print(near_hundred(199))

# def sleep_in(weekday, vacation):
# 	if not weekday or vacation:
#     	return True
#  	return False

# # absolute difference 21 - n / example diff21(19)2
# def diff21(n):
# 	if n > 21:
# 		return abs(21 - n)*2
# 	return abs(21-n)