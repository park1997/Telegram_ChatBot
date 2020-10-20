import pandas as pd
ise_df = pd.read_csv("D:/Python/project/공대선이수/산시선이수.csv",encoding='CP949')
ise_df_dic={}
k=0
for i in ise_df['후수교과목']:
    ise_df_dic[i]=ise_df['선수교과목'][k]
    k+=1
print(ise_df_dic)
