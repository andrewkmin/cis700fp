import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser

url = 'https://google.com/search?q=hello'

response = requests.get(url)

with open('output.html', 'wb') as f:
   f.write(response.content)
webbrowser.open('output.html')

soup = BeautifulSoup(response.text, 'lxml')
for g in soup.find_all(class_='g'):
    print(g.text)
    print('-----')