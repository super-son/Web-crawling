# 셀레늄을 위해서 추가로 웹 드라이버를 설치해줘야 하고 브라우저 마다 다르다
# 크롬 드라이버를 설치해보자. 크롬버전확인후 일치
# chrome://version를 크롬에 입력해서 버전확인후 chrome drive -> 버전일치확인 -> win 32설치
from selenium import webdriver

# https://blog.naver.com/PostView.nhn?blogId=statp_r&logNo=222170495713&parentCategoryNo=&categoryNo=10&viewDate=&isShowPopularPosts=true&from=search
# 여기쓰니까 콘솔창 에러들 잡아줌
# 한개만 남기고 다 끄니까 되네

#같은 경로가 아니라면 path로 채워야되
browser = webdriver.Chrome()
#터미널플레이로 열린 웹이랑 소통하면서 해라!
browser.get("http://naver.com")

# #네이버로그인 버튼 클래스 따와서 elem에 저장
# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back() # 이전의 작업
# browser.forward() # 이후의 작업
# browser.refresh() # 새로고침

#네이버 검색창
elem = browser.find_element_by_id("query")
#글자 타이핑만은 이거안해도 되는데 엔터를 위해선 이걸 import 해야되
from selenium.webdriver.common.keys import Keys
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

#코드의 태그 가져오기
#해당태그 전부 들고오려면 elements!! 
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    e.get_attribute("href")
    

#갑자기 다음으로 빤스런. xpath로 해보리기
browser.get("http://daum.net")
elem = browser.find_element_by_xpath("//*[@id='q']")
elem.send_keys("나도코딩")
#id="daumSearch" 원래 이거였는데 인식이 안되기때문에 ' ' 로 교체.. 얘는 검색버튼 xpath임
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
# 자 중간에 뭔가 에러가난다? elem을 재정의 해줘야 한다
elem.click()
browser.close() # 현재 탭만 닫기
browser.quit() # 브라우저 모두 꺼보리기

########################################### 자동입력방지 뚫는 개꿀코드 (자바스크립트인듯)
###########################################
# browser.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
# browser.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
# browser.find_element_by_xpath("//*[@id='log.login']").click()