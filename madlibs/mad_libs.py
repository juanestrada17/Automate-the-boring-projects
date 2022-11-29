import re, os
 
#Read file
 
startFile = open('C:\\Users\\usuario\\Desktop\\TEST\\automateboring\\madlibs\\story.txt')
startContent = startFile.read()
 
#Start text and user input
 
print('Here is a sample text file:')
print(startContent)
 
#Use regex to extract each type of word
 
seperated = startContent.split(' ')
 
#Ask for user input
  
for index, word in enumerate(seperated):
    if word == 'ADJECTIVE':
        seperated[index] = input('Enter an adjective: ')
    elif word == 'NOUN':
        seperated[index] = input('Enter a noun: ')
    elif word == 'ADVERB':
        seperated[index] = input('Enter an adverb: ')
    elif word == 'VERB.':
        seperated[index] = input('Enter a verb: ') + '.'
 
joined = ' '.join(seperated)
print(joined)
 
 
# #Save the text we generate to a file
 
saveFile = open('Returned text.txt', 'w')
saveFile.write(joined)
saveFile.close()
startFile.close()
 
print('Returned text saved to document, all files are now closed.')