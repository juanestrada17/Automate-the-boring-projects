tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['cake', 'sweets', 'jollyr', 'loli', "car"]]

def printTable(inputList):
    # initialize the list "colWidths" with zeroes equal to the length of the input list
    colWidths = [0] * len(inputList)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if len(inputList[i][j]) > colWidths[i]: # The len(inputList[i][j] shows the len of each string)
                colWidths[i] = len(inputList[i][j])

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in colWidths
    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidths[y]), end = ' ') # It switches the two around so that it goes from up to down "rotates it"
            # end = "" By default there is a newline character appended to the item being printed (end='\n'), and end='' is used to make it printed on the same line.
        print('') # prints a new line after each list 

printTable(tableData)


# def printTable(table):
#     # create a new list of 3 "0" values: one for each list in tableData
#     colWidths = [0] * len(table)
#     # search for the longest string in each list of tableData
#     # and put the numbers of characters in the new list
#     for y in range(len(table)):
#         for x in table[y]:
#             if colWidths[y] < len(x):
#                 colWidths[y] = len(x)

#     # "rotate" and print the list of lists
#     for x in range(len(table[0])) :
#         for y in range(len(table)) :
#             print(table[y][x].rjust(colWidths[y]), end = ' ')
#         print()
#         x += 1

# printTable(tableData)

# colWidth = [0] * len(tableData) # RETURNS a list with each list in tableData
# colWidth[0]= max(tableData[0], key=len)
# colWidth[1]= max(tableData[1], key=len)
# colWidth[2]= max(tableData[2], key=len)

 
# len(max(colWidth, key = len))

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#  ['Alice', 'Bob', 'Carol', 'David'],
#  ['dogs', 'cats', 'moose', 'goose']]

# # Gives the longest string
# res = max(tableData[0], key = len) 
# res2 = max(tableData[1], key = len) 
# res3 = max(tableData[2], key= len)
 
# len(max(ColWidth, key = len))

# for i in range(len(tableData[0])):
#     for j in range(len(tableData)):
#         print(tableData[j][i].rjust(x[y], end = ""))
#     print("")



# # LOOPS and gets the values organized but not together
# for x in tableData[0]:
#     print (x.rjust(len(res)))
# for y in tableData[1]: 
#     print(y.rjust(len(res2)))
# for z in tableData[2]:
#     print(z.rjust(len(res3)))

# # GIVES ALL ELEMENTS in the list of list

#  for j in tableData:
# ...     for i in j:
# ...             print(i)