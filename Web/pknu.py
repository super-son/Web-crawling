from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import sys
import time

id = "201811958"
pw = "jun5281447!"

browser = webdriver.Chrome()
url = "https://lms.pknu.ac.kr/ilos/st/course/submain_form.acl"

browser.get(url)
time.sleep(2)
pyautogui.press("enter")
elem=browser.find_element_by_xpath('//*[@id="header"]/div[4]/ul').click()
elem=browser.find_element_by_xpath('//*[@id="usr_id"]').send_keys(id)
elem=browser.find_element_by_xpath('//*[@id="usr_pwd"]').send_keys(pw)
elem=browser.find_element_by_xpath('//*[@id="login_btn"]').click()
elem=browser.find_element_by_xpath('//*[@id="header"]/div[4]/div/fieldset/div/div[2]/img').click()
time.sleep(2)
notify_list=browser.find_elements_by_class_name('notification_content')
for notify in notify_list :
    print(notify.text)
    print()




