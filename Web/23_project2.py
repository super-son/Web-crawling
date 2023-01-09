import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = "https://news.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
date = datetime.today().strftime("%Y년 %m월 %d일")
print(date)

#######################################################################################
# sum project랑은 다르게 얘는 주소다시보내는 방식!!

hd_news_datas = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li")
# .find_all("li", limit=3)으로 쓰면 idx>=2 안해고 3개까지 뽑을수있데
print("[헤드라인 뉴스]")
for idx, hd_news in enumerate(hd_news_datas):
    news_url ="https://news.naver.com/" + hd_news.find("div", attrs={"class":"hdline_article_tit"}).a["href"]
    news_res = requests.get(news_url,headers=headers)
    news_res.raise_for_status()
    news_soup = BeautifulSoup(news_res.text, "lxml")
    hd_news = news_soup.find("h3", attrs={"id":"articleTitle"}).get_text()
    print(" {0}. {1}".format(idx+1, hd_news))
    print("(링크 : {0})".format(news_url))
    if idx >= 2:
        break
    # for 문에 따른 변수의 동적할당은 좋지않은 방법! print를 한큐에 찍어내는 이유!

#######################################################################################

url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

it_news_datas = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li")
print("[IT 일반 뉴스]")
for idx, it in enumerate(it_news_datas):
    link = it.find("dl").find("dt", attrs={"class":"photo"}).a["href"]
    # index=0
    # img = it.find("img")
    # if img:
    #     index=1
    # title = it.find("a")[index] #이런식의 전개도 괜찮지
    it_news = it.find("dl").find("dt", attrs={"class":""}).get_text().strip() # 클래스 없는거 찾는거 좋았다.
    print(" {0}. {1}".format(idx+1, it_news))
    print("(링크 : {0})".format(link))
    if idx >= 2:
        break

   

