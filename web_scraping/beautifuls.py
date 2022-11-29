import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
elems[0].getText()
type(elems)
len(elems)
type(elems[0])
str(elems[0])
elems[0].attrs

# Getting all the <p>

pElems= exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()

# get() method 

soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id') # author
spanElem.get('some_nonexistent_addr') == None 
spanElem.attrs #{'id': 'author'}

########
# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text)
# type(noStarchSoup)

# ###### 
# #IF the HTML is in the folder 

# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile)
# type(exampleSoup)
