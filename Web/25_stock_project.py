import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://finance.naver.com/")
elem = browser.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a/span").click()
time.sleep(1)
###################################################
soup = BeautifulSoup(browser.page_source, "lxml") # 셀레니움은 헤더정보가 없다고 봐도될듯
kospi1 = soup.find("span",attrs={"id":"KOSPI_now"}).get_text()
kospi2 = soup.find("span",attrs={"id":"KOSPI_change"}).get_text().strip()
kosdaq1 = soup.find("span",attrs={"id":"KOSDAQ_now"}).get_text()
kosdaq2 = soup.find("span",attrs={"id":"KOSDAQ_change"}).get_text().strip()
elem = browser.find_element_by_xpath("//*[@id='menu']/ul/li[3]/a/span").click()
time.sleep(1)
###################################################
s1 = browser.find_element_by_xpath("//*[@id='worldIndexColumn3']/li[1]/dl/dd[1]/strong").text
s2 = browser.find_element_by_xpath("//*[@id='worldIndexColumn3']/li[1]/dl/dd[1]/em").text
s3 = browser.find_element_by_xpath("//*[@id='worldIndexColumn3']/li[1]/dl/dd[1]/span[1]").text
n1 = browser.find_element_by_xpath("//*[@id='worldIndexColumn2']/li[1]/dl/dd[1]/strong").text
n2 = browser.find_element_by_xpath("//*[@id='worldIndexColumn2']/li[1]/dl/dd[1]/em").text
n3 = browser.find_element_by_xpath("//*[@id='worldIndexColumn2']/li[1]/dl/dd[1]/span[1]").text
d1 = browser.find_element_by_xpath("//*[@id='worldIndexColumn1']/li[1]/dl/dd[1]/strong").text
d2 = browser.find_element_by_xpath("//*[@id='worldIndexColumn1']/li[1]/dl/dd[1]/em").text
d3 = browser.find_element_by_xpath("//*[@id='worldIndexColumn1']/li[1]/dl/dd[1]/span[1]").text
elem = browser.find_element_by_xpath("//*[@id='menu']/ul/li[4]/a/span").click()
time.sleep(1)
####################################################
soup = BeautifulSoup(browser.page_source, "lxml") 
dollar1 = soup.find("div",attrs={"class":"head_info point_dn"}).find("span",attrs={"class":"value"}).text
dollar2 = soup.find("div",attrs={"class":"head_info point_dn"}).find("span",attrs={"class":"change"}).text
tof = soup.find("div",attrs={"class":"head_info point_dn"}).find_all("span",attrs={"class":"blind"})
tof = tof[-1].text
if tof == "하락":
    tof_result = "-"
elif tof == "상승":
    tof_result = "+"
else: 
    tof_result = ""

print("코스피 : {0}  {1}".format(kospi1,kospi2))
print("코스닥 : {0}  {1}".format(kosdaq1,kosdaq2))
print("s&p 500 : {0}  {1}  {2}".format(s1,s2,s3))
print("나스닥종합 : {0}  {1}  {2}".format(n1,n2,n3))
print("다우산업 : {0}  {1}  {2}".format(d1,d2,d3))
print("미국USD : {0}  {1}{2}".format(dollar1,tof_result,dollar2))
# browser.quit()



