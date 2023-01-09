from selenium import webdriver

## headless 크롬을 사용하면 실제로 크롬을 안켜도 백그라운드에서
## 동작하므로 속도가 빠르고 용량을 적게 차지하지
## 이거 두줄 첨가해주면 끝!!
options = webdriver.ChromeOptions()
options.headless = True

#이까지 해주면되지만 백그라운드 브라우저창이 어떻게 돌아갈지 모르니 크기를 명시해주는정도의 느낌
options.add_argument("window-size=1920x1080")
browser = webdriver.Chrome(options=options)

browser.maximize_window() 

url="https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 2 

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
    #else
    prev_height = curr_height

print("~가져온다~")
# 스크롤 다 됬을때 화면을 스크린샷해준다
browser.get_screenshot_as_file("google_movie.png")
################################################ 

##################################bs4와 합 쳐 보 자 ###

import requests
from bs4 import BeautifulSoup
# request랑은 다르게 셀레니움은 문제가 없네
# url과 header 다 지워버리고

soup = BeautifulSoup(browser.page_source, "lxml") #셀레니움과 연계할때 이렇게 쓰는듯

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

print
browser.quit()