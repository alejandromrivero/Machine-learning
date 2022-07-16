from bs4 import BeautifulSoup
import requests
html=requests.get("https://en.wikipedia.org/wiki/Ren%C3%A9_Gu%C3%A9non").text
soup=BeautifulSoup(html,'html5lib')
first_paragraph=soup.find_all('p')
#print(first_paragraph)
print (html)