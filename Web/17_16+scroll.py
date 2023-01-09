from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window() # 최대화

url="https://play.google.com/store/movies/top"
browser.get(url)

################### 스크롤 내리는 코드########################################
# #1920 * 1080, 세로방향으로 1080 내려라 라는 뜻(한페이지를 스크롤 다운)
# browser.execute_script("window.scrollTo(0, 1080)")
# 자 우리는 화면 가장 아래로 스크롤 내려야 하지..
# 문서 가장아래까지 스크롤 하는 개꿀코드
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# 이렇게 한다음 밑에 계속 업데이트 되니까 또 내려줘야지

import time
interval = 2 #2초에 한번씩 스크롤을 내릴꺼야

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이(얘는 계속 더해지네)를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        # 맨 밑 까지 온거니까
        break
    prev_height = curr_height #else 의 뜻
    
# 맨 위로 올려주기
browser.execute_script('window.scrollTo(0,0)')

print("~종료~")
################################################ 

##################################bs4와 합 쳐 보 자 ###

import requests 
from bs4 import BeautifulSoup
# request랑은 다르게 셀레니움은 문제가 없네
# url과 header 다 지워버리고

soup = BeautifulSoup(browser.page_source, "lxml")

# 업데이트된애들은 기존 10개와 클래스네임이 달라서 리스트로 묶어준다
# 이렇게 클래스네임을 리스트로 하면 OR의 뜻을 가지게 해주지.
# 인 줄 알았는데 !! 기존 10개가 클래스를 두개를 가지고 있어서 두번찍히네
# 그럼 그냥 클래스 밑에꺼 하나쓰면되지
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
# print(len(movies))

for movie in movies:

    # 영화 제목
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price: # 이것이 존재한다면!!
        original_price = original_price.get_text()
    else:
        continue

    # 할인 된 가격    
    price =  movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    
    # 링크 정보
    link = movie.find("a", attrs={"class":"JC71ub"})["href"] #이런 구조할려면 a href의 a가 무조건 앞에위치
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()