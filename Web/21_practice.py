a = "안녕하세요	어	반갑고	너는누구니	아니야".split("\t")
print(a)
b = "안녕하세요  어  반갑고  너는누구니  아니야".split("  ")
print(b)
# a는 csv파일의 -> 모양의 띄어쓰기 인데 \t와 호환하네
# b는 스페이스 두개줫어!
a="얘들아 반가워"
b="12345"
if a.startswith("얘"):
    print("ji")
###########################################
datas = soup.find("table",attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, data in enumerate(datas):
    datas2 = data.find_all("td")
    print("==============매물 {}==============".format(index+1))
    print("거래 : ", datas2[0].get_text())
    print("공급/전용면적 : ", datas2[1].get_text())
    print("매물가(만원) : ", datas2[2].get_text().strip(),"만원") #개행문자 없애주는 
    print("동 : ", datas2[3].get_text())
    print("층 : ", datas2[4].get_text()) 

x path id값은 크롬이 잘되어있어서 크롬을 쓰자!
full path로 진짜주소를 가져올수도 있지..
requests 라이브러리는 문서의 정보를 받기위함이다
############################33####################
if __name__ == "__main__":
    scawd() #라고 했을때 이걸 직접실행하면 함수가 실행되고
    # 다른 파일에 의해서 실행되면 함수실행을 하지않는 코드

.get_text().replace("도정섭","") # 이렇게 마음에 들지않는 텍스트도 없애줄수있지
그리고 {"class":""} # 이건 나머지애들 클래스 잇고 나 없을때 이렇게 찾는거 ㄹㅈㄷ
dust = soup.find("dl",attrs={"Calss":"indicatro"},text="미세먼지") # 클래스가 저거 이면서 text로 미세먼지인것을 찾음
dust = soup.find("dl",attrs={"Calss":["indicatro","hi"]}) # 클래스가 이거 이거나 저거 인거 찾아줌
dust = soup.find("dl",attrs={"Calss":["indicatro","hi"],"id"="dust"}) #위 조건 or id가 dust인것도

