import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

try: 
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' %(exc))

####################################################

#Downloading and saving a file 
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') #Downloads the file
res.raise_for_status() 
playFile = open('RomeoAndJuliet.txt', 'wb') # Creates a new file in binary mode
for chunk in res.iter_content(100000): #loop over the response objects
	playFile.write(chunk) # calls write() to write the content to the file 

playFile.close() 