import requests
from bs4 import BeautifulSoup
url = "http://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
with open("test.html","w",encoding="utf-8") as f: # html 허용코드범위 파악!
    f.write(soup.prettify())
    
#########################################################################################

print(soup.find("a", attrs={"class":"gb_g"}).get_text()) # "a"가 없어도 되
cartoons = soup.find_all("a", attrs={"class":"gb_g"}) #여기서 나열되는 쟤들은 같은 계급이라고 생각
for i in cartoons:
    print(i.get_text()) # 해보니까 꼭 .get_text()안하고 .text 해도 무관하네
link1 = cartoons[0]["target"] # get_attribute 코드와 똑같은 뜻인듯 ㅋ 이건 내 뇌피셜
link2 = cartoons[0].a["href"] 
for cartoon in cartoons:
    rate = cartoon.strong.get_text() #div하위태그의 strong에 해당되는 get text
    rate = cartoon.find("strong").get_text() #같다잉
    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # td를 적게가진 tr을 거른다.
            continue
        #.strip()은 개행문자 자동삭제   
        data = [column.get_text().strip() for column in columns]
        
##########################################################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get("http://naver.com")
elem = browser.find_element_by_id("query").click() #id뿐만 아니라 다른것도 가능하지
#browser.find_element_by_xpath("query").click()
#browser.find_element_by_class_name("bg_gradient").click()
#browser.find_element_by_link_text("항공권 검색").click()

elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
browser.quit()

### 꿀팁 전수
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click() 
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()
# 위에껄 아래처럼 xpath에 text값까지 합해서 사용한다면 훨씬 품질이 좋아진다. 변화에도 견딜수있다.
# 저건 포함하는 단어를 찾아주는 거다. 자세한건 14번으로 ㄱ

######### time.sleep() 대체방법

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text) # 첫번째 결과 출력
    # 내가 여기서 xpath에 ''넣을때 " "를 안없애고 같이 넣어서 에러가 뜸
# 에러나서 바로 파이널리 가거나, 동작 다하고 파이널리 가거나.
finally:
    print("hi")
    browser.quit()
    
##################################################################### 셀레니움 자동 스크롤

import time
interval = 2 

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

print("~종료~") 
# 여기에 bs4 더해주면 되겟지

############################################# headless 크롬

options = webdriver.ChromeOptions()
options.headless = True
#이까지 해주면되지만 백그라운드 브라우저창이 어떻게 돌아갈지 모르니 크기를 명시해주는정도의 느낌
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
# 이렇게 user-agent를 명시해주면 chrome -> headlesschorme으로 변형되는 걸 방지
browser = webdriver.Chrome(options=options)
################################################################셀레니움과 연계할때 이렇게 쓰는듯##############################33
soup = BeautifulSoup(browser.page_source, "lxml") 