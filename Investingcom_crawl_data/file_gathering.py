# per 음수 필터링
# 올림차순 정렬
# 순위매기기
# ROA 내림차순 정렬
# 순위 매기기
# 두 순위 종합해 정렬




##엑셀 자료 경로 입력 및 열기-> 크롤링으로 변경예정
import pandas as pd

def file_gathering(path):
    import xlrd
    import operator as op  #딕셔너리 key와 data를 같이 정렬하기위한 모듈삽입_itemgetter()


    wb=xlrd.open_workbook(path)  


##불러올 Sheet 이름 설정
    per_sh=wb.sheet_by_name('PER')

##빈 딕셔너리 설정 -> 불러온 엑셀데이터를 딕셔너리형으로 변경하여 저장함
    per_dict={}
    for i in range(1,per_sh.nrows):
        data=per_sh.row_values(i)
        name=data[0] #[딕셔너리 내부의  [n번:m번] 의 n번 위치 지정  ]
        per=data[1]  #[딕셔너리 내부의  [n번:m번] 의 n번 위치 지정  ]
        if per>0:
            per_dict[name]=per


    sorted_per=sorted(per_dict.items(),key=op.itemgetter(1))
#item은 key와 data의 set을 의미하며 튜플형으로 불러옴. 
#itemgetter(엑셀의 사용할 첫 행의 번호)를 이용해서 data를 우선적으로 사용하는것으로 만듦.

    per_rank={}
    for num, firm in enumerate(sorted_per):
        per_rank[firm[0]]=num + 1

        roa_sh=wb.sheet_by_name('ROA')

        roa_dict={}

    for i in range(1,roa_sh.nrows):
        data=roa_sh.row_values(i)
        name=data[0] #[딕셔너리 내부의  [n번:m번] 의 n번 위치 지정  ]
        roa=data[1]  #[딕셔너리 내부의  [n번:m번] 의 m번 위치 지정  ]
        if roa!='':
            roa_dict[name]=roa
## ROA 지표는 낮을수록 좋기때문에 오름차순 반영 -> reverse=True
    sorted_roa=sorted(roa_dict.items(),key=op.itemgetter(1),reverse=True)
##ROA 지표에 대한 RANK 매기기
    roa_rank={}
    for num, firm in enumerate(sorted_roa):
        roa_rank[firm[0]]=num+1
    
    
##ROA 지표와 PER 지표를 합쳐서 판단하는 지표 작성 -> Total Rank
    total_rank={}

    for name in roa_rank.keys():
        if name in per_rank.keys():
            total_rank[name]=per_rank[name]+roa_rank[name]

    sorted_total=sorted(total_rank.items(),key=op.itemgetter(1))
    ##윗부분 지정제대로 안하니까 딕셔너리 key값(=종목name)이 똑바로 안나오네
    
    result_rank={}

    for num,firm in enumerate(sorted_total):
        result_rank[firm[0]]= num + 1
    


    return result_rank

print(file_gathering('C:\\Users\\user\\Desktop\\Python\\quant_trading\\excel\\마법공식 데이터.xlsx'))


df = pd.DataFrame(file_gathering('C:\\Users\\user\\Desktop\\Python\\quant_trading\\excel\\마법공식 데이터.xlsx'), index=[0])

df = (df.T)

##file_gathering의 값이 nrow*1의 형태이기 때문에, T 로 전치시켜줌

print (df)

df.to_excel('sorted_and_gathered_file.xlsx')
## file_gathering의 결과값을 다른 파일에 저장시켜줌


