import requests
from bs4 import BeautifulSoup

GFG_Python_url = "https://www.geeksforgeeks.org/python-programming-language/"

req = requests.get(GFG_Python_url)
content = req.content

soup = BeautifulSoup(content, 'html.parser')

Topics = soup.find_all("div", {"class":"leftbar-dropdown"})
current_topic = soup.find("li", {"class": "currentpage"}).text
print("You are currently reading : ",current_topic)


for topic in Topics:
    next_topic = topic.find("h2", {"class" : "dropdown-title"}).text
    
    print("Your next topic will be : ",next_topic)
 
