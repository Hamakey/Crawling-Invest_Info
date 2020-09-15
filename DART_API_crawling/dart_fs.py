# 재무제표 추출
# Parameters
# ①corp_code: str___ 공시대상회사의 고유번호(8자리)
# ②bgn_de: str___ 검색 시작일자(YYYYMMDD)
# ③end_de: str, optional___ 검색 종료일자(YYYYMMDD)
# fs_tp: tuple of str, optional___ ‘bs’ 재무상태표, ‘is’ 손익계산서, ‘cis’ 포괄손익계산서, ‘cf’ 현금흐름표
# separate: bool, optional ___ 개별재무제표 여부
# report_tp: str, optional ___ ‘annual’ 1년, ‘half’ 반기, ‘quarter’ 분기
# lang: str, optional___ ‘ko’ 한글, ‘en’ 영문
# separator: bool, optional___1000단위 구분자 표시 여부
# Returns
# FinancialStatement___제무제표 검색 결과
# rtype___FinancialStatement ..

def fs_extract(corp_code,bgn_date,end_date,report_tp):
    import dart_fss as dart
    import datetime
    
    result=dart.fs.extract(corp_code,bgn_date,end_date,separate=False,report_tp=report_tp,lang='ko')

    return result
