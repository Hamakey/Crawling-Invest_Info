#투자지표(investment index) 데이터프레임 만들기


def crawling_invest(firm_code):
    import pandas as pd
    import requests
    invest_url='http://comp.fnguide.com/SVO2/asp/SVD_Finance.asp?pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=103&stkGb=701&gicode=' + firm_code
    invest_page=requests.get(invest_url)
    invest_tables=pd.read_html(invest_page.text)
    
    temp_df=invest_tables[1]
    
    temp_df=temp_df.set_index(temp_df.columns[0])
    temp_df=temp_df.loc[['PER수정주가(보통주) / 수정EPS PER계산에 참여한 계정 펼치기'
                         ,'PCR수정주가(보통주) / 수정CFPS PCR계산에 참여한 계정 펼치기'
                         ,'PSR수정주가(보통주) / 수정SPS PSR 계산에 참여한 계정 펼치기'
                         ,'PBR수정주가(보통주) / 수정BPS PBR계산에 참여한 계정 펼치기'
                         ,'총현금흐름세후영업이익 + 유무형자산상각비 총현금흐름']]
    temp_df.index=['PER','PCR','PSR','PBR','총현금흐름']
    return temp_df