import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8F%99%EB%9E%98%EA%B5%AC+%EC%95%88%EB%9D%BD%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EC%9B%B9+%EB%84%A4%EC%9D%B4%EB%B2%84%EB%82%A0%EC%94%A8+%EC%A7%80%EC%97%AD&tqi=huFDOdprvmssstnagJosssssswK-502945"
    soup = create_soup(url)
    weather_box = soup.find("div", attrs={"class":"weather_area _mainArea"})
    area = weather_box.find("span", attrs={"class":"btn_select"}).get_text()
    temp = soup.find("div", attrs={"class":"info_data"})
    today_temp = temp.find("span", attrs={"class":"todaytemp"}).get_text()
    temp_text = temp.find("p", attrs={"class":"cast_txt"}).get_text().split(", ")
    temp_height = soup.find("li", attrs={"class":"date_info today"}).find("dd").find_all("span")
    low_temp = temp_height[0].get_text()
    high_temp = temp_height[-1].get_text()
    rain = soup.find("li", attrs={"class":"date_info today"}).find_all("span", attrs={"class":"num"})
    m_rain = rain[0].get_text()
    a_rain = rain[1].get_text()
    dust = soup.find("dl", attrs={"class":"indicator"}).find_all("dd")
    m_dust = dust[0].get_text()
    c_dust = dust[1].get_text()
    
    print("[오늘의 날씨] - ({0})\n".format(area))
    print(temp_text[0]+" "+today_temp+"℃ ({0})".format(temp_text[1]))
    print("최저기온 : {0}℃ , 최고기온 : {1}℃".format(low_temp, high_temp))
    print("오전 강수확률 : {0}%, 오후 강수확률 : {1}%".format(m_rain, a_rain)) 
    print("미세먼지 : {0}, 초미세먼지 : {1}".format(m_dust, c_dust))
    print()

def scrape_headline_news():
    url = "https://news.naver.com/"
    soup = create_soup(url)
    hd_news_datas = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li",limit=3) # 이렇게 하면 3개까지 찾아라는 뜻
    print("[헤드라인 뉴스]\n")
    
    for idx, hd_news in enumerate(hd_news_datas):
        news_url = url + hd_news.a["href"]
        hd_news = hd_news.find("a").get_text().strip()
        print(" {0}. {1}".format(idx+1, hd_news))
        print("(링크 : {0})".format(news_url))
    print()

def scrape_it_news():
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    it_news_datas = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    print("[IT 일반 뉴스]\n")

    for idx, it in enumerate(it_news_datas):
        link = it.find("dl").find("dt", attrs={"class":""}).a["href"]
        it_news = it.find("dl").find("dt", attrs={"class":""}).get_text().strip() # 클래스 없는거 찾는거 좋았다.
        print(" {0}. {1}".format(idx+1, it_news))
        print("(링크 : {0})".format(link))
    print()

def scrape_english():
    url = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_I_others_english&keywd=haceng_submain_lnb_lec_I_others_english&logger_kw=haceng_submain_lnb_lec_I_others_english"
    soup = create_soup(url)
    script_datas = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")}) #정규식을 이용한 코드
    print("[오늘의 영어회화지문 - 해커스영어]\n")
    print("(영어 지문)")
    for script in script_datas[len(script_datas)//2:] : # 8문장이 있다고 가정할 때, index기준 4~7 까지 가져오기. 근데 왜 /는 안되고 //만 되지?
        print(script.get_text().strip())
    print()
    time.sleep(1)
    print("(한글 지문)")
    for script in script_datas[:len(script_datas)//2] :
        print(script.get_text().strip())
    print()

def scrape_stock_kor():
    print("[지수변동]\n")
    url = "https://finance.naver.com/sise/"
    soup = create_soup(url)
    kospi1 = soup.find("span",attrs={"id":"KOSPI_now"}).get_text()
    kospi2 = soup.find("span",attrs={"id":"KOSPI_change"}).get_text().strip()
    kosdaq1 = soup.find("span",attrs={"id":"KOSDAQ_now"}).get_text()
    kosdaq2 = soup.find("span",attrs={"id":"KOSDAQ_change"}).get_text().strip()
    print("코스피 : {0}  {1}".format(kospi1,kospi2))
    print("코스닥 : {0}  {1}".format(kosdaq1,kosdaq2))

def scrape_stock_eng(): # 해외증시가 로딩되는데 시간텀이 있네
    browser.get("https://finance.naver.com/world/")
    # 해외증시가 바로안뜨고 조금있다가 뜨네
    s1 = browser.find_element_by_xpath("//*[@id='worldIndexColumn3']/li[1]/dl/dd[1]/strong").text
    s2 = browser.find_element_by_xpath("//*[@id='worldIndexColumn3']/li[1]/dl/dd[1]/em").text
    s3 = browser.find_element_by_xpath("//*[@id='worldIndexColumn3']/li[1]/dl/dd[1]/span[1]").text
    n1 = browser.find_element_by_xpath("//*[@id='worldIndexColumn2']/li[1]/dl/dd[1]/strong").text
    n2 = browser.find_element_by_xpath("//*[@id='worldIndexColumn2']/li[1]/dl/dd[1]/em").text
    n3 = browser.find_element_by_xpath("//*[@id='worldIndexColumn2']/li[1]/dl/dd[1]/span[1]").text
    d1 = browser.find_element_by_xpath("//*[@id='worldIndexColumn1']/li[1]/dl/dd[1]/strong").text
    d2 = browser.find_element_by_xpath("//*[@id='worldIndexColumn1']/li[1]/dl/dd[1]/em").text
    d3 = browser.find_element_by_xpath("//*[@id='worldIndexColumn1']/li[1]/dl/dd[1]/span[1]").text
    
    print("s&p 500 : {0}  {1}  {2}".format(s1,s2,s3))
    print("나스닥종합 : {0}  {1}  {2}".format(n1,n2,n3))
    print("다우산업 : {0}  {1}  {2}".format(d1,d2,d3))

def scrape_stock_dollar():
    url = "https://finance.naver.com/marketindex/"
    soup = create_soup(url)
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
    print("USD 달러 : {0}  {1}{2}%{3}".format(dollar1,tof_result,dollar2,tof))
    print()

def scrape_lucky():
    print("정보를 가져오는 중입니다. 잠시만 기다려주세요..")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8"
    browser = webdriver.Chrome()
    browser.get(url)
    birth = "20000106"
    elem = browser.find_element_by_xpath("//*[@id='srch_txt']").send_keys(birth)
    elem = browser.find_element_by_xpath("//*[@id='fortune_birthCondition']/div[1]/fieldset/input").click()
    time.sleep(1)
    lucky_text = browser.find_element_by_xpath("//*[@id='fortune_birthResult']/dl[1]/dd")
    print("[오늘의 운세]\n")
    print(lucky_text.text)
    print()
    
if __name__ == "__main__" : # 직접실행이 아닐시 동작하지않음.

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
    browser = webdriver.Chrome(options=options)
    ###########################################
    print()
    print("안녕하세요. 빅스비입니다\n")
    time.sleep(1)
    date = datetime.today().strftime("%Y년 %m월 %d일")
    print(date)
    print()
    time.sleep(1)
    scrape_weather()
    time.sleep(1)
    scrape_headline_news()
    time.sleep(1)
    scrape_it_news()
    time.sleep(1)
    scrape_english()
    time.sleep(1)
    scrape_stock_kor()
    time.sleep(1)
    scrape_stock_eng()
    time.sleep(1)
    scrape_stock_dollar()
    time.sleep(1)
    scrape_lucky()
    time.sleep(1)
    print("행복한 하루 보내세요")
