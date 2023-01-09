import requests
res = requests.get("http://google.com")
#######1번
print("문제없는지 응답코드 :", res.status_code)
# 200이면 이상무
# 403이면 페이지 접근 권한이 없음. 다른방법으로 스크래핑
#######2번
if res.status_code == requests.codes.ok : #200과 같은 뜻
    print("정상입니다")
else :
    print("문제가 생겼습니다. [ 에러코드", res.status_code, "]")
#######3번
res.raise_for_status() #애도 비슷한 기능으로
# 만약 올바르게 정보를 가지고오지 못한다면 에러를 내버림
print("웹 스크래핑을 진행합니다")
# 얘랑 조합해서 두줄컷가능
# res = requests.get("http://naver.com")
# res.raise_for_status()
########################################################################3
print(len(res.text)) #문서의 글자 갯수
#파일을 만들고 text만 보여주기.. 익스플로 열어봐
with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)
