firmcode_list=['A005930','A005380','A035420','A003550','A034730']

import crawling_fs as cr
import change_df_form as ch_form
import pandas as pd

for num,code in enumerate(firmcode_list):
    
    fs_df=cr.crawling_fs(code)
    fs_df_changed=ch_form.change_df(code,fs_df)
    if num==0:
        total_fs=fs_df_changed
    else:
        total_fs=pd.concat([total_fs,fs_df_changed])
        
