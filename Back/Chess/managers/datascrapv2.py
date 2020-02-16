from urllib.request import urlopen
from bs4 import BeautifulSoup

file = "chasse_data.csv"
f = open(file, "w")
Headers = "Echiquier,ChessPieces,StorageBox"
f.write(Headers)
for page in range(0,5):
    url = "https://le-palais-des-echecs.com/collections/tous-les-ensembles-complets?page={}".format(page)
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    products = soup.find_all("div", {"itemprop": "itemListElement"})
    for product in products:
        product_url = "https://le-palais-des-echecs.com" + product.find("a").get("href")



