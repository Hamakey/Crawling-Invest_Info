#전 종목코드 입력 -> 한국거래소

def insert_company_code(path):
    
    def make_code(x):
        x=str(x)
        return'A' + '0' * (6-len(x)) + x
    import pandas as pd
    
    code_data=pd.read_excel(path,'소프트웨어 개발 및 공급업')
    code_data=code_data[['종목코드','기업명']]
    code_data['종목코드']=code_data['종목코드'].apply(make_code)

    return code_data


