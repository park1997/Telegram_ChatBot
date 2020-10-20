from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler, ConversationHandler
from emoji import emojize
import requests
from bs4 import BeautifulSoup
import lxml
import json
import datetime
import time
import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction
import pandas as pd

#telegram.ext.Updater : 텔레그램으로부터 업데이트를 받아서 dispatcher로 전달
#CommandHandler: 텔레그램 /start등의 Command
#MessageHandler: 텍스트 상태 업데이트
#CallbackQueryHandler: callback 쿼리


BOT_TOKEN='937755335:AAHsVeoU6isCkDyPY53LFu0quZdWRf88J8Q'   #Py*R**2의 텔레그램 토큰
updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher




def start(update, context):
    task_buttons = [[
        InlineKeyboardButton( '산업시스템공학과', callback_data='ise' )
        , InlineKeyboardButton( '건설환경공학과', callback_data='cee' )
    ],[
        InlineKeyboardButton( '건축공학과', callback_data='gunchuk' )
        , InlineKeyboardButton( '기계로봇에너지공학과', callback_data='mre' )
    ] ,[
        InlineKeyboardButton( '멀티미디어공학과', callback_data='mme' )
        , InlineKeyboardButton( '융합에너지신소재공학과', callback_data='newmeterial' )
    ],[
        InlineKeyboardButton( '전자전기공학부', callback_data='eee' )
        , InlineKeyboardButton( '정보통신공학과', callback_data='ice' )
    ],[
        InlineKeyboardButton( '컴퓨터공학과', callback_data='cse' )
        , InlineKeyboardButton( '화공생명공학과', callback_data='cbe' )
    ],[
        InlineKeyboardButton( '건축학과', callback_data='architec' )
        ,InlineKeyboardButton('추가 기능', callback_data="function")
    ]
     ,[InlineKeyboardButton( '취소', callback_data='cancel' )
    ]]

    reply_markup = InlineKeyboardMarkup( task_buttons )

    context.bot.send_message(
        chat_id=update.message.chat_id
        , text='학과를 선택해주세요.'
        , reply_markup=reply_markup
    )


#callback_query된 애들 여기로 들어감
def major(update, context):
    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id=update.effective_user.id
        , action=ChatAction.TYPING
    )
    print(data)
    if data == 'cancel':
        context.bot.edit_message_text(
            text='작업이 취소되었습니다. 다시 선택하시려면 /start 를클릭해 주세요.'
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id)

    elif data == 'ise':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 산업시스템공학과 이수체계도 -> /ise_toothwatermap\n2. 선 이수과목 조회 -> /ise_mc_the_max_1\n3. 산업공학과 커리어넷 학과정보 -> /ise_career\n4. 학과 공지사항 -> /ise_ballground\n5. 졸업요건 계산기 -> /ise_calculate_1' )
    elif data == 'cee':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 건설환경공학과 이수체계도 -> /cee_toothwatermap\n2. 선 이수과목 조회\n3. 환경공학과 커리어넷 학과정보 -> /cee_career\n4. 학과 공지사항 -> /cee_ballground' )
    elif data == 'gunchuk':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 건축공학과 이수체계도 -> /gunchuk_toothwatermap\n2. 선 이수과목 조회\n3. 건축공학과 커리어넷 학과정보 -> /gunchuk_career\n4. 학과 공지사항 -> /gunchuk_ballground' )
    elif data == 'mre':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 기계로봇에너지공학과 이수체계도 -> /mre_toothwatermap\n2. 선 이수과목 조회\n3. 기계공학과 커리어넷 학과정보 -> /mre_career\n4. 학과 공지사항 -> /mre_ballground' )
    elif data == 'mme':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 멀티미디어공학과 이수체계도 -> /mme_toothwatermap\n2. 선 이수과목 조회\n3. 멀티미디어학과 커리어넷 학과정보 -> /mme_career\n4. 학과 공지사항 -> /mme_ballground' )
    elif data == 'newmeterial':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 융합에너지신소재공학과 이수체계도 -> /newmeterial_toothwatermap\n2. 선 이수과목 조회\n3. 신소재공학과 커리어넷 학과정보 -> /newmeterial_career\n4. 학과 공지사항 -> /newmeterial_ballground' )
    elif data == 'eee':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 전자전기공학부 이수체계도 -> /eee_toothwatermap\n2. 선 이수과목 조회\n3. 전기전자공학과 커리어넷 학과정보 -> /eee_career\n4. 학과 공지사항 -> /eee_ballground' )
    elif data == 'ice':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 정보통신공학과 이수체계도 -> /ice_toothwatermap\n2. 선 이수과목 조회\n3. 정보통신공학과 커리어넷 학과정보 ->  /ice_career\n4. 학과 공지사항 -> /ice_ballground' )
    elif data == 'cse':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 컴퓨터공학과 이수체계도 -> /cse_toothwatermap\n2. 선 이수과목 조회\n3. 컴퓨터공학과 커리어넷 학과정보 -> /cse_career\n4. 학과 공지사항 -> /cse_ballground' )
    elif data == 'cbe':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 화공생명공학과 이수체계도 -> /cbe_toothwatermap\n2. 선 이수과목 조회\n3. 화학공학과 커리어넷 학과정보 -> /cbe_career\n4. 학과 공지사항 -> /cbe_ballground' )
    elif data == 'architec':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 건축학과 이수체계도 -> /architec_toothwatermap\n2. 선 이수과목 조회\n3. 건축학과 커리어넷 학과정보 -> /architec_career\n4. 학과 공지사항 -> /architec_ballground' )
    elif data == "function" :
        context.bot.send_message(chat_id=update.effective_chat.id,
        text="1. 일반공지 -> /normal_ballground\n")


#이수체계도 함수들
def ise_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\산업시스템공학과이수체계도.jpg','rb'))
def cee_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\건설환경공학과이수체계도.jpg','rb'))
def gunchuk_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\건축공학과이수체계도.jpg','rb'))
def mre_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\기계로봇에너지공학과이수체계도.jpg','rb'))
def mme_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\멀티미디어공학과이수체계도.jpg','rb'))
def newmeterial_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\융합에너지신소재공학과이수체계도.jpg','rb'))
def eee_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\전자전기공학부이수체계도.jpg','rb'))
def ice_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\정보통신공학과이수체계도.jpg','rb'))
def cse_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\컴퓨터공학과이수체계도.jpg','rb'))
def cbe_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\화공생명공학과이수체계도.jpg','rb'))
def architec_toothwatermap(update,context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\건축학과이수체계도.jpg','rb'))

#커리어넷 학과정보 링크주기
def ise_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='산업공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=250' )
def cee_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='환경공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=653' )
def gunchuk_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='건축공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=17' )
def mre_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='기계공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=86' )
def mme_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='멀티미디어학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=149' )
def newmeterial_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='신소재공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=324' )
def eee_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='전기전자공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=463' )
def ice_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='정보통신공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=493' )
def cse_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='컴퓨터공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=569' )
def cbe_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='화학공학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=648' )
def architec_career(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
     text ='건축학과의 커리어넷 정보입니다.\n'+'http://mobile.career.go.kr/info/major?seq=20' )

#학과 공지사항
def ise_ballground(update, context):
    #crawling을 할 원하는 url
    print(ise_ballground)
    ise_url="http://ise.dongguk.edu/bbs/board.php?bo_table=ise6_1"
    ise_res = requests.get(ise_url,verify=False) #verify=False 한 이유는 가끔 인증받지못한 싸이트들은 크롤링결과를 빼올수없었음
    ise_text=''
    ise_res.raise_for_status()#혹시나 프로그램에 문제가 있으면 종료를 하도록 함.
    ise_soup = BeautifulSoup(ise_res.text, 'lxml') #ise_soup은 모든 정보를 가지고 있음.
    ise_info=ise_soup.form.find_all("a")
    ise_info_list=[ise_info[i] for i in range(len(ise_info))]
    for i in range(2,len(ise_info_list)):
        if 'style' not in str(ise_info_list[i]):
            ise_text+=ise_info_list[i].get_text()+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,
    text=ise_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
    text='산업시스템공학과 홈페이지는 -> '+'http://ise.dongguk.edu/bbs/board.php?bo_table=ise6_1'+' 입니다.')
def cee_ballground(update,context):
    print(cee_ballground)
    cee_url="https://civil.dongguk.edu/?page_id=269"
    cee_text=''
    cee_res= requests.get(cee_url,verify=False)
    cee_res.raise_for_status()
    cee_soup = BeautifulSoup(cee_res.text, 'lxml')
    cee_info=cee_soup.find_all(attrs={"class":"cut_strings"})
    for i in cee_info:
        cee_text+=i.a.get_text()+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = cee_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '건설환경공학과 홈페이지는 -> '+'https://civil.dongguk.edu/?page_id=269'+' 입니다.')
def gunchuk_ballground(update, context):
    print(gunchuk_ballground)
    gunchuk_url="https://archi.dongguk.edu/?page_id=18387"
    gunchuk_text=''
    gunchuk_res = requests.get(gunchuk_url,verify=False)
    gunchuk_res.raise_for_status()
    gunchuk_soup=BeautifulSoup(gunchuk_res.text, 'lxml')
    gunchuk_info=gunchuk_soup.find_all(attrs={"class":"cut_strings"})
    for i in gunchuk_info:
        gunchuk_text+=i.a.get_text()+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = gunchuk_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '건축공학과 홈페이지는 -> '+gunchuk_text+' 입니다.')
def mre_ballground(update, context):
    print(mre_ballground)
    mre_url="https://mecha.dongguk.edu/?page_id=207"
    mre_text=''
    mre_res = requests.get(mre_url,verify=False)
    mre_res.raise_for_status()
    mre_soup=BeautifulSoup(mre_res.text, 'lxml')
    mre_info=mre_soup.find_all(attrs={"class":"kboard-list-uid"})
    for i in mre_info:
        try:
            if type(int(i.get_text())) is int:
                mre_text+=i.next_sibling.next_sibling.a.get_text()
        except:
            EOFError
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = mre_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '기계로봇에너지공학과 홈페이지는 -> '+mre_url+' 입니다.')
def mme_ballground(update, context):
    print('mme_ballground')
    mme_url="https://mme.dongguk.edu/index.php?CurrentPage=1&module=Board&action=SiteBoard&sMode=SELECT_FORM&iBrdNo=2&sSearchField=&sSearchValue=&brd_title="
    mme_text=''
    mme_res = requests.get(mme_url,verify=False)
    mme_res.raise_for_status()
    mme_soup=BeautifulSoup(mme_res.text, 'lxml')
    mme_info=mme_soup.find_all(attrs={"class":"al"})
    for i in mme_info:
        mme_text+=i.a.get_text()+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = mme_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '멀티미디어공학과 홈페이지는 -> '+mme_url+' 입니다.')
def newmeterial_ballground(update, context):
    print('newmeterial_ballground')
    newmeterial_url="https://me.dongguk.edu/?page_id=218"
    newmeterial_text=''
    newmeterial_res = requests.get(newmeterial_url,verify=False)
    newmeterial_res.raise_for_status()
    newmeterial_soup=BeautifulSoup(newmeterial_res.text, 'lxml')
    newmeterial_info=newmeterial_soup.find_all(attrs={"class":"kboard-list-uid"})
    for i in newmeterial_info:
        try:
            if type(int(i.get_text())) is int:
                newmeterial_text+=i.next_sibling.next_sibling.a.get_text()+"\n"
        except:
            EOFError
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = newmeterial_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '융합에너지신소재공학과 홈페이지는 -> '+newmeterial_url+' 입니다.')
def eee_ballground(update, context):
    print('eee_ballground')
    eee_url="https://dee.dongguk.edu/?page_id=553"
    eee_text=''
    eee_res = requests.get(eee_url,verify=False)
    eee_res.raise_for_status()
    eee_soup=BeautifulSoup(eee_res.text, 'lxml')
    eee_info=eee_soup.find_all(attrs={"class":"kboard-list-uid"})
    for i in range(1,len(eee_info)):
        eee_text+=eee_info[i].next_sibling.next_sibling.get_text()+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = eee_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '전기전자공학부 홈페이지는 -> '+eee_url+' 입니다.')
def ice_ballground(update, context):
    print('ice_ballground')
    ice_url="https://ice.dongguk.edu/?page_id=18518"
    ice_text=''
    ice_res = requests.get(ice_url,verify=False)
    ice_res.raise_for_status()
    ice_soup=BeautifulSoup(ice_res.text, 'lxml')
    ice_info=ice_soup.find_all(attrs={"class":"cut_strings"})
    for i in ice_info:
        ice_text+=i.a.get_text()+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = ice_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '정보통신공학과 홈페이지는 -> '+ice_url+' 입니다.')
def cse_ballground(update, context):
    print('cse_ballground')
    cse_url="https://cse.dongguk.edu/?page_id=799"
    cse_text=''
    cse_res = requests.get(cse_url,verify=False)
    cse_res.raise_for_status()
    cse_soup=BeautifulSoup(cse_res.text, 'lxml')
    cse_info=cse_soup.find_all(attrs={"class":"kboard-list-uid"})
    for i in range(1,len(cse_info)):
        cse_text+=cse_info[i].next_sibling.next_sibling.get_text()+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = cse_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '컴퓨터공학과 홈페이지는 -> '+cse_url+' 입니다.')
def cbe_ballground(update, context):
    print('cbe_ballground')
    cbe_text=''
    cbe_url="https://chembioeng.dongguk.edu/?page_id=207"
    cbe_res= requests.get(cbe_url,verify=False)
    cbe_res.raise_for_status()
    cbe_soup = BeautifulSoup(cbe_res.text, 'lxml')
    cbe_info=cbe_soup.find_all(attrs={"class":"cut_strings"})
    for i in cbe_info:
        cbe_text+=i.a.get_text()+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = cbe_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '화공생명공학과 홈페이지는 -> '+cbe_url+' 입니다.')
def architec_ballground(update, context):
    print('architec_ballground')
    architec_text=''
    architec_url="https://archi.dongguk.edu/?page_id=18387"
    architec_res = requests.get(architec_url,verify=False)
    architec_res.raise_for_status()
    architec_soup=BeautifulSoup(architec_res.text, 'lxml')
    architec_info=architec_soup.find_all(attrs={"class":"cut_strings"})
    for i in architec_info:
        architec_text+=i.a.get_text()+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = architec_text)
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = '건축공학과 홈페이지는 -> '+architec_url+' 입니다.')

#동국대학교 공지사항 crawling
def normal_ballground(update,context):
    print("normal_ballground")
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
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = ballground+"\n"+not_ballground)
    context.bot.send_message(chat_id=update.effective_chat.id,
      text = "일반공지 게시판 ------> https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000")


#text를 읽는 함수 구분!
def ise_mc_the_max_1(update,context):
    update.message.reply_text("과목명을 입력하세요.")
    updater.dispatcher.remove_handler(ise_calculate_handler)
    dispatcher.add_handler(ise_mc_the_max_handler)
    print("ise_mc_the_max_handler")
def ise_calculate_1(update,context):
    updater.dispatcher.remove_handler(ise_mc_the_max_handler)
    updater.dispatcher.add_handler(ise_calculate_handler)
    update.message.reply_text("계산들어갑니다.")
    print('calculate')


#판다스로 선 이수과목 조회하기
def ise_mc_the_max(update,context):
    ise_df = pd.read_csv("D:/Python/project/공대선이수/산시선이수.csv",encoding='CP949')
    ise_df_dic={}
    k=0
    for i in ise_df['후수교과목']:
        ise_df_dic[i]=ise_df['선수교과목'][k]
        k+=1
    print(update.message.text)
    for_strip=update.message.text
    for_strip=''.join(for_strip.split())
    if for_strip in ise_df_dic:
        result=ise_df_dic[for_strip]
        context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 의 선 이수 과목은 \'"+result+"\' 입니다.")
        context.bot.send_message(chat_id=update.effective_chat.id, text="과목명을 입력하세요. 처음으로 돌아가고싶다면 /start 를 누르세요.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 은(는) 선 이수 과목이 없습니다!")
        context.bot.send_message(chat_id=update.effective_chat.id, text="과목명을 입력하세요. 처음으로 돌아가고싶다면 /start 를 누르세요.")
#졸업요건 계산하기
def ise_calculate(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)








# 명령어  /start 정의 CommandHandler
start_handler = CommandHandler( 'start', start )
# 각 학과에 조회가능한 것들이 뭐 있는지에대한 명령어들 제시하는 CallbackQueryHandler
major_callback_handler = CallbackQueryHandler( major )
#각 학과의 이수체계도 명령 CommandHandler
ise_toothwatermap_handler = CommandHandler('ise_toothwatermap',ise_toothwatermap)
cee_toothwatermap_handler = CommandHandler('cee_toothwatermap',cee_toothwatermap)
gunchuk_toothwatermap_handler = CommandHandler('gunchuk_toothwatermap',gunchuk_toothwatermap)
mre_toothwatermap_handler = CommandHandler('mre_toothwatermap',mre_toothwatermap)
mme_toothwatermap_handler = CommandHandler('mme_toothwatermap',mme_toothwatermap)
newmeterial_toothwatermap_handler = CommandHandler('newmeterial_toothwatermap',newmeterial_toothwatermap)
eee_toothwatermap_handler = CommandHandler('eee_toothwatermap',eee_toothwatermap)
ice_toothwatermap_handler = CommandHandler('ice_toothwatermap',ice_toothwatermap)
cse_toothwatermap_handler = CommandHandler('cse_toothwatermap',cse_toothwatermap)
cbe_toothwatermap_handler = CommandHandler('cbe_toothwatermap',cbe_toothwatermap)
architec_toothwatermap_handler = CommandHandler('architec_toothwatermap',architec_toothwatermap)
#각 학과 커리어넷 링크주기 명령 CommandHandler
ise_career_handler = CommandHandler('ise_career',ise_career)
cee_career_handler = CommandHandler('cee_career',cee_career)
gunchuk_career_handler = CommandHandler('gunchuk_career',gunchuk_career)
mre_career_handler = CommandHandler('mre_career',mre_career)
mme_career_handler = CommandHandler('mme_career',mme_career)
newmeterial_career_handler = CommandHandler('newmeterial_career',newmeterial_career)
eee_career_handler = CommandHandler('eee_career',eee_career)
ice_career_handler = CommandHandler('ice_career',ice_career)
cse_career_handler = CommandHandler('cse_career',cse_career)
cbe_career_handler = CommandHandler('cbe_career',cbe_career)
architec_career_handler = CommandHandler('architec_career',architec_career)
#공지사항 crawling
ise_ballground_handler=CommandHandler('ise_ballground',ise_ballground)
cee_ballground_handler=CommandHandler('cee_ballground', cee_ballground)
gunchuk_ballground_handler=CommandHandler('gunchuk_ballground', gunchuk_ballground)
mre_ballground_handler=CommandHandler('mre_ballground', mre_ballground)
mme_ballground_handler=CommandHandler('mme_ballground', mme_ballground)
newmeterial_ballground_handler=CommandHandler('newmeterial_ballground', newmeterial_ballground)
eee_ballground_handler=CommandHandler('eee_ballground', eee_ballground)
ice_ballground_handler=CommandHandler('ice_ballground', ice_ballground)
cse_ballground_handler=CommandHandler('cse_ballground', cse_ballground)
cbe_ballground_handler=CommandHandler('cbe_ballground', cbe_ballground)
architec_ballground_handler=CommandHandler('architec_ballground', architec_ballground)
#동국대 전체공지사항
normal_ballground_handler=CommandHandler('normal_ballground', normal_ballground)





# /start dispatcher
dispatcher.add_handler( start_handler )
# 학과에 조회가능한것들 dispatcher
dispatcher.add_handler( major_callback_handler )
# 각 학과 이수체계도로 접근하는 dispatcher
dispatcher.add_handler(ise_toothwatermap_handler)
dispatcher.add_handler(cee_toothwatermap_handler)
dispatcher.add_handler(gunchuk_toothwatermap_handler)
dispatcher.add_handler(mre_toothwatermap_handler)
dispatcher.add_handler(mme_toothwatermap_handler)
dispatcher.add_handler(newmeterial_toothwatermap_handler)
dispatcher.add_handler(eee_toothwatermap_handler)
dispatcher.add_handler(ice_toothwatermap_handler)
dispatcher.add_handler(cse_toothwatermap_handler)
dispatcher.add_handler(cbe_toothwatermap_handler)
dispatcher.add_handler(architec_toothwatermap_handler)
#각 학과 career net dispatcher
dispatcher.add_handler(ise_career_handler)
dispatcher.add_handler(cee_career_handler)
dispatcher.add_handler(gunchuk_career_handler)
dispatcher.add_handler(mre_career_handler)
dispatcher.add_handler(mme_career_handler)
dispatcher.add_handler(newmeterial_career_handler)
dispatcher.add_handler(eee_career_handler)
dispatcher.add_handler(ice_career_handler)
dispatcher.add_handler(cse_career_handler)
dispatcher.add_handler(cbe_career_handler)
dispatcher.add_handler(architec_career_handler)
#학과 공지사항 crawling dispatcher
dispatcher.add_handler(ise_ballground_handler)
dispatcher.add_handler(cee_ballground_handler)
dispatcher.add_handler(gunchuk_ballground_handler)
dispatcher.add_handler(mre_ballground_handler)
dispatcher.add_handler(mme_ballground_handler)
dispatcher.add_handler(newmeterial_ballground_handler)
dispatcher.add_handler(eee_ballground_handler)
dispatcher.add_handler(ice_ballground_handler)
dispatcher.add_handler(cse_ballground_handler)
dispatcher.add_handler(cbe_ballground_handler)
dispatcher.add_handler(architec_ballground_handler)
#동국대학교 공자사항 crawling dispatcher
dispatcher.add_handler(normal_ballground_handler)


#판다스로 선이수 MessageHandler(MessageHandler는 에코 이므로 맨위에 작성하면 맨위에서 상속 될수 밖에없다)
#따라서 맨 하위에 놔서 어떠한 명령어도 없을 경우에 message_handler를 실행한다.
ise_mc_the_max_1_handler=CommandHandler('ise_mc_the_max_1',ise_mc_the_max_1)
dispatcher.add_handler(ise_mc_the_max_1_handler)
#졸업요건 MessageHandler
ise_calculate_1_handler=CommandHandler('ise_calculate_1',ise_calculate_1)
dispatcher.add_handler(ise_calculate_1_handler)
ise_mc_the_max_handler = MessageHandler(Filters.text,ise_mc_the_max)
#dispatcher.add_handler(ise_mc_the_max_handler)
ise_calculate_handler=MessageHandler(Filters.text,ise_calculate)
#dispatcher.add_handler(ise_calculate_handler)

print('end')
#주기적으로 텔레그램 접속 새로운메세지가 있으면 받아온다.
updater.start_polling()
updater.idle()
