import urllib.request
from bs4 import BeautifulSoup

url = urllib.request.urlopen("https://news.google.com/covid19/map?hl=en-IN&mid=%2Fm%2F049lr&gl=IN&ceid=IN%3Aen")
soup = BeautifulSoup(url, "html.parser")

cases = soup.find_all("tr", {"class":"sgXwHf wdLSAe Iryyw"})
cases_wo=cases[0].find_all("td")

print("COVID-19 in World")
print("Total confirmed cases:",cases_wo[0].text)
print("Cases per 1 million people:",cases_wo[1].text)
print("Total Recovered:",cases_wo[2].text)
print("Total Death:",cases_wo[3].text)
print()

cases_india=cases[1].find_all("td")

print("COVID-19 in India")
print("Total confirmed cases:",cases_india[0].text)
print("Cases per 1 million people:",cases_india[1].text)
print("Total Recovered:",cases_india[2].text)
print("Total Death:",cases_india[3].text)
print()

case = soup.find("tr", {"class":"sgXwHf wdLSAe ROuVee"})
cases_ka=case.find_all("td")

print("COVID-19 in Karnataka")
print("Total confirmed cases:",cases_ka[0].text)
print("Cases per 1 million people:",cases_ka[1].text)
print("Total Recovered:",cases_ka[2].text)
print("Total Death:",cases_ka[3].text)
print()
