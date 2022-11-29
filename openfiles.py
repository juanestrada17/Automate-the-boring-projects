hello = open('hello.txt')
hello.read()
hello.readlines() - # returns a list of strings
bacon = open('bacon.txt', 'w') # re-writes the contents in a file / write mode
bacon = open('bacon.txt', 'a') # adds the contents to the end / append mode

# #EXAMPLES 
bacon_file = open('bacon.txt', 'w')
bacon_file.write('Hello world!\n')
bacon_file.close()

# SHELVE - SAVE variables in Python programs to binary shelf files 
import shelve 
shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats #assigns the cats key
shelf_file.close()

# # they work like a dictionary - example 
shelf_file = shelve.open('mydata')
list(shelf_file.keys())   #['cats']
list(shelf_file.values()) #['Zophie', 'Pooka', 'Simon']
shelf_file.close()

## PPRINT.pformat 
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

## use it later importing mycats
import myCats
myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
myCats.cats[0]['name']
'Zophie'
