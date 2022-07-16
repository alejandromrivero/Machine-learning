from bs4 import BeautifulSoup
import html5lib
import requests

page=requests.get("https://www.brainyquote.com/authors/jose_marti")
soup=BeautifulSoup(page.content,'html.parser')
html=list(soup.children)
print (soup.prettify())
#print(page)
#print(html)
