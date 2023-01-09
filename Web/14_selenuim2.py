from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# elem = .. 형식으로 가도되는데 더 간단하게 가볼게!!

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
browser.find_element_by_class_name("link_login").click()

# 3. 정보입력
id = "newhj1447"
pw = "thsgnlwns9631!"
browser.find_element_by_xpath("//*[@id='id']").send_keys(id)
browser.find_element_by_xpath("//*[@id='pw']").send_keys(pw)
browser.find_element_by_xpath("//*[@id='log.login']").send_keys(Keys.ENTER)

########################################### 자동입력방지 뚫는 개꿀코드 (자바스크립트인듯)
###########################################
# browser.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
# browser.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
# browser.find_element_by_xpath("//*[@id='log.login']").click()

# 4. 아이디 잘못쳤다하고, 아이디 새로 입력
time.sleep(3) #이걸 쓰는이유는 보안문자나 자동입력방지같은
#새로운 창이뜨면서 시간 갭이 뜨는데 그 타이밍에 입력하면 씹혀서 대기.
new_id = "newhj1447"
browser.find_element_by_xpath("//*[@id='id']").clear() # 이거안하면 뒤에 추가를 시켜
browser.find_element_by_xpath("//*[@id='id']").send_keys(new_id)

# # 5. html 정보출력
# print(browser.page_source) # 현재 해당페이지의

# # 6. 브라우저 종료
# # browser.close() # 현재 탭만 종료
# browser.quit() # 전체 브라우저 종료

################################################################################## xpath의 극한의 효율
# 실제로 작업할때는 몇 번째의 순번을 띠는 xpath는 언제든지 변할수 있기 때문에 text 값으로 처리하는것이 낫다.
# 그런데 또 그냥 text로 하기에는 코드 내 중복되는 text가 나올 수도 있으므로 xpath와 text를 모두 이용하는 방식이 가장 좋다.
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click() 이것을
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # 이렇게 해주면
# a 하위까지 범위를 좁힌 후 text값이 contact form 인것을 찾는것이다!!
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click() # 이건 포함단어를 찾는것인데
# 텍스트도 2020, 2021 처럼 변하는 값이라면 이렇게 포함값을 해주면 좋지!
###################################################################################




