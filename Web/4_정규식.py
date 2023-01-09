# 주민등록번호의 형식
# 111111-1111111
# 이메일 주소의 형식
# 차량번호의 형식 등
# 식의 형식에 부합하는지!!
import re
p=re.compile("ca.e") #여기서 .은 하나의 문자를 의미
#case cafe cake등을 다 검색할수 있는거지
# (ca.e) : 하나의 문자 / care, cafe, cake...
# (^de) : 문자열의 시작 / desk, destine... / fade(X)
# (se$) : 문자열의 끝 / case, base.. / face(X)

def print_match(m):
    # m = p.match("caffe")
    # print(m.group()) #매치되지 않으면 에러가 발생
    if m : # 매치되었을때
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:",m.string) # 입력받은 문자열 반환, 애는 함수가아니라 변수
        print("m.start():",m.start()) # 일치하는 문자열의 시작인덱스
        print("m.end():",m.end()) # 일치하는 문자열의 끝인덱스
        print("m.span():",m.span()) #일치하는 문자열의 시작과 끝 인덱스

    else : #에러안내고 메세지주기
        print("매치되지 않음")

m = p.match("cake") #careless도 매치됨, nocareless는 매치안됨
print_match(m)

m2 = p.search("nocareless cake") #search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m2) #애는 nocareless도 매치됨

m3_list = p.findall("careless cafe") #일치하는 모든 것을 리스트 형태로 반환
print(m3_list)
