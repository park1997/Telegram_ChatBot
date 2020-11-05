from bs4 import BeautifulSoup
import requests
import lxml
mouthpoem_url="https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3654&id=kr_010803000000"
mouthpoem_res=requests.get(mouthpoem_url,verify=False)
mouthpoem_res.raise_for_status()
mouthpoem_soup=BeautifulSoup(mouthpoem_res.text,'lxml')
#mouthpoem_info=mouthpoem_soup.find_all(attrs={"class":"title"})
mouthpoem_info=mouthpoem_soup.find_all(attrs={"class":"title"})
mouthpoem_info_ballground_str=[]
mouthpoem_info_str=[]
for i in mouthpoem_info:
    mouthpoem_info_ballground_str.append(i.get_text().replace('\n',"").replace('\n',""))
del mouthpoem_info_ballground_str[0]
#mouthpoem_info_str=mouthpoem_info_ballground_str[mouthpoem_info_ballground_str.index(mouthpoem_info_ballground_str[0],1,len(mouthpoem_info_ballground_str)):-1]
#mouthpoem_info_ballground_str=mouthpoem_info_ballground_str[0:mouthpoem_info_ballground_str.index(mouthpoem_info_ballground_str[0],1,len(mouthpoem_info_ballground_str))-1]
ballground="공지\n\n"
not_ballground="최신글\n\n"
#for i in mouthpoem_info_str:
#    ballground+=i+"\n"
for j in mouthpoem_info_ballground_str:
    not_ballground+=j+"\n"

print(ballground)
print()
print(not_ballground)
