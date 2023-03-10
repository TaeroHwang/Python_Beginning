# [모듈] : 필요한 것들끼리 부품처럼 만드는 것 / 함수 정의나 클래스 등 파이썬 문장들을 담고 있는 파일
# 모듈은 모듈을 사용하려는 파일과 같은 경로(폴더)내에 있어야 사용 가능하다.

# 일반 가격

def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))
    
# 조조 할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))
    
# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))