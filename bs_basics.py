from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""





soup = BeautifulSoup(html, "html.parser")
d = soup.select("[data-example]") #ALWAYS returns a list
print(d)

d = soup.find(id = "first")
d = soup.find_all(class_= "special")


# id takes and individual id
# class takes multiple ones 

#MORE EXAMPLES= 
# Find an element with an id of foo
soup.find(id="foo")
soup.select("#foo")[0]

# find all elements with a class of bar 
soup.find_all(class_="bar")
soup.select(".bar")

# for loop

soup = BeautifulSoup(html, "html.parser")
for el in soup.select(".special"):
  print (el.get_text()) #METHOD TO get the text 
  print (el.name) # GETS the names




