import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_I_others_english&keywd=haceng_submain_lnb_lec_I_others_english&logger_kw=haceng_submain_lnb_lec_I_others_english"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# with open("test.html","w",encoding="utf-8") as f: # html 허용코드범위 파악!
#     f.write(soup.prettify())
script_datas = soup.find("div", attrs={"class":"conv_container"}).find_all("span", attrs={"class":"conv_sub"})
print("[오늘의 영어회화지문 - 해커스영어]")
s_data=[]
for script in script_datas :
    s_data.append(script.get_text())
####################print문##############################
print(s_data[4])
print(s_data[0])
print(s_data[5])
print(s_data[1])
print(s_data[6])
print(s_data[2])
print(s_data[7])
print(s_data[3])


