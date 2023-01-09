import requests
import re
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# 처음에 request로 가져올수 있는지 셀레니움 써야되는지 판단하려면
# with open("movie.html","w",encoding="utf-8") as f:     
# f.write(soup.prettify()) 한 다음에 데이터 검색 
########################### 내가 짠 망코드##################################
# forms = soup.find_all("td", attrs={"class" : "col1"})
# extends = soup.find_all("td", attrs={"class" : "col2"})
# prices = soup.find_all("td", attrs={"class" : "col3"})
# places = soup.find_all("td", attrs={"class" : "col4"})
# floors = soup.find_all("td", attrs={"class" : "col5"})

# for i in range(0,5) :
#     form = forms[i]
#     extend = extends[i]
#     price = prices[i]
#     place = places[i]
#     floor = floors[i]
#     print(f"거래 : {form.get_text()}")
#     print(f"공급/전용면적 : {extend.get_text()}")
#     print(f"매물가(만원) : {price.get_text()}")
#     print(f"동 : {place.get_text()}")
#     print(f"층 : {floor.get_text()}") 
#     print("-"*100)
############################# 나도코딩 코드##################################
datas = soup.find("table",attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, data in enumerate(datas):
    datas2 = data.find_all("td")
    print("==============매물 {}==============".format(index+1))
    print("거래 : ", datas2[0].get_text())
    print("공급/전용면적 : ", datas2[1].get_text())
    print("매물가(만원) : ", datas2[2].get_text().strip(),"만원") #개행문자 없애주는 
    print("동 : ", datas2[3].get_text())
    print("층 : ", datas2[4].get_text()) 