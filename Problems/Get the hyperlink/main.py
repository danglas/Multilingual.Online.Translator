import requests

from bs4 import BeautifulSoup

act = int(input())
link = input()

r = requests.get(link)

soup = BeautifulSoup(r.content, 'html.parser')

a = soup.find_all('a', href=True)

print(a[act - 1]['href'])
