from bs4 import BeautifulSoup
import requests

url = input("Enter a URL (start with www): ")
link = "http://" + url
data = requests.get(link).content
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
   print(link.get('href'))