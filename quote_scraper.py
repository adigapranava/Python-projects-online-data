from bs4 import BeautifulSoup
import urllib.request
from pprint import pprint

url = urllib.request.urlopen("http://quotes.toscrape.com/")

soup = BeautifulSoup(url, "html.parser")

quotes = soup.find_all('div',{"class":"quote"})

for quote in quotes:  
    print(quote.find("span",{'itemprop':"text"}).text)
    print("-",quote.find("small").text)
    print()
    
