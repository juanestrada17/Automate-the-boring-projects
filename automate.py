# MESSAGE letter count /character count

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
count.setdefault(character, 0)
count[character] = count[character] + 1
print(count)
# can also import pprint.pprint(count) to make it look better

# ## PROJECT NUMBER 3 / prints a heart

# grid = [['.', '.', '.', '.', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['.', 'O', 'O', 'O', 'O', 'O'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.']]

# for x in range(len(grid[0])): # takes x
# 	for y in range(len(grid)): # takes y
# 		print (grid[y][x], end= "") # maps the numbers on the grid
# 	print() #CREATES A NEW LINE so that it shows the heard


# PROJECT NUMBER 2 / TRANSFORM LIST INTO A STRING and put and AND at the end

# def comma (lista):
# 	commas = ", "
# 	space = " "
# 	lista[-1] = "and " + lista[-1]
# 	if len(lista) ==1:
# 		return lista[0] # NECESSARY SO THAT it doesn't return "and lista[-1]"
# 	elif len(lista) ==2:
# 		return space.join(lista)
# 	return commas.join(lista)

# print (comma(["apples", "cats", "dogs", "tits"]))


# PROGRAM NUMBER 1 - Collatz program

# def collatz(number):
# 	if number % 2 == 0:
# 		print (number//2)
# 		return number//2
# 	else:
# 		print (3*number+1)
# 		return 3* number+1

# x = input("Please, enter a number: " )

# while x != 1: #loop UNTIL X is ONE
# 	x = collatz(int(x))


# 	x = input("Please, enter a number: " )
# print(collatz(int(x)))
