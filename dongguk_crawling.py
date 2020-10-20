from bs4 import BeautifulSoup
import requests
import lxml
normal_url="https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000"
normal_res=requests.get(normal_url,verify=False)
normal_res.raise_for_status()
normal_soup=BeautifulSoup(normal_res.text,'lxml')
#normal_info=normal_soup.find_all(attrs={"class":"title"})
normal_info=normal_soup.find_all(attrs={"class":"title"})
normal_info_ballground_str=[]
normal_info_str=[]
for i in normal_info:
    normal_info_ballground_str.append(i.get_text().replace('\n',"").replace('\n',""))
del normal_info_ballground_str[0]
normal_info_str=normal_info_ballground_str[normal_info_ballground_str.index(normal_info_ballground_str[0],1,len(normal_info_ballground_str)):-1]
normal_info_ballground_str=normal_info_ballground_str[0:normal_info_ballground_str.index(normal_info_ballground_str[0],1,len(normal_info_ballground_str))-1]
ballground="공지\n\n"
not_ballground="최신글\n\n"
for i in normal_info_str:
    ballground+=i+"\n"
for j in normal_info_ballground_str:
    not_ballground+=j+"\n"

print(ballground)
print()
print(not_ballground)
