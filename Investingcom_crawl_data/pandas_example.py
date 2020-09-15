##pandas examples.

import pandas as pd


series_ex1=pd.Series([100,500,150],index=['카카오','삼성전자','현대차'])
print(series_ex1['카카오'])
print(series_ex1['현대차'])
print(series_ex1[1])

##series class는 딕셔너리 + 리스트의 형태이다.(순서가 있고, key와 data 대응 가능)
##series는 1차원 데이터구조, dataframe은 2차원 데이터구조로 이루어진다.
##series는 인덱스, 데이터 값으로 이루어져서 1차원이다.
##datafame 은 인덱스, 데이터 값, 컬럼으로 이루어져서 2차원이다.


df_ex1=pd.DataFrame({'가격':[100,500,150],'PER':[0.5,1.2,0.2],'ROA':[1.01,3.1,0.97]},
          index=['카카오','삼성전자','현대차'])

print(df_ex1['가격'], df_ex1['PER'],df_ex1['ROA'])
print(df_ex1['가격']['삼성전자'])
print(df_ex1.loc['카카오'],['ROA'])