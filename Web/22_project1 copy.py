import requests
from bs4 import BeautifulSoup
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8F%99%EB%9E%98%EA%B5%AC+%EC%95%88%EB%9D%BD%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EC%9B%B9+%EB%84%A4%EC%9D%B4%EB%B2%84%EB%82%A0%EC%94%A8+%EC%A7%80%EC%97%AD&tqi=huFDOdprvmssstnagJosssssswK-502945"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# with open("test.html","w",encoding="utf-8") as f: # html 허용코드범위 파악!
#     f.write(soup.prettify())

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

dust = soup.find("li", attrs={"class":"bx"})
print(len(dust))
