import urllib.request
import requests

url1=urllib.request.urlopen("https://ipinfo.io/")
url2=requests.get("https://ipinfo.io/")

print(url1.read().decode())

print(url2.text)
