import time
import crawling_fs as crfs
import crawling_fr as crfr
import crawling_invest as crinv
import insert_company_code
import pandas as pd
import requests
import change_df_form

path='C:\\Users\\user\\Desktop\\Python\\quant_trading\\excel\\data1.xls'

code_data=insert_company_code.insert_company_code(path)

for num, code in enumerate(code_data['종목코드']):
    try:
        print(num,code)
        time.sleep(1)
        try:
            fs_df=crfs.crawling_fs(code)
        except requests.exceptions.Timeout:
            time.sleep(10)
            fs_df=crfs.crawling_fs(code)
        fs_df_changed=change_df_form.change_df_form(code,fs_df)
        if num==0:
            total_fs=fs_df_changed
            print(total_fs)
        else:
            total_fs=pd.concat([total_fs,fs_df_changed])
            print(total_fs)
    except ValueError:
        continue
    except KeyError:
        continue