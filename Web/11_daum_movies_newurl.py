# 다음 이미지에서 우클릭 사진저장이 안되면 사진 클릭하고 클릭해서 최종단계 까지가면
# 저장을 할 수 있는데 이때 f12코드는 이미지 코드이고 이전은 a href 주소 코드이다
# 내가 봤을때 request를 한번 더 해줘야하는 거 구분은 이미지 저장을 할수없다 + src 코드가 완전하지않다
import requests
from bs4 import BeautifulSoup

for i in range(2015,2020): #2015-2020년 대표작
    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images): #enumerate가 들어온다고 특별해지는게 아니고 for구문에서 저것과 idx정보만 착취
        image_url = image["src"]
        if image_url.startswith("//"): #~로 시작한다면
            image_url = "https:" + image_url
        #image_url을 따내고 다시 request로 접속해서 이미지정보를 따낸다
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        # 이름에서 쓸려고 idx를 뽑아낸거구만~
        with open("movie_{}_{}.jpg".format(str(i)+"년",idx+1), "wb") as f: #다음에서 jpg로 제공하더래요. 근데 png로도 되는디 ㅎ
            f.write(image_res.content) #파일에 정보의 내용을 쓴다
        if idx >= 0: #1-5위 까지의 사진만 받고 받지않겠다
            break
