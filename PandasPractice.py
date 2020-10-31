import pandas as pd
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
newmeterial_df = pd.read_excel("D:/Python/Telegram_ChatBot/공대선이수/건축학선이수.xlsx")
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
print(df_dic)
