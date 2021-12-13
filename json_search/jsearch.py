#저장된 covid19.json파일 읽어서 쓸만한 데이터 가져오는 코드
import json, os

all = ["전체", "all", "a"]
quit = ["종료", "quit", "exit", "q"]

def get_data(date: str, arg):
    jpath = os.getcwd()
    with open(f"{jpath}/covid19.json", "r") as f:
        data = json.load(f)
    for info in data[str(date)]:
        return info[arg]

def date_data(date, data):
    try:
        total = get_data(date, 'total')
        isol = get_data(date, 'isol')
        deisol = get_data(date, 'deisol')
        death = get_data(date, 'death')
        tenM = get_data(date, 'tenM')
        if data == 'total':
            print(total)
        elif data == 'isol':
            print(isol)
        elif data == 'deisol':
            print(deisol)
        elif data == 'isol':
            print(death)
        elif data == 'isol':
            print(f"{tenM}%")
        elif data == 'all':
            print(f"누적 확진자 : {total}명\n격리 : {isol}명\n격리해제 : {deisol}명\n사망 : {death}명\n10만명당 발생률 : {tenM}%")
    except KeyError:
        print("해당 날짜에 값이 존재하지 않습니다.")

def table(cur):
    print(cur)
    while True:
        try:
            date = int(input("[검색할 날짜]\n>>"))
            if date == 0:
                break
            else:
                if cur == '누적 확진자':
                    date_data(date, 'total')
                elif cur == '격리중':
                    date_data(date, 'isol')
                elif cur == '격리해제':
                    date_data(date, 'deisol')
                elif cur == '사망자':
                    date_data(date, 'death')
                elif cur == '10만명당 발생률':
                    date_data(date, 'tenM')
                elif cur == 'all':
                    date_data(date, 'all')
        except ValueError:#타입오류 예외 처리
            print("정수 형태의 숫자를 입력해주세요.(뒤로가기:0)")


def main():
    while True:
        try:
            cur = str(input("[검색할 정보]\n>>"))
            if cur in all:
                table('all')
            elif cur == '누적':
                table('누적 확진자')
            elif cur == '격리':
                table('격리중')
            elif cur == '격리해제':
                table('격리해제')
            elif cur == '사망':
                table('사망자')
            elif cur == '비율':
                table('10만명당 발생률')
            elif cur in quit:
                print('종료중...')
                break
            else:
                print('---명령어 목록---\n전체, 누적, 격리, 격리해제, 사망, 비율')
        except ValueError:#타입오류 예외 처리
            print("ValueError")

main()