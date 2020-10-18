from bs4 import BeautifulSoup
import requests
import lxml
eee_url="https://dee.dongguk.edu/?page_id=553"
eee_res = requests.get(eee_url)
eee_res.raise_for_status()
eee_soup=BeautifulSoup(eee_res.text, 'lxml')
eee_info=eee_soup.find_all(attrs={"class":"kboard-list-uid"})
for i in eee_info:
    print(i.next_sibling.next_sibling.get_text())
#crawling을 할 원하는 url
#ise_url="http://ise.dongguk.edu/bbs/board.php?bo_table=ise6_1"
#ise_res = requests.get(ise_url)
#ise_res.raise_for_status()#혹시나 프로그램에 문제가 있으면 종료를 하도록 함.
#ise_soup = BeautifulSoup(ise_res.text, 'lxml') #ise_soup은 모든 정보를 가지고 있음.
#print(ise_soup.title.get_text())
#print(ise_soup.table) #soup객체에서 처음 발견되는 table element를 출력
#print(ise_soup.body.attrs) #body element 의 속성 정보 출력
#print(ise_soup.body.attrs['topmargin']) #body element의 topmargin의 속성값 정보 출력
#print(ise_soup.find("table",attrs={"class":"member"})) #class = member 인 table element를 찾아줘
#print(ise_soup.find(attrs={"class":"member"}))  #class = member 인 어떤 element 를 찾아줘
#print(ise_soup.find('nobr',attrs={"style":"display:block; overflow:hidden;"}))
#ise_ad1=ise_soup.find(attrs={"bgcolor":'F5F5F5'}).a
#ise_ad2=ise_ad1.next_sibling
#print(ise_ad1.get_text())
#print(ise_ad2.get_text())
#ise_info=ise_soup.form.find_all("a")
#ise_info_list=[ise_info[i] for i in range(len(ise_info))]
#for i in ise_info_list:
#    if 'style' not in str(i):
#        print(i)
#cee_url="https://civil.dongguk.edu/?page_id=269"
#cee_res= requests.get(cee_url)
#cee_res.raise_for_status()
#cee_soup = BeautifulSoup(cee_res.text, 'lxml')
#cee_info=cee_soup.find_all(attrs={"class":"cut_strings"})
#for i in cee_info:
#    print(type(i.a.get_text()))
