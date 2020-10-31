def ise_graduate(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='다음 양식에 맞게 수강한 과목을 입력하세요.\n연계/복수전공명(단일전공이면 X);수강한과목명1,...\nEx)\n융합소프트웨어;인간공학;응용통계학;자아와명상1')

    print(update.message.text)
    for_strip=update.message.text
    for_strip_list=list(map(str,for_strip.split(';')))
    print(for_strip_list)
    df = pd.read_excel('졸업요건_산시.xlsx',encoding='CP949')

    산업시스템공학과선택필수=list(map(str,df['산업시스템공학과선택필수']))
    산업시스템공학과선택필수학점=0
    산업시스템공학과전공필수=list(map(str,df['산업시스템공학과전공필수']))
    산업시스템공학과전공필수학점=0
    산업시스템공학과전공기초=list(map(str,df['산업시스템공학과전공기초']))
    산업시스템공학과전공기초학점=0
    산업시스템공학과전공전문=list(map(str,df['산업시스템공학과전공전문']))
    산업시스템공학과전공전문=0
    산업시스템공학과MSC=list(map(str,df['산업시스템공학과MSC']))
    산업시스템공학과MSC학점=0
    산업시스템공학과기본소양=list(map(str,df['산업시스템공학과기본소양']))
    산업시스템공학과기본소양학점=0
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

    if for_strip_list[0]=='융합소프트웨어':
        for i in for_strip_list:
            if i in 산업시스템공학과선택필수:
                산업시스템공학과선택필수학점+=int(df[['산업시스템공학과선택필수학점']].iloc[산업시스템공학과선택필수.index(i)])
            if i in 산업시스템공학과전공필수:
                산업시스템공학과전공필수학점+=int(df[['산업시스템공학과전공필수학점']].iloc[산업시스템공학과전공필수.index(i)])
            if i in 산업시스템공학과전공기초:
                산업시스템공학과선택전공기초+=int(df[['산업시스템공학과전공기초학점']].iloc[산업시스템공학과전공기초.index(i)])
            if i in 산업시스템공학과전공전문:
                산업시스템공학과전공전문학점+=int(df[['산업시스템공학과전공전문학점']].iloc[산업시스템공학과전공전문.index(i)])
            if i in 산업시스템공학과MSC:
                산업시스템공학과MSC학점+=int(df[['산업시스템공학과MSC학점']].iloc[산업시스템공학과MSC.index(i)])
            if i in 산업시스템공학과기본소양:
                산업시스템공학과기본소양학점+=int(df[['산업시스템공학과기본소양학점']].iloc[산업시스템공학과기본소양.index(i)])
            if i in 융합소프트웨어전공필수:
                융합소프트웨어전공필수학점+=int(df[['융합소프트웨어전공필수학점']].iloc[융합소프트웨어전공필수.index(i)])
            if i in 융합소프트웨어전공선택:
                융합소프트웨어전공선택학점+=int(df[['융합소프트웨어전공선택학점']].iloc[융합소프트웨어전공선택.index(i)])
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과선택필수 : '+str(산업시스템공학과선택필수학점)+'/??')
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과전공필수 : '+str(산업시스템공학과전공필수학점)+'/??')
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과전공기초 : '+str(산업시스템공학과전공기초학점)+'/??')
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과전공전문 : '+str(산업시스템공학과전공전문학점)+'/??')
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과MSC : '+str(산업시스템공학과MSC학점)+'/??')
        context.bot.send_message(chat_id=update.effective_chat.id, text='산업시스템공학과기본소양 : '+str(산업시스템공학과기본소양학점)+'/??')
        context.bot.send_message(chat_id=update.effective_chat.id, text='융합소프트웨어전공필수 : '+str(융합소프트웨어전공필수학점)+'/??')
        context.bot.send_message(chat_id=update.effective_chat.id, text='융합소프트웨어전공선택 : '+str(융합소프트웨어전공선택학점)+'/??')



    elif for_strip_list[0]=='디자인공학':
        print(4)
    elif for_strip_list[0]=='건설정보소프트웨어':
        print(4)
    elif for_strip_list[0]=='로봇융합소프트웨어':
        print(4)
    elif for_strip_list[0]=='문화예술소프트웨어':
        print(4)
    elif for_strip_list[0]=='범죄수사소프트웨어':
        print(4)
    elif for_strip_list[0]=='산업정보소프트웨어':
        print(4)
    elif for_strip_list[0]=='디자인공학':
        print(4)
