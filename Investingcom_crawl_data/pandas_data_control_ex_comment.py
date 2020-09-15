
import pandas as pd


file_path='C:\\Users\\user\\Desktop\\Python\\quant_trading\\excel\\마법공식 데이터.xlsx'
# print(pd.read_excel(file_path,sheet_name='PER'))
per_data=pd.read_excel(file_path,sheet_name='PER',index_col=0)

# print(per_data)
filtered_per=per_data[per_data['PER']>0]
sorted_per=filtered_per.sort_values(by='PER')
# sorted_per_ex=filtered_per.sort_values() 
# 윗줄이 변수로 저장이 안되는 이유는 data frame의 형태이지만 
#col이 지정이 안되어있어서 저장이 안됨.
# 즉 df 자료형은 반드시 sort_values(by=열 이름)를 해줘야함
sorted_per['PER랭킹']=sorted_per['PER'].rank()
# sorted_per['PER랭킹+1]=sorted_per['PER'].rank()+1
# 윗줄은 새로운 열의 데이터 만들기인데, 계산하여 수식넣기도 가능함.
# 대신에 dataframe인지 series인지 크기도 고려해서 진행해야함.

roa_data=pd.read_excel(file_path,sheet_name='ROA',index_col=0)

filtered_roa=roa_data.dropna()
filtered_roa.columns=['ROA']
sorted_roa=filtered_roa.sort_values(by='ROA',ascending=False)

sorted_roa['ROA랭킹']=sorted_roa.rank(ascending=False)

total_df=pd.merge(sorted_per,sorted_roa,how='inner',left_index=True,right_index=True)
#data frame 합치는 메소드_pd.merge 2개 이상의 데이터프레임에서
#기준이 되는 열을 뽑아 이를 기준으로 병합한다.
#병합 기준 1. outer 는 두 데이터프레임 중 한쪽에만 있는 데이터도
#합쳐짐
#병합 기준 2. inner 는 두 데이터프레임 중 양쪽 공통으로 있는
#데이터만 합쳐짐
#left_index=Ture, right_index=True 는 어떤열을 기준으로 병합할것인지
#그럼 그 기준은 outer와 inner의 기준을 잡는것인가?
#그렇다면 기준열이 3개이상일때는 어떻게 기준을 잡는건가...?

total_df['종합랭크']=(total_df['PER랭킹']+total_df['ROA랭킹']).rank()
total_df.sort_values(by='종합랭크')
