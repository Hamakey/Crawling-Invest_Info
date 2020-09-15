#재무비율(=financial ratio) 데이터프레임을 만드는 함수



def crawling_fr(firm_code):
    import requests
    import pandas as pd
    fr_url='http://comp.fnguide.com/SVO2/asp/SVD_Finance.asp?pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=103&stkGb=701&gicode=' + firm_code
    fr_page=requests.get(fr_url)
    fr_tables=pd.read_html(fr_page.text)
    
    temp_df=fr_tables[0]
    temp_df=temp_df.set_index(temp_df.columns[0])
    temp_df=temp_df.loc[['유동비율(유동자산/유동부채)*100 유동비율계산에 참여한 계정 펼치기',
                         '부채비율(총부채/총자본)*100 부채비율계산에 참여한 계정 펼치기'
                         ,'영업이익률(영업이익/영업수익)*100 영업이익률계산에 참여한 계정 펼치기'
                         ,'ROA(당기순이익(연율화)/총자산(평균))*100 ROA계산에 참여한 계정 펼치기'
                         ,'ROIC(세후영업이익(연율화)/영업투하자본(평균))*100 ROIC계산에 참여한 계정 펼치기']]
    temp_df.index=['유동비율','부채비율','영업이익률','ROA','ROIC']
    return temp_df