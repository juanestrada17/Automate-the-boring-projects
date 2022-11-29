import os 
os.path.join('usr','bin','spam') # MAKES it avaliable in all operating systems


#ASSIGN STRING NAMES 
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles: 
	print(os.path.join('C:\\Users\\Juan', filename))

#C:\Users\asweigart\accounts.txt
#C:\Users\asweigart\details.csv
#C:\Users\asweigart\invite.docx

#GET A DIRECTORY
os.getcwd()

# CREATE NEW FOLDERS WITH THE PROGRAM USING os.makedirs()

os.makedirs('C:\\delicious\\walnut\\waffles') # creates the folder with everything inside

#absolute and relative paths WITH os.path() module

os.path.abspath(path) # string of the absolute path of the argument 
os.path.isabs(path) # returns True if it's aboslute and False if relative
os.path.relpath(path, start) 

# BASE NAME and DIR NAME

# C:\Windows\System32(DIR NAME)\calc.exe(BASE NAME)
path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)
os.path.dirname(path)
os.path.split(path) # gives a tuple with dirname and base name

path.split(os.path.sep) # ['C:','Windows', 'System32', 'calc.exe']

#FINDING FILE SIZES AND CONTENTS IN FOLDERS 

os.path.getsize(path) #SIZE in bytes
os.listdir(path) #FILENAME strings for each file in path - ALL FILES IN folder 

#TOTAL size of all the files 

total_size= 0 
for filename in os.listdir('C:\\Windows\\System32'):
	total_size = total_size + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(total_size)

#CHECK PATH VALIDITY

os.path.exists(path) #returns True if the file or folder exists 
os.path.isfile(path) #returns True if the file exists
os.path.isdir(path)  #returns True if the folder exists  











