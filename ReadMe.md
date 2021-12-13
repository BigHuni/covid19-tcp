Covid19-TCP
======
웹 크롤링으로 covid-19 웹 페이지의 필요한 정보를 불러와 covid19.json에 주기적으로 저장하고, <br>
TCP통신을 통해 파일을 전송 및 조회하는 프로그램
<br/>
<br/>
[Youtube Link](https://youtu.be/0W2NsviK9Mc)


* **/client/py**
    - client.py = python버전 클라이언트
    - config.env = covid19.json 파일이 저장될 경로를 지정하는 환경변수 파일(자기 PC에서 파일이 저장될 경로로 수정)

* **/client/C**
    - hostip = C++버전 클라이언트


* **/jsonsearch**
    - jsearch.py = 저장된 covid19.json에서 필요한 정보를 불러오는 프로그램

* **/server**
    - search.py = 크롤링 및 json덤프
    - server.py = TCP통신, 스레딩으로 search.py 백그라운드 실행

<br/>
source : [코로나감염증19](http://ncov.mohw.go.kr)

<br/>

사전준비
-
* **모듈**
    - bs4 = 웹 크롤링
    - pytz = KST시간 받는 용도
    - asyncio = 비동기처리 라이브러리
    - schedule = 스케쥴링

> pip install -r requirements.txt

파일이 위치한 디렉토리에서 위 명령어로 한번에 설치할 수 있습니다.
<br/>
<br/>
프로젝트 팀원 : 윤현종, 허대훈, 신임철, 왕현민, 장비, 김정현, 임지웅, 순민기, 김효성
