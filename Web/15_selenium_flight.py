# https://blog.naver.com/PostView.nhn?blogId=statp_r&logNo=222170495713&parentCategoryNo=&categoryNo=10&viewDate=&isShowPopularPosts=true&from=search
# 여기쓰니까 콘솔창 에러들 잡아줌
# 한개만 남기고 다 끄니까 되네
# 코드 맨 밑에 input() 한 줄 넣으시면 동작 완료 후 엔터를 입력할때까지 대기하도록 할 수가 있답니다!
from selenium import webdriver
# 이 밑에 세개는 time sleep 대신으로 사용하는 꿀 코드
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window # 화면 전체화면으로 해줌

# 아니 지금 여기 사이트 자체가 좀 이상하네
# xpath로 긁어와도 list로만 받네 자꾸

url = "https://flight.naver.com/flights/"
browser.get(url)

# 링크를 타는 text정보로도 get할수있네
# 하나니까 elements가 아니라 element로 해야지 ㅇㅇ
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 25,26일 선택할건데
# 다음달 25,26일의 코드 text정보도 25,26로 동일하기때문에!
# 이번달 - [0], 다음달 - [1]
browser.find_elements_by_link_text("25")[0].click()
browser.find_elements_by_link_text("26")[0].click()

# 제주도 선택 및 항공권 검색
browser.find_element_by_class_name("bg_gradient").click()
browser.find_element_by_link_text("항공권 검색").click()

# time sleep대신 효율적인 기다리는 코드공식
# 최대 10초 준다는 설정 .. 넘기면 에러
# 저 xpath의 것이 존재할때까지만 기다려 달라는 거지

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text) # 첫번째 결과 출력
    # 내가 여기서 xpath에 ''넣을때 " "를 안없애고 같이 넣어서 에러가 뜸

# 에러나서 바로 파이널리 가거나, 동작 다하고 파이널리 가거나.
finally:
    print("hi")
    browser.quit()

