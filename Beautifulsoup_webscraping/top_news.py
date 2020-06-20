from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen("https://www.indiatoday.in/")

soup = BeautifulSoup(url, "html.parser")

topnews = soup.find('ul',{"class":"itg-listing"})

newslist = topnews.find_all("li")

print("=== Top News of India ===\n")
count=1
for news in newslist:
    print(str(count)+")"+news.find("a").text)
    count += 1
    print()
