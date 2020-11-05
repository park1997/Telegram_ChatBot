import pandas as pd
ise_df = pd.read_excel("산시이수과목구분.xlsx",sheet_name='Sheet1')
ise_df_선택필수 = pd.read_excel("산시이수과목구분.xlsx",sheet_name='선택필수')
ise_df_전공필수 = pd.read_excel("산시이수과목구분.xlsx",sheet_name='전공필수')
ise_df_전공전문 = pd.read_excel("산시이수과목구분.xlsx",sheet_name='전공전문')
ise_df_전공기초 = pd.read_excel("산시이수과목구분.xlsx",sheet_name='전공기초')
ise_df_MSC = pd.read_excel("산시이수과목구분.xlsx",sheet_name='MSC')
ise_df_기본소양 = pd.read_excel("산시이수과목구분.xlsx",sheet_name='기본소양')

ise_df_choose = list(map(str,ise_df['선택필수']))
ise_df_must = list(map(str,ise_df['전공필수']))
ise_df_pro = list(map(str,ise_df['전공전문']))
ise_df_base = list(map(str,ise_df['전공기초']))
ise_df_MSC = list(map(str,ise_df['MSC']))
ise_df_cow_sheep = list(map(str,ise_df['기본소양']))

print(update.message.text)
for_strip=update.message.text
for_strip=''.join(for_strip.split())

if for_strip in ise_df_choose:
    result='선택필수'
    context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 은('는') \'"+result+"\' 입니다.")
if for_strip in ise_df_must:
    result='전공필수'
    context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 은('는') \'"+result+"\' 입니다.")
if for_strip in ise_df_pro:
    result='전공전문'
    context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 은('는') \'"+result+"\' 입니다.")
if for_strip in ise_df_base:
    result='전공기초'
    context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 은('는') \'"+result+"\' 입니다.")
if for_strip in ise_df_MSC:
    result='MSC'
    context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 은('는') \'"+result+"\' 입니다.")
if for_strip in ise_df_cow_sheep:
    result='기본소양'
    context.bot.send_message(chat_id=update.effective_chat.id, text="\'"+update.message.text+"\' 은('는') \'"+result+"\' 입니다.")
