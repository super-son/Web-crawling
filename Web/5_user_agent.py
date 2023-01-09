# 3_py 파일 복붙했고 403권한에러 뜰때 취할수 있다.
import requests
url = "https://comic.naver.com/webtoon/detail.nhn?titleId=662774&no=222&weekday=wed"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
res = requests.get(url,headers=headers)
res.raise_for_status() #주석처리 하면 일단 403에러떠도 일단 결과는 볼수 있다 
with open("nadocoing.html", "w", encoding="utf-8") as f:
    f.write(res.text)

# 네이버에 what is my user agent? 타고 들어가서
# 자신의 컴퓨터 유저 에이전트 값을 확인한다.. 브라우저 마다 달라
# 복사해서 데리고 온다
###################################
# 이거 끼우고 다시 하니까 정보를 훨씬 많이 받아오는 모습!!
# 403에러날때 쓴다고 생각하면될듯 ㅋ 위의 예제는 그냥 다 줘서..안되네 ㅋ
