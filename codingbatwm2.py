## checks if multiple substrings are in strings 

def string_match(a, b):
    count = 0
    for i in range(min([len(a), len(b)])-1):
        if a[i] == b[i] and a[i+1] == b[i+1]:
            count += 1
    return count

print(string_match('abc', 'abc'))


## AMOUNT OF TIMES A NUM is in a loop

# def array_count9(nums):
# 	return nums.count(9)

# def array_count9(nums):
# 	count = 0
# 	for num in nums: 
# 		if num == 9:
# 			count += 1
# 	return count

## skips 1 letter in a word 

# def string_bits(stri):
# 	return stri[0::2]

# ## with for loop

# def string_bits(stri):
# 	result = ""
# 	for i in range(len(stri)):
# 		if i%2 ==0:
# 			result+=stri[i]
# 	return result


#IDENTIFY IF A SEQUENCE OF NUMBERS is in a list 
##IMPORTANT 

# def array123 (nums):
# 	s = "".join(str(x) for x in nums)
# 	if "123" in s:
# 		return True
# 	return False 

# print(array123([1, 1, 2, 4, 1]))

# def array123(nums):
# 	for i in range(len(nums)-2):
# 		if nums[i]==1 and nums[i+1]== 2 and nums[i+2]==3:
# 			return True
# 	return False


## def front_times(stri, n):
# 	return (stri[:3])*n

# print(front_times('Chocolate', 3))




# def array_front9(nums):
# 	for x in nums[:4]:
# 		if x == 9:
# 			return True
# 	return False

# print(array_front9([1,2,3,4,9]))




##STRING explosion = 
# def string_splosion(stri):
# 	result = ""
# 	for i in range(len(stri)):
# 		result += stri[:i+1]
# 	return result 

# print(string_splosion("Code"))

######################

# def string_times(stri, n):
# 	if n > -1:
# 		return stri * n 

# print (string_times("Hi", 0))