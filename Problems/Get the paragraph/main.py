import requests

from bs4 import BeautifulSoup

word = input()
story = input()

r = requests.get(story)

soup = BeautifulSoup(r.content, 'html.parser')
p1 = soup.find_all('p')

for i in p1:
    if word in i.text:
        print(i.text)
        break
