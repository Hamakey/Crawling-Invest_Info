
import pandas as pd

df_ex2=pd.DataFrame({'가격':[100,140,155,70,90],'PER':[1.1,0.8,0.7,2.3,3.9],'거래량':[100,800,890,700,2000]},
          index=['a','b','c','d','e'])


# print(df_ex2[df_ex2['가격']>=100])

# print(df_ex2[df_ex2['거래량']<1000])

# print(df_ex2['PER'].sort_values(ascending=False))

##sort_values 이거는 행, data 기준으로 정렬할때 사용함
##ascending=False는 내림차순, 안쓰면 오름차순
##df_ex2['PER']은 정렬하고싶은 데이터   .sort_values()는 정렬방식정의


##sort_values 이거는 행, data + 열(by를 이용하여 정렬함) 까지 정렬가능
# print(df_ex2.sort_values(by='PER'))

# print(df_ex2.sort_values(by='PER',ascending=False))

print(df_ex2['거래량'].rank(ascending=False))
