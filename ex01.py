import pandas as pd

df = pd.read_excel('졸업요건_산시.xlsx')
for_strip_list=["인간공학","린간공학","공학선형대수학","공선대","글로벌리더십","자아와명상1","일반물리학"]
five_ride=for_strip_list
for i in df:
    for k in for_strip_list:
        for j in df[i].isin([k]):
            if j ==True:
                five_ride.remove(k)
                break
print(five_ride)
