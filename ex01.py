import pandas as pd
df = pd.read_excel('졸업요건_산시.xlsx')
for_strip_list=["인간공학","린간공학"]
five_ride=[]
for i in df:
    for j in df[i]:
        for k in for_strip_list:
            if k in str(j):
                break
            break
            else:
                five_ride.append(k)
                break
print(set(five_ride))
