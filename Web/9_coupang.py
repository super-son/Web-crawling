# http method
# get과 post
# get에 비해 post가 크기가 크고 개인정보에 안전하다는점
# 예를들면 get의 주소방식은 직관적이고 ?page=2이런식으로 되있어
# 반면 post는 id=213이런 정보를 가지고있어서 애초에 보여주지않고 내부에 숨겨버려
import requests
import re #정규식 쓰기 위함
from bs4 import BeautifulSoup
# url page=2정보를 내가 page=1로 바꾼거
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.21 Safari/537.36"}
res = requests.get(url,headers=headers)
## 자자 user-agent 없이 그냥 하니까 쿠팡서버에서 막네
## 사람이 직접 들어가는것같은 역할을 해준다네..  
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
#search-product로 시작하는 것에 대한 정규식
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

# for item in items:
#     name = item.find("div", attrs={"class":"name"}).get_text()
#     price = item.find("strong", attrs={"class":"price-value"}).get_text()
    
#     # 아 평점이 없는 광고성애들도 있구나
#     rate = item.find("em", attrs={"class":"rating"})
#     if rate:
#         rate = rate.get_text()
#     else :
#         rate = "평점 없음"
   
#     rate_count = item.find("span", attrs={"class":"rating-total-count"})
#     if rate_count:
#         rate_count = rate_count.get_text()
#     else :
#         rate_count = "평점 수 없음"
    
#     print(name, price, rate, rate_count)

###########################광고성 애들은 배제 시켜볼게   
for item in items:

    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        # print(" <광고 상품 제외합니다>")
        continue #이렇게 해줘야 걸러주는 역할을 함
                 #ㄷㄷ 사기코드

    name = item.find("div", attrs={"class":"name"}).get_text()
    # 애플 제품 제외
    if "LG" in name:
        # print(" <LG 상품 제외합니다>")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    
    # 광고가 아니더라도 평점이 없는 애들땜시.. ㅎ
    # 리뷰 100개 이상, 평점 4.5이상 뽑아보자
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else :
        # print(" <평점 없는 상품 제외합니다>")
        continue
   
    rate_count = item.find("span", attrs={"class":"rating-total-count"})
    if rate_count:
        rate_count = rate_count.get_text() #현 출력값 : (26)
        rate_count = rate_count[1:-1] #슬라이싱으로 숫자만
    else :
        # print(" <평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >=4.5 and int(rate_count) >= 100:
        print(name, price, rate, rate_count)

    