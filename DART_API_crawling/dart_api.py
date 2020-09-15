import dart_fs as fs
import dart_fss as dart


api_key='00cc4596027045e1f3ffe47456ed7aa3a3aeebd9'
da=dart.set_api_key(api_key=api_key)
api_key = dart.get_api_key()
result=fs.fs_extract(corp_code='00126380',bgn_date='20120101',end_date='20200719',report_tp='quarter')

filename='삼성전자'
path='C:\\Users\\user\\Desktop\\Python\\quant_trading\\fsdata'
result=fs.fs_extract.save(filename=filename,path=path)

path_file=path.format(path,'\\')