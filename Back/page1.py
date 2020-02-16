import re

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as request
from tqdm import tqdm


def scrap(my_url):
    Client = request(my_url)
    page_html = Client.read()
    page_soup = soup(page_html, "html.parser")
    products = page_soup.find_all('div[contains(@class,"one-third column")]')
    #products = page_soup.find_all('div', href=re.compile("one-third column"))

    mylist = []
    for elements in products:
        print(elements)
        print(products)
    # mylist.append(products)
    # print(mylist)


scrap('https://le-palais-des-echecs.com/collections/tous-les-ensembles-complets')
