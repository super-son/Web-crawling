import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.21 Safari/537.36"}

for i in range(1, 6):
    print("페이지 :",i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+str(i)+"&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
    # 이렇게도 되고 format도 되고
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    
    for item in items:

        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            continue 
        
        name = item.find("div", attrs={"class":"name"}).get_text()
        if "Apple" in name:
            continue
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else :
            continue
    
        rate_count = item.find("span", attrs={"class":"rating-total-count"})
        if rate_count:
            rate_count = rate_count.get_text()[1:-1] 
        else :
            continue

        link = item.find("a", attrs={"class":"search-product-link"}) 
        link = link["href"] #애를 윗문장 마지막에 붙여도 되지
        
        if float(rate) >=4.5 and int(rate_count) >= 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점  ({rate_count}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) #줄긋기

        