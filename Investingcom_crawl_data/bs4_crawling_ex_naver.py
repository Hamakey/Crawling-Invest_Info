

import requests as rq

naver_url='https://www.naver.com/'
naver_response=rq.get(naver_url)

naver_response.text

import bs4

naver_bs=bs4.BeautifulSoup(naver_response.text,'lxml')
result=naver_bs.find('span',class_='ah_k')

result.text

result_list=naver_bs.find_all('span',class_='ah_k')

for span in result_list:
    print(span.text)
    
    
######'NoneType' object has no attribute 'text'
###### 위의 에러는 아무 값을 못받았을때 나오는 에러입니다. 확인필