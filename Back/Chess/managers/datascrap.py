import csv
import time
import re
import bs4
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as request
from tqdm import tqdm

my_url = 'https://le-palais-des-echecs.com/collections/tous-les-ensembles-complets'

# Itérer sur les catégories
##Itérer sur les pages
###Itérer sur les produits d'une page
####Récupérer les données
def get_content(url):
    Client = request(url)
    page_html = Client.read()
    page_soup = soup(page_html, "html.parser")
    return page_soup


def load_product_stats(url): #dans la page du produit
    page_soup = get_content(url)
    products_div = page_soup.find("div", {"class": "description"})
    p_content = products_div.find_all("p")[0:2]
    paradict=[]
    for p in p_content :
        textp = re.findall('[A-Z][^A-Z]*', p.text)
        # textpara = p.content
        # if '\xa0' in paradict:paradict.remove('\xa0')
        # print(textp)
        paradict.append(textp)
        print(paradict)
        return paradict
                # print(p.contents)
        # print(p.string)
    #     for el in textpara:
    #           # print(el)
    #           try:
    #               txt = el.text.strip()
    #           except:
    #               txt=''
    #           paradict.append(txt)
    #     # print(paradict)
    #    # return paradict


def loadpage(id=''): #dans la page des ensembles complets
    url = my_url + 'page=' + str(id) if (id != '') else my_url
    print(url)
    page_soup = get_content(url)
    products = page_soup.find_all("div", {"itemprop": "itemListElement"})
    for product in products:
        product_url = "https://le-palais-des-echecs.com" + product.find("a").get("href")
        print(product_url)
        productstat = load_product_stats(product_url)
        print(productstat)

def writer():
    with open('filename5.csv', 'wb') as file:
        writer = csv.writer(file)
        for row in writer:
            writer.writerow(row)

loadpage(2)


# liste = []
#
# ###################################################################
# complete_sets_start_url = 'https://le-palais-des-echecs.com/collections/tous-les-ensembles-complets'
# variable_url = f'https://le-palais-des-echecs.com/collections/tous-les-ensembles-complets{}'
#
# Client = request(complete_sets_start_url)
# page_html = Client.read()
# next_page = request.get
# soup = bs4.BeautifulSoup(requests.get(complete_sets_start_url).content, 'html.parser')
# # for link in soup.find_all('a'):
# #     print(link.get('href'))
