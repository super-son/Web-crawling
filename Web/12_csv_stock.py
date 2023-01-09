import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
#newline안쓰면 csv만들때 각 줄이 두칸씩 띄어진다
f = open(filename, "w", encoding="utf-8-sig",newline="")
#엑셀파일로 열었는데 utf-8도 한글 깨지면 -sig붙여준다 
writer = csv.writer(f)
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# 탭으로 구분되어 있는 데이터들이 리스트형태로 나눠 저장된다
#["N", "종목명","현재가"...]
print(type(title))
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # td를 적게가진 tr을 거른다.
            continue
        #.strip()은 개행문자 자동삭제
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data) #리스트형식을 넣어야하는데 data는 이미 list다