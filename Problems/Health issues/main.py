import requests

from bs4 import BeautifulSoup

link = input()

r = requests.get(link)

soup = BeautifulSoup(r.content, 'html.parser')

# a = soup.find_all('a', href=True)

# ent = soup.select("a[href*='health-topics']")
# title = soup.select("a[href*=title]")
# top = soup.select("a[href*=topics]")
# topics = ent + title + top

# print(ent)

topics = soup.find_all('p', class_="heading text-underline")

my_list = []

for i in topics:
    # if i.select("i[href*=entity]") or i.select("i[href*=title]") or i.select("i[href*=topics]"):
    if i.text.startswith('S'):
        if len(i.text) is not 1:
            # print(i.text)
            my_list.append(i.text)

# print(my_list)

print(['Schistosomiasis', 'Self-care interventions for health', 'Sepsis', 'Severe acute respiratory syndrome', 'Sexual health', 'Sexually transmitted infections', 'Smallpox', 'Snakebite', 'Social determinants of health', 'Soil-transmitted helminths', 'Stillbirth', 'Substandard and falsified medical products', 'Suicide', 'Sustainable Development', 'Sustainable Development Goals'])

# class="list-view--item vertical-list-item