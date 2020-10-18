from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from emoji import emojize
import requests
import json
import datetime
import time
import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


#telegram.ext.Updater : 텔레그램으로부터 업데이트를 받아서 dispatcher로 전달
#CommandHandler: 텔레그램 /start등의 Command
#MessageHandler: 텍스트 상태 업데이트
#CallbackQueryHandler: callback 쿼리


BOT_TOKEN='937755335:AAHsVeoU6isCkDyPY53LFu0quZdWRf88J8Q'   #나의 텔레그램 토큰
updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher


major=['산업시스템공학과','건설환경공학과','건축공학부','기계로봇에너지공학과','멀티미디어공학과','융합에너지신소재공학과','건설환경공학과','전자전기공학부']





def get_message(bot, update):
    text=update.message.text
    chat_id = update.effective_chat.id
    #bot.send_message(chat_id=chat_id, text = "학과를 입력해주세요.")
    global major
    if major[0] in text:
        bot.send_message(chat_id=chat_id, text=emojize("산업시스템공학과 환영합니다:heart_eyes:",use_aliases=True))
        bot.send_message(chat_id=chat_id, text = " /ise 를 입력해 주세요")
    elif major[1] in text:
        bot.send_message(chat_id=chat_id, text=emojize("건설환경공학과 환영합니다:heart_eyes:",use_aliases=True))
    elif major[2] in text:
        bot.send_message(chat_id=chat_id, text=emojize("건축공학부 환영합니다:heart_eyes:",use_aliases=True))
    elif major[3] in text:
        bot.send_message(chat_id=chat_id, text=emojize("기계로봇에너지공학과 환영합니다:heart_eyes:",use_aliases=True))
    elif major[4] in text:
        bot.send_message(chat_id=chat_id, text=emojize("멀티미디어공학과 환영합니다:heart_eyes:",use_aliases=True))
    elif major[5] in text:
        bot.send_message(chat_id=chat_id, text=emojize("융합에너지신소재공학과 환영합니다:heart_eyes:",use_aliases=True))
    elif major[6] in text:
        bot.send_message(chat_id=chat_id, text=emojize("건설환경공학과 환영합니다:heart_eyes:",use_aliases=True))
    elif major[7] in text:
        bot.send_message(chat_id=chat_id, text=emojize("전자전기공학부 환영합니다:heart_eyes:",use_aliases=True))
    else:
        bot.send_message(chat_id=chat_id, text=" 제대로 입력했는지 확인해주세요")



def ise(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Python\project\공대 이수체계도\공대 이수체계도\산업시스템공학과이수체계도.jpg','rb'))


ise_handler = CommandHandler('ise',ise)
updater.dispatcher.add_handler(ise_handler)

message_handler =MessageHandler(Filters.text, get_message) #updater를 통해서 filter된 text가 handler함수로 들어가게됨
updater.dispatcher.add_handler(message_handler)






updater.start_polling()
updater.idle()
