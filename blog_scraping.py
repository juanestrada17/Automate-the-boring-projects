# https://www.rithmschool.com/blog # CHECK developer tools with ctrl+shift+J
import requests 
from bs4 import BeautifulSoup
import csv 

response= requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup (response.text, "html.parser")
articles = soup.find_all("article")

with open ("blog_data.csv", "w") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["title","link","date"]) #HEADERS
	
	for article in articles:
		a_tag = article.find("a") #GETS all anchor tags
		title = a_tag.get_text() # gets all text(ALL the titles of the articles)
		url  = a_tag["href"] # gets the url
		date = article.find("time")["datetime"]
		csv_writer.writerow([title, url, date]) #using all the variables to create a csv