import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56",
    "Accept-Language":"ko-KR,ko" #이걸해주면 한글언어로 된 페이지가 있으면 달라고 요청하는 추가코드
    }

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies)) = 0 이라고 뜨네..
print(len(movies)) #헤더넣고 다시 만든거

with open("movie.html","w",encoding="utf-8") as f:
    ######## f.write(res.text) 는 너무 보기힘드네
    f.write(soup.prettify()) #html 문서 이쁘게 출력
    # 여기에.. 영화제목을 검색했는데 안나오네.. reveal 해봤는데 아 영어로 되있구나
    # 접속하는 헤더정보를 통해서 구글무비에서는 서로 다른 페이지를 리턴해주기 때문에.. request로 접속하니 미국으로 주는거 같네
    # 그럼 한글페이지를 받아와야지.. user agent를 통해

################################################
# 헤더 정보넣고 나니까 movie.html에 이제 영화제목검색하니 나오네.. 물론 웹 상에서는 한글이 깨지지만 코드는 멀쩡하니 ㄱㅊ
# !!!! 근데 10개 밖에 안뜨네.! 왜그렇냐면 처음에 영화 10개가 뜨고나서
#업데이트가 되는 식으로 구글 무비가 구성되어있기때문이야
#스크롤을 내릴때마다 더 생기네.. 이런것이 동적페이지라고 불러
#그래서 이제 셀레니움이랑 연동해줘야해
for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
