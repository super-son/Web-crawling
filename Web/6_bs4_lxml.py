# pip install beautifulsoup4
# pip install lxml 부터 해줘 구문분석하는 parsel 기능   
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() # 이상시 에러발생

soup = BeautifulSoup(res.text, "lxml")
# # 가져온 res 문서를 lxml parsel을 통해 b-s 객체로 만든거
# print(soup.title) #parsel 하니까 이렇게 골라서 가져올수 잇네
# print(soup.a.get_text()) # a 안에서 text만 뽑아줍니다.
# print(soup.meta) #아 근데 다 고르는건아니고 제일 처음발견되는거!!!!
# print(soup.a.attrs) #a의 속성을 보여줌..
# print(soup.a["href"]) #a의 href 속성값을 출력하네
## 근데 요거는 페이지에 대한 이해도가 높을때 사용
###########################################

# # 내가 버튼정보를 따오고 싶어서 정보를 확인해보니
# # 클래스가 주어져d있으니 이를 이용할것으로 판단
# # 밑 문장 해석해보면 저 이름의 클래스중 a태크를 띈 제일 첫번째 아이
# 다 찾으려면 find_all을 사용해주면 되
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find(attrs={"class":"Nbtn_upload"})) #이렇게도 가능

# attrs는 말그대로 코드 내 속성값이므로 xpath는 속성값이 아니잖니
# 적혀있는 클래스명이나 고유의 속성값을 적어보면 가져오구나

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a) # a만 솎아낸다.
# print(rank1.a.get_text()) #a라는 최소단위에서 text를 솎아내는거구나
# print(rank1.next_sibling) #형제위치(최소단위)의 정보 출력. 아무것도 안나오는경우는
# #개행코드 \n이 숨어있기때문에 이럴땐
# print(rank1.next_sibling.next_sibling) # 두번적어준다
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.next_sibling #이건 방향성이 반대
# print(rank1.parent) #부모태그 소환
# 자 근데 next_sibling.next_sibling 보다 확실한 코드 나간다
############################################

# 개행이 있든 없든~
# rank2 = rank1.find_next_sibling("li") # 다음으로 가는데 li인거 찾을때까지
# print(rank2.a.get_text())
# print(rank1.find_next_siblings("li")) #이건 이제 다음 형제들을 모두 가져오는 개꿀팁

############################################
webtoon = soup.find("a",text="급식아빠-3화 너 내가 보여?") # 이 텍스트를 가진 a태그를 데려오는 코드
print(webtoon)