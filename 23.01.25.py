# my_set = {1,2,3,5,4}
# print(my_set)

# java = {"유재석", "박명수", "김종국"}
# python = set(["유재석", "김태호", "조세호"])
# print(java | python)

# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

#내가 짠 코드
# list_ID = [1,2,3,4,5,6,7,8,9,10]
# chicken_ID = sample(list_ID,1)
# print(chicken_ID)

# print("치킨 당첨자 : " + sample(list_ID, 1))
# print("커피 당첨자 : " + sample(list_ID, 3))

# from random import *
# users = range(1, 21)
# users = list(users)
# shuffle(users)
# winners = sample(users, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {}".format(winners[0]))
# print("커피 당첨자 : {}".format(winners[1:]))
# print("-- 축하합니다 --")

# weather = input("오늘 날씨는 어떤가요? > ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else:
#     print("날씨가 맑습니다. 좋은 하루 보내세요^^")

# temp = int(input("기온이 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요.")
# elif 10 <= temp < 30:
#     print("외출하기 너무 좋은 날씨에요!")
# else:
#     print("날씨가 추워요. 외투를 들고 나가세요.")

# for waiting_no in range(1, 6):
#     print("대기번호 : {}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아메리칸 싸이코"]
# for customers in starbucks:
#     print("{}, 커피가 준비되었습니다.".format(customers))

# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "토르"
# stranger = "unknown"
# while stranger != customer:
#     print("{}, 커피가 준비되었습니다.".format(customer))
#     stranger = input("이름이 어떻게 되세요? ")
#     if stranger == customer:
#         print("기다려 주셔서 감사합니다. 맛있게 드세요.")

absent = [2,5] # 결석자
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {}는 교무실로 따라와.".format(student))
        break
    print("{}, 책을 읽어줘".format(student))