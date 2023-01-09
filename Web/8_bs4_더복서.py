import requests
from bs4 import BeautifulSoup

#밑에 네줄 필수코드
url = "https://comic.naver.com/webtoon/list.nhn?titleId=736989&weekday=thu"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td",attrs={"class":"title"})
title = cartoons[0].a.get_text() #리스트니까 첫번째꺼 볼려고
print(cartoons[0])
linnk = cartoons[0].a["href"]
link2 = cartoons[0].a["onclick"] #속성가져오려면 대괄호
print(title)
print("https://comic.naver.com" + linnk)
# 터미널에 있는 링크 컨트롤 누르면서 클릭하니까 들어가지네 ㄷ

# 만화 제목 + 링크
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 가져오기
# total_rates = 0
# cartoons = soup.find_all("div", attrs={"class":"rating_type"}) #여기서 나열되는 쟤들은 같은 계급이라고 생각
# for cartoon in cartoons:
#     rate = cartoon.strong.get_text()
#     # rate = cartoon.find("strong").get_text() #같다잉
#     print(rate)
#     total_rates += float(rate)
# print("전체점수 : ", total_rates)
# print("평균점수 : ", total_rates / len(cartoons))