from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

options.add_argument("window-size=1920x1080")
# 이걸 더해주는 것이다..!
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
browser = webdriver.Chrome(options=options)

browser.maximize_window() 

# what is my user agent의 url이다
url="https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
#AppleWebKit/537.36 (KHTML, like Gecko) 
#Chrome/88.0.4324.150 Safari/537.36
d_value = browser.find_element_by_id("detected_value")
# 이대로 출력해보니까 위의 Chrome부분이 HeadlessChrome 으로 값이 변질되네
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
# 원래의 user-agent를 옵션으로 이렇게 더해주면 된다!!
print(d_value.text)
browser.quit()