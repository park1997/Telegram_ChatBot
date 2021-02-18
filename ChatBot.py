from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler, ConversationHandler
import requests
from bs4 import BeautifulSoup
import lxml
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
            text='작업이 취소되었습니다. 다시 선택하시려면 /start 를 클릭해 주세요.'
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id)

    elif data == 'ise':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 산업시스템공학과 이수체계도,졸업기준표\n-> /ise_toothwatermap\n2. 산업공학과 커리어넷 학과정보\n-> /ise_career\n3. 학과 공지사항\n-> /ise_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1\n6. 졸업학점 계산기\n-> /ise_graduate_1' )
    elif data == 'cee':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 건설환경공학과 이수체계도\n-> /cee_toothwatermap\n2. 환경공학과 커리어넷 학과정보\n-> /cee_career\n3. 학과 공지사항\n-> /cee_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == 'gunchuk':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 건축공학과 이수체계도\n-> /gunchuk_toothwatermap\n2. 건축공학과 커리어넷 학과정보\n-> /gunchuk_career\n3. 학과 공지사항\n-> /gunchuk_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == 'mre':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 기계로봇에너지공학과 이수체계도\n-> /mre_toothwatermap\n2. 기계공학과 커리어넷 학과정보\n-> /mre_career\n3. 학과 공지사항\n-> /mre_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == 'mme':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 멀티미디어공학과 이수체계도\n-> /mme_toothwatermap\n2. 멀티미디어학과 커리어넷 학과정보\n-> /mme_career\n3. 학과 공지사항\n-> /mme_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == 'newmeterial':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 융합에너지신소재공학과 이수체계도\n-> /newmeterial_toothwatermap\n2. 신소재공학과 커리어넷 학과정보\n-> /newmeterial_career\n3. 학과 공지사항\n-> /newmeterial_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == 'eee':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 전자전기공학부 이수체계도\n-> /eee_toothwatermap\n2. 전기전자공학과 커리어넷 학과정보\n-> /eee_career\n3. 학과 공지사항\n-> /eee_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == 'ice':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 정보통신공학과 이수체계도\n-> /ice_toothwatermap\n2. 정보통신공학과 커리어넷 학과정보\n->  /ice_career\n3. 학과 공지사항\n-> /ice_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1')
    elif data == 'cse':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 컴퓨터공학과 이수체계도\n-> /cse_toothwatermap\n2. 컴퓨터공학과 커리어넷 학과정보\n-> /cse_career\n3. 학과 공지사항\n-> /cse_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == 'cbe':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 화공생명공학과 이수체계도\n-> /cbe_toothwatermap\n2. 화학공학과 커리어넷 학과정보\n-> /cbe_career\n3 학과 공지사항\n-> /cbe_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == 'architec':
        context.bot.send_message(chat_id=update.effective_chat.id,
         text ='1. 건축학과 이수체계도\n-> /architec_toothwatermap\n2. 건축학과 커리어넷 학과정보\n-> /architec_career\n3. 학과 공지사항\n-> /architec_ballground\n4. 선 이수과목 조회\n-> /mc_the_max_1\n5. 과목정보 조회\n-> /info_1' )
    elif data == "function" :
        context.bot.send_message(chat_id=update.effective_chat.id,
        text="1. 일반공지\n-> /normal_ballground\n2. 학사공지\n-> /haksa_ballground\n3. 입시 공지\n-> /mouthpoem_ballground\n4. 장학 공지\n-> /scholarship_ballground\n5. 국제 공지\n-> /international_ballground\n6. 학술/행사 공지\n-> /event_ballground")

#이수체계도 함수들
def ise_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/산업시스템공학과이수체계도.jpg','rb'))
    update.message.reply_text("↓일반과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/산시졸업기준표_일반과정.jpg','rb'))
    update.message.reply_text("↓심화과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/산시졸업기준표_심화과정.jpg','rb'))
def cee_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/건설환경공학과이수체계도.jpg','rb'))
    update.message.reply_text("↓일반과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/건환졸업기준표_일반과정.jpg','rb'))
    update.message.reply_text("↓심화과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/건환졸업기준표_심화과정.jpg','rb'))
def gunchuk_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/건축공학과이수체계도.jpg','rb'))
    update.message.reply_text("↓일반과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/졸업기준표/건공졸업기준표_일반과정.jpg','rb'))
    update.message.reply_text("↓심화과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/졸업기준표/건공졸업기준표_심화과정.jpg','rb'))
def mre_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/기계로봇에너지공학과이수체계도.jpg','rb'))
    update.message.reply_text("↓일반과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/졸업기준표/기계졸업기준표_일반과정.jpg','rb'))
    update.message.reply_text("↓심화과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/졸업기준표/기계졸업기준표_심화과정.jpg','rb'))
def mme_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/멀티미디어공학과이수체계도.jpg','rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/졸업기준표/멀공졸업기준표.jpg','rb'))
def newmeterial_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/융합에너지신소재공학과이수체계도.jpg','rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/융신졸업기준표.jpg','rb'))
def eee_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/전자전기공학부이수체계도.jpg','rb'))
    update.message.reply_text("↓일반과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/전전졸업기준표_일반과정.jpg','rb'))
    update.message.reply_text("↓심화과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/전전졸업기준표_심화과정.jpg','rb'))
def ice_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/정보통신공학과이수체계도.jpg','rb'))
    update.message.reply_text("↓일반과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/정통졸업기준표_일반과정.jpg','rb'))
    update.message.reply_text("↓심화과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/정통졸업기준표_심화과정.jpg','rb'))
def cse_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/컴퓨터공학과이수체계도.jpg','rb'))
    update.message.reply_text("↓일반과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/컴공졸업기준표_일반과정.jpg','rb'))
    update.message.reply_text("↓심화과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/컴공졸업기준표_심화과정.jpg','rb'))
def cbe_toothwatermap(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/화공생명공학과이수체계도.jpg','rb'))
    update.message.reply_text("↓일반과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/화공졸업기준표_일반과정.jpg','rb'))
    update.message.reply_text("↓심화과정↓")
    context.bot.send_photo(chat_id=update.effective_chat.id ,photo=open('D:/Python/Telegram_ChatBot/졸업기준표/화공졸업기준표_심화과정.jpg','rb'))
def architec_toothwatermap(update,context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/공대 이수체계도/공대 이수체계도/건축학과이수체계도.jpg','rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:/Python/Telegram_ChatBot/졸업기준표/건축학졸업기준표.jpg','rb'))

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
    print("ise_ballground")
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
    print("cee_ballground")
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
    print("gunchuk_ballground")
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
     text = '건축공학과 홈페이지는 -> '+gunchuk_url+' 입니다.')
def mre_ballground(update, context):
    print("mre_ballground")
    mre_url="https://mecha.dongguk.edu/?page_id=207"
    mre_text=''
    mre_res = requests.get(mre_url,verify=False)
    mre_res.raise_for_status()
    mre_soup=BeautifulSoup(mre_res.text, 'lxml')
    mre_info=mre_soup.find_all(attrs={"class":"kboard-list-uid"})
    for i in mre_info:
        try:
            if type(int(i.get_text())) is int:
                mre_text+=i.next_sibling.next_sibling.a.get_text()+"\n"
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
    ballground="< 공지 >\n\n"
    not_ballground="< 최신글 >\n\n"
    for i in normal_info_str:
        ballground+=i+"\n"
    for j in normal_info_ballground_str:
        not_ballground+=j+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = ballground+"\n"+not_ballground)
    context.bot.send_message(chat_id=update.effective_chat.id,
      text = "일반공지 게시판 ------> https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000")
def haksa_ballground(update,context):
    print("haksa_ballground")
    haksa_url="https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&id=kr_010801000000"
    haksa_res=requests.get(haksa_url,verify=False)
    haksa_res.raise_for_status()
    haksa_soup=BeautifulSoup(haksa_res.text,'lxml')
    #haksa_info=haksa_soup.find_all(attrs={"class":"title"})
    haksa_info=haksa_soup.find_all(attrs={"class":"title"})
    haksa_info_ballground_str=[]
    haksa_info_str=[]
    for i in haksa_info:
        haksa_info_ballground_str.append(i.get_text().replace('\n',"").replace('\n',""))
    del haksa_info_ballground_str[0]
    haksa_info_str=haksa_info_ballground_str[haksa_info_ballground_str.index(haksa_info_ballground_str[0],1,len(haksa_info_ballground_str)):-1]
    haksa_info_ballground_str=haksa_info_ballground_str[0:haksa_info_ballground_str.index(haksa_info_ballground_str[0],1,len(haksa_info_ballground_str))-1]
    ballground="< 공지 >\n\n"
    not_ballground="< 최신글 >\n\n"
    for i in haksa_info_str:
        ballground+=i+"\n"
    for j in haksa_info_ballground_str:
        not_ballground+=j+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = ballground+"\n"+not_ballground)
    context.bot.send_message(chat_id=update.effective_chat.id,
      text = "학사공지 게시판 ------> https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&id=kr_010801000000")
def mouthpoem_ballground(update,context):
    print("mouthpoem_ballground")
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
    ballground="< 공지 >\n\n"
    not_ballground="< 최신글 >\n\n"
    for i in mouthpoem_info_str:
        ballground+=i+"\n"
    for j in mouthpoem_info_ballground_str:
        not_ballground+=j+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = ballground+"\n"+not_ballground)
    context.bot.send_message(chat_id=update.effective_chat.id,
      text = "입시공지 게시판 ------> https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3654&id=kr_010803000000")
def scholarship_ballground(update,context):
    print("scholarship_ballground")
    scholarship_url="https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3662&id=kr_010804000000"
    scholarship_res=requests.get(scholarship_url,verify=False)
    scholarship_res.raise_for_status()
    scholarship_soup=BeautifulSoup(scholarship_res.text,'lxml')
    #scholarship_info=scholarship_soup.find_all(attrs={"class":"title"})
    scholarship_info=scholarship_soup.find_all(attrs={"class":"title"})
    scholarship_info_ballground_str=[]
    scholarship_info_str=[]
    for i in scholarship_info:
        scholarship_info_ballground_str.append(i.get_text().replace('\n',"").replace('\n',""))
    del scholarship_info_ballground_str[0]
    scholarship_info_str=scholarship_info_ballground_str[scholarship_info_ballground_str.index(scholarship_info_ballground_str[0],1,len(scholarship_info_ballground_str)):-1]
    scholarship_info_ballground_str=scholarship_info_ballground_str[0:scholarship_info_ballground_str.index(scholarship_info_ballground_str[0],1,len(scholarship_info_ballground_str))-1]
    ballground="< 공지 >\n\n"
    not_ballground="< 최신글 >\n\n"
    for i in scholarship_info_str:
        ballground+=i+"\n"
    for j in scholarship_info_ballground_str:
        not_ballground+=j+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = ballground+"\n"+not_ballground)
    context.bot.send_message(chat_id=update.effective_chat.id,
      text = "장학공지 게시판 ------> https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3662&id=kr_010804000000")
def international_ballground(update,context):
    print("international_ballground")
    international_url="https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=9457435&id=kr_010807000000"
    international_res=requests.get(international_url,verify=False)
    international_res.raise_for_status()
    international_soup=BeautifulSoup(international_res.text,'lxml')
    #international_info=international_soup.find_all(attrs={"class":"title"})
    international_info=international_soup.find_all(attrs={"class":"title"})
    international_info_ballground_str=[]
    international_info_str=[]
    for i in international_info:
        international_info_ballground_str.append(i.get_text().replace('\n',"").replace('\n',""))
    del international_info_ballground_str[0]
    international_info_str=international_info_ballground_str[international_info_ballground_str.index(international_info_ballground_str[0],1,len(international_info_ballground_str)):-1]
    international_info_ballground_str=international_info_ballground_str[0:international_info_ballground_str.index(international_info_ballground_str[0],1,len(international_info_ballground_str))-1]
    ballground="< 공지 >\n\n"
    not_ballground="< 최신글 >\n\n"
    for i in international_info_str:
        ballground+=i+"\n"
    for j in international_info_ballground_str:
        not_ballground+=j+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = ballground+"\n"+not_ballground)
    context.bot.send_message(chat_id=update.effective_chat.id,
      text = "국제공지 게시판 ------> https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=9457435&id=kr_010807000000")
def event_ballground(update,context):
    event_url="https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=11533472&id=kr_010808000000"
    event_res=requests.get(event_url,verify=False)
    event_res.raise_for_status()
    event_soup=BeautifulSoup(event_res.text,'lxml')
    #event_info=event_soup.find_all(attrs={"class":"title"})
    event_info=event_soup.find_all(attrs={"class":"title"})
    event_info_ballground_str=[]
    event_info_str=[]
    for i in event_info:
        event_info_ballground_str.append(i.get_text().replace('\n',"").replace('\n',""))
    del event_info_ballground_str[0]
    event_info_str=event_info_ballground_str[event_info_ballground_str.index(event_info_ballground_str[0],1,len(event_info_ballground_str)):-1]
    event_info_ballground_str=event_info_ballground_str[0:event_info_ballground_str.index(event_info_ballground_str[0],1,len(event_info_ballground_str))-1]
    ballground="< 공지 >\n\n"
    not_ballground="< 최신글 >\n\n"
    for i in event_info_str:
        ballground+=i+"\n"
    for j in event_info_ballground_str:
        not_ballground+=j+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id,
     text = ballground+"\n"+not_ballground)
    context.bot.send_message(chat_id=update.effective_chat.id,
      text = "학술/행사 공지 게시판 ------> https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=11533472&id=kr_010808000000")

#text를 읽는 함수 구분! MessageHandler의 삭제와 추가를 담당함
#공대선이수
def mc_the_max_1(update,context):
    updater.dispatcher.remove_handler(info_handler)
    updater.dispatcher.remove_handler(ise_graduate_handler)
    updater.dispatcher.add_handler(mc_the_max_handler)
    print("mc_the_max_handler_1")
    update.message.reply_text("과목명을 입력하세요.")
#과목정보 조회
def info_1(update,context):
    updater.dispatcher.remove_handler(mc_the_max_handler)
    updater.dispatcher.remove_handler(ise_graduate_handler)
    updater.dispatcher.add_handler(info_handler)
    update.message.reply_text("과목명을 입력해주세요.")
    print('info_1')
#졸업학점 계산기
def ise_graduate_1(update,context):
    updater.dispatcher.remove_handler(mc_the_max_handler)
    updater.dispatcher.remove_handler(info_handler)
    updater.dispatcher.add_handler(ise_graduate_handler)
    context.bot.send_message(chat_id=update.effective_chat.id, text='다음 양식에 맞게 수강한 과목을 입력하세요.\n\nEX1) 단일전공인 경우(";"로 구분하여 수강한 과목 입력)\n인간공학;응용통계학;자아와명상1\n\nEX2) 복수(연계)전공인 경우(";" 로 구분하여 연계전공과 과목 입력)\n융합소프트웨어;인간공학;응용통계학;자아와명상1\n\n'+'< 필 독!! >\n(현장실습, 개별연구)는 학점 계산에 포함되지 않습니다. ')
    print("ise_graduate_1")
#판다스로 선 이수과목 조회하기
def mc_the_max(update,context):
    ise_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/산시선이수.xlsx")
    cee_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/건설환경공학선이수.xlsx")
    mre_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/기계공학선이수.xlsx")
    mme_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/멀티미디어선이수.xlsx")
    ice_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/정보통신공학선이수.xlsx")
    cse_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/컴퓨터공학선이수.xlsx")
    cbe_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/화생공선이수.xlsx")
    eee_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/전자전기공학선이수.xlsx")
    gunchuk_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/건축공학선이수.xlsx")
    architec_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/건축학선이수.xlsx")
    newmeterial_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/융에신선이수.xlsx")
    df_dic={}
    k=0
    for i in ise_df['후수교과목']:
        df_dic[i]=ise_df['선수교과목'][k]
        k+=1
    k=0
    for i in cee_df["후수교과목"]:
        df_dic[i]=cee_df['선수교과목'][k]
        k+=1
    k=0
    for i in mre_df["후수교과목"]:
        df_dic[i]=mre_df["선수교과목"][k]
        k+=1
    k=0
    for i in mme_df["후수교과목"]:
        df_dic[i]=mme_df["선수교과목"][k]
        k+=1
    k=0
    for i in ice_df["후수교과목"]:
        df_dic[i]=ice_df["선수교과목"][k]
        k+=1
    k=0
    for i in cse_df["후수교과목"]:
        df_dic[i]=cse_df["선수교과목"][k]
        k+=1
    k=0
    for i in cbe_df["후수교과목"]:
        df_dic[i]=cbe_df["선수교과목"][k]
        k+=1
    k=0
    for i in gunchuk_df["후수교과목"]:
        df_dic[i]=gunchuk_df["선수교과목"][k]
        k+=1
    k=0
    for i in architec_df["후수교과목"]:
        df_dic[i]=architec_df["선수교과목"][k]
        k+=1
    k=0
    for i in eee_df["후수교과목"]:
        df_dic[i]=eee_df["선수교과목"][k]
        k+=1
    k=0
    for i in newmeterial_df["후수교과목"]:
        df_dic[i]=newmeterial_df["선수교과목"][k]
        k+=1
    print(update.message.text)
    for_strip=update.message.text
    for_strip=''.join(for_strip.split())
    if for_strip in df_dic:
        result=df_dic[for_strip]
        context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 의 선 이수 과목은 \'"+result+"\' 입니다.")
        context.bot.send_message(chat_id=update.effective_chat.id, text="과목명을 입력하세요. 처음으로 돌아가고싶다면 /start 를 누르세요.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 은(는) 선 이수 과목이 없습니다!")
        context.bot.send_message(chat_id=update.effective_chat.id, text="과목명을 입력하세요. 처음으로 돌아가고싶다면 /start 를 누르세요.")

#과목 정보 조회하기
def info(update,context):
    ise_df = pd.read_excel("과목 및 학점구분.xlsx",sheet_name='Sheet1')
    ise_df_선택필수 = pd.read_excel("과목 및 학점구분.xlsx",sheet_name='선택필수')
    ise_df_전공필수 = pd.read_excel("과목 및 학점구분.xlsx",sheet_name='전공필수')
    ise_df_전공전문 = pd.read_excel("과목 및 학점구분.xlsx",sheet_name='전공전문')
    ise_df_전공기초 = pd.read_excel("과목 및 학점구분.xlsx",sheet_name='전공기초')
    ise_df_MSC = pd.read_excel("과목 및 학점구분.xlsx",sheet_name='MSC')
    ise_df_기본소양 = pd.read_excel("과목 및 학점구분.xlsx",sheet_name='기본소양')

    ise_df_choose = list(map(str,ise_df['선택필수']))
    ise_df_must = list(map(str,ise_df['전공필수']))
    ise_df_pro = list(map(str,ise_df['전공전문']))
    ise_df_base = list(map(str,ise_df['전공기초']))
    ise_df_MSC = list(map(str,ise_df['MSC']))
    ise_df_cow_sheep = list(map(str,ise_df['기본소양']))

    print(update.message.text)
    for_strip=update.message.text
    for_strip=''.join(for_strip.split())
    printlist=[]
    printlist_1=[]
    if for_strip in ise_df_choose:
        result='선택필수'
        printlist.append(ise_df[['선택필수학점']].iloc[ise_df_choose.index(for_strip)])
        printlist_1.append(result)
    if for_strip in ise_df_must:
        result='전공필수'
        printlist.append(ise_df[['전공필수학점']].iloc[ise_df_must.index(for_strip)])
        printlist_1.append(result)
    if for_strip in ise_df_pro:
        result='전공전문'
        printlist.append(ise_df[['전공전문학점']].iloc[ise_df_pro.index(for_strip)])
        printlist_1.append(result)
    if for_strip in ise_df_base:
        result='전공기초'
        printlist.append(ise_df[['전공기초학점']].iloc[ise_df_base.index(for_strip)])
        printlist_1.append(result)
    if for_strip in ise_df_MSC:
        result='MSC'
        printlist.append(ise_df[['MSC학점']].iloc[ise_df_MSC.index(for_strip)])
        printlist_1.append(result)
    if for_strip in ise_df_cow_sheep:
        result='기본소양'
        printlist.append(ise_df[['기본소양학점']].iloc[ise_df_cow_sheep.index(for_strip)])
        printlist_1.append(result)
    print(printlist)
    result=""
    for i in printlist_1:
        result+=i+" "
    if len(printlist)==0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="\""+update.message.text+"\"  과목명을 확인후 다시 입력해 주세요.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text+' : '+result+'\t학점 : '+str(float(printlist[0][0])))
        if update.message.text=="머신러닝":
            context.bot.send_message(chat_id=update.effective_chat.id, text="(정보통신공학과 에서는 \"머신러닝\"이 전공전문 입니다. )")

#졸업학점 계산하기
def ise_graduate(update,context):
    print(update.message.text)
    for_strip=update.message.text
    for_strip_list=list(map(str,for_strip.split(';')))
    for i in range(len(for_strip_list)):
        for_strip_list[i]=''.join(for_strip_list[i].split())
    print(for_strip_list)
    df = pd.read_excel('졸업요건_산시.xlsx')
    #사용자가 오타로 입력한 과목명을 걸러내기
    five_ride=''
    column_data=[]
    column_data_list=[]
    for_set=[]
    for i in df:
        column_data.append(list(set(list(map(str,df[i])))))
    for i in column_data:
        for _ in i:
            column_data_list.append(_)
    for i in for_strip_list:
        if i not in column_data_list:
            for_set.append(i)
    for_set=list(set(for_set))
    for i in for_set:
        five_ride+=i+','
    five_ride=five_ride.replace(five_ride,five_ride[0:len(five_ride)-1])

    산업시스템공학과선택필수=list(map(str,df['산업시스템공학과선택필수']))
    산업시스템공학과선택필수학점=0
    산업시스템공학과전공필수=list(map(str,df['산업시스템공학과전공필수']))
    산업시스템공학과전공필수학점=0
    산업시스템공학과전공기초=list(map(str,df['산업시스템공학과전공기초']))
    산업시스템공학과전공기초학점=0
    산업시스템공학과전공전문=list(map(str,df['산업시스템공학과전공전문']))
    산업시스템공학과전공전문학점=0
    산업시스템공학과MSC=list(map(str,df['산업시스템공학과MSC']))
    산업시스템공학과MSC학점=0
    산업시스템공학과기본소양=list(map(str,df['산업시스템공학과기본소양']))
    산업시스템공학과기본소양학점=0
    산업시스템공학과기초교양=list(map(str,df['산업시스템공학과기초교양']))
    산업시스템공학과기초교양학점=0
    융합소프트웨어전공필수=list(map(str,df['융합소프트웨어전공필수']))
    융합소프트웨어전공필수학점=0
    융합소프트웨어전공선택=list(map(str,df['융합소프트웨어전공선택']))
    융합소프트웨어전공선택학점=0
    디자인공학전공기초=list(map(str,df['디자인공학전공기초']))
    디자인공학전공기초학점=0
    디자인공학전공전문=list(map(str,df['디자인공학전공전문']))
    디자인공학전공전문학점=0
    건설정보소프트웨어필수=list(map(str,df['건설정보소프트웨어필수']))
    건설정보소프트웨어필수학점=0
    건설정보전공선택=list(map(str,df['건설정보전공선택']))
    건설정보전공선택학점=0
    로봇융합전공필수=list(map(str,df['로봇융합전공필수']))
    로봇융합전공필수학점=0
    로봇융합전공선택=list(map(str,df['로봇융합전공선택']))
    로봇융합전공선택학점=0
    로봇융합소프트웨어전필수=list(map(str,df['로봇융합소프트웨어전필수']))
    로봇융합소프트웨어전학점=0
    로봇융합소프트웨어선택=list(map(str,df['로봇융합소프트웨어선택']))
    로봇융합소프트웨어선택학점=0
    문화예술전공필수=list(map(str,df['문화예술전공필수']))
    문화예술전공필수학점=0
    문화예술전공선택=list(map(str,df['문화예술전공선택']))
    문화예술전공선택학점=0
    문화예술소프트웨어선택=list(map(str,df['문화예술소프트웨어선택']))
    문화예술소프트웨어선택학점=0
    범죄수사전공필수=list(map(str,df['범죄수사전공필수']))
    범죄수사전공필수학점=0
    범죄수사전공선택=list(map(str,df['범죄수사전공선택']))
    범죄수사전공선택학점=0
    범죄수사전공선택필수=list(map(str,df['범죄수사전공선택필수']))
    범죄수사전공선택필수학점=0
    범죄수사소프트웨어선택=list(map(str,df['범죄수사소프트웨어선택']))
    범죄수사소프트웨어선택학점=0
    산업정보전공선택=list(map(str,df['산업정보전공선택']))
    산업정보전공선택학점=0
    산업정보소프트웨어필수=list(map(str,df['산업정보소프트웨어필수']))
    산업정보소프트웨어필수학점=0
    산업정보소프트웨어선택=list(map(str,df['산업정보소프트웨어선택']))
    산업정보소프트웨어선택학점=0
    산업정보전공필수=list(map(str,df['산업정보전공필수']))
    산업정보전공필수학점=0
    산업정보전공선택=list(map(str,df['산업정보전공선택']))
    산업정보전공선택학점=0
    산업정보소프트웨어필수=list(map(str,df['산업정보소프트웨어필수']))
    산업정보소프트웨어필수학점=0
    산업정보소프트웨어선택=list(map(str,df['산업정보소프트웨어선택']))
    산업정보소프트웨어선택학점=0
    산시전공=0
    if for_strip_list[0]=='융합소프트웨어':
        del for_strip_list[0]
        for_strip_list=list(set(for_strip_list))
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과전공기초학점+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 산업시스템공학과기초교양:
                산업시스템공학과기초교양학점+=int(df[['산업시스템공학과기초교양학점']].iloc[산업시스템공학과기초교양.index(i)])
            if i in 융합소프트웨어전공필수:
                융합소프트웨어전공필수학점+=int(df[['융합소프트웨어전공필수학점']].iloc[융합소프트웨어전공필수.index(i)])
            if i in 융합소프트웨어전공선택:
                융합소프트웨어전공선택학점+=int(df[['융합소프트웨어전공선택학점']].iloc[융합소프트웨어전공선택.index(i)])
        산시전공=산업시스템공학과전공기초학점+산업시스템공학과전공전문학점
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/12\n'+'산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/24\n'+'( 18년도 이전 입학생 : 21학점 )\n'+'산업시스템공학과전공 : '+str(산시전공)+'/36\n'+'산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/18학점 이상\n'+'MSC : '+str(산업시스템공학과MSC학점)+'/30\n'+'기본소양 : '+str(산업시스템공학과기본소양학점)+'/6\n'+'기초교양 : '+str(산업시스템공학과기초교양학점)+'/16\n'+'융합소프트웨어전공 : '+str(융합소프트웨어전공필수학점+융합소프트웨어전공선택학점)+'/36')

    elif for_strip_list[0]=='디자인공학':
        del for_strip_list[0]
        for_strip_list=list(set(for_strip_list))
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과전공기초학점+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 산업시스템공학과기초교양:
                산업시스템공학과기초교양학점+=int(df[['산업시스템공학과기초교양학점']].iloc[산업시스템공학과기초교양.index(i)])
            if i in 융합소프트웨어전공필수:
                융합소프트웨어전공필수학점+=int(df[['디자인공학전공필수학점']].iloc[디자인공학전공필수.index(i)])
            if i in 융합소프트웨어전공선택:
                융합소프트웨어전공선택학점+=int(df[['디자인공학전공선택학점']].iloc[디자인공학전공선택.index(i)])
        산시전공=산업시스템공학과전공기초학점+산업시스템공학과전공전문학점
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/12\n'+'산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/24\n'+'( 18년도 이전 입학생 : 21학점 )\n'+'산업시스템공학과전공 : '+str(산시전공)+'/36\n'+'산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/18학점 이상\n'+'MSC : '+str(산업시스템공학과MSC학점)+'/30\n'+'기본소양 : '+str(산업시스템공학과기본소양학점)+'/6\n'+'기초교양 : '+str(산업시스템공학과기초교양학점)+'/16\n'+'디자인공학전공 : '+str(디자인공학전공필수학점+디자인공학전공선택학점)+'/36')

    elif for_strip_list[0]=='건설정보소프트웨어':
        del for_strip_list[0]
        for_strip_list=list(set(for_strip_list))
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과전공기초학점+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 산업시스템공학과기초교양:
                산업시스템공학과기초교양학점+=int(df[['산업시스템공학과기초교양학점']].iloc[산업시스템공학과기초교양.index(i)])
            if i in 융합소프트웨어전공필수:
                융합소프트웨어전공필수학점+=int(df[['건설정보소프트웨어전공필수학점']].iloc[건설정보소프트웨어전공필수.index(i)])
            if i in 융합소프트웨어전공선택:
                융합소프트웨어전공선택학점+=int(df[['건설정보소프트웨어전공선택학점']].iloc[건설정보소프트웨어전공선택.index(i)])
        산시전공=산업시스템공학과전공기초학점+산업시스템공학과전공전문학점
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/12\n'+'산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/24\n'+'( 18년도 이전 입학생 : 21학점 )\n'+'산업시스템공학과전공 : '+str(산시전공)+'/36\n'+'산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/18학점 이상\n'+'MSC : '+str(산업시스템공학과MSC학점)+'/30\n'+'기본소양 : '+str(산업시스템공학과기본소양학점)+'/6\n'+'기초교양 : '+str(산업시스템공학과기초교양학점)+'/16\n'+'건설정보소프트웨어전공 : '+str(건설정보소프트웨어전공필수학점+건설정보소프트웨어전공선택학점)+'/36')

    elif for_strip_list[0]=='로봇융합소프트웨어':
        del for_strip_list[0]
        for_strip_list=list(set(for_strip_list))
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과전공기초학점+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 산업시스템공학과기초교양:
                산업시스템공학과기초교양학점+=int(df[['산업시스템공학과기초교양학점']].iloc[산업시스템공학과기초교양.index(i)])
            if i in 융합소프트웨어전공필수:
                융합소프트웨어전공필수학점+=int(df[['로봇융합소프트웨어전공필수학점']].iloc[로봇융합소프트웨어전공필수.index(i)])
            if i in 융합소프트웨어전공선택:
                융합소프트웨어전공선택학점+=int(df[['로봇융합소프트웨어전공선택학점']].iloc[로봇융합소프트웨어전공선택.index(i)])
        산시전공=산업시스템공학과전공기초학점+산업시스템공학과전공전문학점
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/12\n'+'산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/24\n'+'( 18년도 이전 입학생 : 21학점 )\n'+'산업시스템공학과전공 : '+str(산시전공)+'/36\n'+'산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/18학점 이상\n'+'MSC : '+str(산업시스템공학과MSC학점)+'/30\n'+'기본소양 : '+str(산업시스템공학과기본소양학점)+'/6\n'+'기초교양 : '+str(산업시스템공학과기초교양학점)+'/16\n'+'로봇융합소프트웨어전공 : '+str(로봇융합소프트웨어전공필수학점+로봇융합소프트웨어전공선택학점)+'/36')
    elif for_strip_list[0]=='문화예술소프트웨어':
        del for_strip_list[0]
        for_strip_list=list(set(for_strip_list))
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과전공기초학점+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 산업시스템공학과기초교양:
                산업시스템공학과기초교양학점+=int(df[['산업시스템공학과기초교양학점']].iloc[산업시스템공학과기초교양.index(i)])
            if i in 융합소프트웨어전공필수:
                융합소프트웨어전공필수학점+=int(df[['문화예술소프트웨어전공필수학점']].iloc[문화예술소프트웨어전공필수.index(i)])
            if i in 융합소프트웨어전공선택:
                융합소프트웨어전공선택학점+=int(df[['문화예술소프트웨어전공선택학점']].iloc[문화예술소프트웨어전공선택.index(i)])
        산시전공=산업시스템공학과전공기초학점+산업시스템공학과전공전문학점
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/12\n'+'산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/24\n'+'( 18년도 이전 입학생 : 21학점 )\n'+'산업시스템공학과전공 : '+str(산시전공)+'/36\n'+'산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/18학점 이상\n'+'MSC : '+str(산업시스템공학과MSC학점)+'/30\n'+'기본소양 : '+str(산업시스템공학과기본소양학점)+'/6\n'+'기초교양 : '+str(산업시스템공학과기초교양학점)+'/16\n'+'융합소프트웨어전공 : '+str(문화예술소프트웨어전공필수학점+문화예술소프트웨어전공선택학점)+'/36')
    elif for_strip_list[0]=='범죄수사소프트웨어':
        del for_strip_list[0]
        for_strip_list=list(set(for_strip_list))
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과전공기초학점+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 산업시스템공학과기초교양:
                산업시스템공학과기초교양학점+=int(df[['산업시스템공학과기초교양학점']].iloc[산업시스템공학과기초교양.index(i)])
            if i in 융합소프트웨어전공필수:
                융합소프트웨어전공필수학점+=int(df[['범죄수사소프트웨어전공필수학점']].iloc[범죄수사소프트웨어전공필수.index(i)])
            if i in 융합소프트웨어전공선택:
                융합소프트웨어전공선택학점+=int(df[['범죄수사소프트웨어전공선택학점']].iloc[범죄수사소프트웨어전공선택.index(i)])
        산시전공=산업시스템공학과전공기초학점+산업시스템공학과전공전문학점
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/12\n'+'산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/24\n'+'( 18년도 이전 입학생 : 21학점 )\n'+'산업시스템공학과전공 : '+str(산시전공)+'/36\n'+'산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/18학점 이상\n'+'MSC : '+str(산업시스템공학과MSC학점)+'/30\n'+'기본소양 : '+str(산업시스템공학과기본소양학점)+'/6\n'+'기초교양 : '+str(산업시스템공학과기초교양학점)+'/16\n'+'범죄수사소프트웨어전공 : '+str(범죄수사소프트웨어전공필수학점+범죄수사소프트웨어전공선택학점)+'/36')
    elif for_strip_list[0]=='산업정보소프트웨어':
        del for_strip_list[0]
        for_strip_list=list(set(for_strip_list))
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과전공기초학점+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 산업시스템공학과기초교양:
                산업시스템공학과기초교양학점+=int(df[['산업시스템공학과기초교양학점']].iloc[산업시스템공학과기초교양.index(i)])
            if i in 융합소프트웨어전공필수:
                융합소프트웨어전공필수학점+=int(df[['산업정보소프트웨어전공필수학점']].iloc[산업정보소프트웨어전공필수.index(i)])
            if i in 융합소프트웨어전공선택:
                융합소프트웨어전공선택학점+=int(df[['산업정보소프트웨어전공선택학점']].iloc[산업정보소프트웨어전공선택.index(i)])
        산시전공=산업시스템공학과전공기초학점+산업시스템공학과전공전문학점
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/12\n'+'산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/24\n'+'( 18년도 이전 입학생 : 21학점 )\n'+'산업시스템공학과전공 : '+str(산시전공)+'/36\n'+'산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/18학점 이상\n'+'MSC : '+str(산업시스템공학과MSC학점)+'/30\n'+'기본소양 : '+str(산업시스템공학과기본소양학점)+'/6\n'+'기초교양 : '+str(산업시스템공학과기초교양학점)+'/16\n'+'융합소프트웨어전공 : '+str(산업정보소프트웨어전공필수학점+산업정보소프트웨어전공선택학점)+'/36')

    else:
        for_strip_list=list(set(for_strip_list))
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과전공기초학점+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 산업시스템공학과기초교양:
                산업시스템공학과기초교양학점+=int(df[['산업시스템공학과기초교양학점']].iloc[산업시스템공학과기초교양.index(i)])
        산시전공=산업시스템공학과전공기초학점+산업시스템공학과전공전문학점
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/12\n'+'산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/24\n'+'( 18년도 이전 입학생 : 21학점 )\n'+'산업시스템공학과전공 : '+str(산시전공)+'/60\n'+'산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/18학점 이상\n'+'MSC : '+str(산업시스템공학과MSC학점)+'/30\n'+'기본소양 : '+str(산업시스템공학과기본소양학점)+'/6\n'+'기초교양 : '+str(산업시스템공학과기초교양학점)+'/16')
    essential_list=['공학경제','미적분학및연습1','미적분학및연습2','공학선형대수학']
    for _ in for_strip_list:
        if _ in essential_list:
            essential_list.remove(_)
    essential_str=''
    for i in essential_list:
        essential_str+=i+','
    essential_str=essential_str.replace(essential_str,essential_str[0:len(essential_str)-1])
    #산시 필수 과목을 이수하지 않았을시 그 과목 보여주기
    if len(essential_list)!=0:
        context.bot.send_message(chat_id=update.effective_chat.id, text='[필수과목] '+essential_str+'을(를) 아직 수강하지 않았습니다!')
    #사용자가 오타로 적은 과목 봇이 사용자에게 전송하기
    if len(five_ride)!=0:
        print(five_ride)
        context.bot.send_message(chat_id=update.effective_chat.id, text=five_ride+'(은)는 잘못 입력된 과목 입니다.')

# 명령어  /start 정의 CommandHandler
start_handler = CommandHandler('start', start )
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
haksa_ballground_handler=CommandHandler("haksa_ballground",haksa_ballground)
mouthpoem_ballground_handler=CommandHandler("mouthpoem_ballground",mouthpoem_ballground)
scholarship_ballground_handler=CommandHandler("scholarship_ballground",scholarship_ballground)
international_ballground_handler=CommandHandler("international_ballground",international_ballground)
event_ballground_handler=CommandHandler("event_ballground",event_ballground)

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
#동국대학교 공지사항 crawling dispatcher
dispatcher.add_handler(normal_ballground_handler)
dispatcher.add_handler(haksa_ballground_handler)
dispatcher.add_handler(mouthpoem_ballground_handler)
dispatcher.add_handler(scholarship_ballground_handler)
dispatcher.add_handler(international_ballground_handler)
dispatcher.add_handler(event_ballground_handler)
#판다스로 선이수 MessageHandler(MessageHandler는 에코 이므로 맨위에 작성하면 맨위에서 상속 될수 밖에없다)
#따라서 맨 하위에 놔서 어떠한 명령어도 없을 경우에 message_handler를 실행한다.
mc_the_max_1_handler=CommandHandler('mc_the_max_1',mc_the_max_1)
dispatcher.add_handler(mc_the_max_1_handler)
info_1_handler=CommandHandler('info_1',info_1)
dispatcher.add_handler(info_1_handler)
ise_graduate_1_handler=CommandHandler("ise_graduate_1",ise_graduate_1)
dispatcher.add_handler(ise_graduate_1_handler)

#MessageHandler 선이수 과목 조회하기
mc_the_max_handler = MessageHandler(Filters.text,mc_the_max)
#과목정보 조회하기
info_handler=MessageHandler(Filters.text,info)
#졸업학점계산하기
ise_graduate_handler=MessageHandler(Filters.text,ise_graduate)

print('end')
#주기적으로 텔레그램 접속 새로운메세지가 있으면 받아온다.
updater.start_polling()
updater.idle()
