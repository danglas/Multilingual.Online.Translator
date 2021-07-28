'''
takes word input by user and translates into one language or multiple languages,
depending on user's selection. Translations and examples are scraped from reverso.net.
outputs to both terminal and text file
'''

import requests
import re
from bs4 import BeautifulSoup


translations_array = []
examples_array = []


# creates array of translations
def scrape_translations(soup):
    words = []
    regex = re.compile('.*dict .*')  # space after to exclude 'dictionary'
    # first find 'a' with class 'dict'
    for i in soup.find_all('a', {"class": regex}):
        string = i.text
        a_list = string.split()
        new_string = " ".join(a_list)
        words.append(new_string)
        if len(words) > 1:  # limit list size
            break
    # also find 'div' with class 'dict' and append results to previous results in list
    for i in soup.find_all('div', {"class": regex}):
        # to get rid of lines, spaces
        string = i.text
        a_list = string.split()
        new_string = "".join(a_list)
        words.append(new_string)
        if len(words) > 1:  # limit list size
            break
    return words


# creates array of example sentences
def scrape_examples(soup):
    sentences = []
    regex = re.compile("(src ltr|trg ltr|trg rtl)")  #rtl for Arabic and Hebrew
    for i in soup.find_all('div', {"class": regex}):
        string = i.text
        a_list = string.split()
        new_string = " ".join(a_list)
        sentences.append(new_string)
        if len(sentences) > 2:  # limit list size
            break
    return sentences


def url_connect(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    return BeautifulSoup(r.content, 'html.parser')


language = {'1': 'Arabic',
            '2': 'German',
            '3': 'English',
            '4': 'Spanish',
            '5': 'French',
            '6': 'Hebrew',
            '7': 'Japanese',
            '8': 'Dutch',
            '9': 'Polish',
            '10': 'Portuguese',
            '11': 'Romanian',
            '12': 'Russian',
            '13': 'Turkish'}

print("Hello. Welcome to the Translator. The Translator supports:")

for item in language:  # print the numbered list from the dictionary
    print("{}. {}".format(item, language[item]))

src_key = input("Type the number of your language:\n")

trg_key = input("Type the number of a language you want to translate to "
                "or '0' to translate to all languages:\n")

print("Type the word you want to translate")
source_word = input()

filename = source_word + '.txt'

url = "https://context.reverso.net/translation/"  # url prefix

if int(trg_key) is not 0:  # user chooses one target language
    # make language names lowercase, generate url
    url = url + language[src_key].lower() + '-' + language[trg_key].lower() + '/' + source_word
    soup = url_connect(url)
    translations = scrape_translations(soup)
    f = open(filename, "a")
    f.write(language[trg_key] + " Translation:\n")
    print("\n" + language[trg_key] + " Translation:")
    f.write(translations[0] + '\n\n')
    print(translations[0] + '\n')
    examples = scrape_examples(soup)
    f.write(language[trg_key] + " Example:\n")
    print(language[trg_key] + " Example:")
    for i in range(2):
        f.write(examples[i] + '\n')
        print(examples[i])
    f.close()
else:  # chose 0: all available languages
    source = language[src_key]
    f = open(filename, "a")
    for k, v in language.items():
        if source == v:  # skips when source and target are same
            continue
        soup = url_connect(url + source.lower() + '-' + v.lower() + '/' + source_word)
        translations = scrape_translations(soup)
        f.write(v + " Translation:\n")
        print(v + " Translation:")
        f.write(translations[0] + '\n\n')
        print(translations[0] + '\n')
        examples = scrape_examples(soup)
        f.write(v + " Example:\n")
        print(v + " Example:")
        for i in range(2):
            f.write(examples[i] + '\n')
            print(examples[i])
        # f.write('\n')
    f.close()