from bs4 import BeautifulSoup
import requests
import lxml
library_url="http://lib.dongguk.edu/"
library_res = requests.get(library_url)
library_res.raise_for_status()
library_soup=BeautifulSoup(library_res.text, 'lxml')
library_info=library_soup.find(attrs={"class":"contents2","class":"readingR"})
print(library_info)
