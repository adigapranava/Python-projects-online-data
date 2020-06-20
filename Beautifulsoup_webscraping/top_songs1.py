import requests
import urllib.request
from bs4 import BeautifulSoup
import re
from pprint import pprint 

'''url = requests.get("https://gaana.com/songs")
soup = BeautifulSoup(url.text, "html.parser")
tops = soup.find_all('ol',{'class':'content-list'})
print(tops)
#find1=re.search('<ol class="page-group track-list">.+</ol>', soup.text)
#print(find1)'''

url = urllib.request.urlopen("https://www.radiomirchi.com/more/mirchi-top-20/")

soup = BeautifulSoup(url, "html.parser")

tops = soup.find_all('article',{'class':'top01'})

for count,item in enumerate(tops, 1):
    print("Top {} song:\nSong: {}\nMovie:{}\n".format(count,item.find('h2').text,item.find('h3').text))
