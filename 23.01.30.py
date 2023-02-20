gun = 20

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내]남은 총 : {0}".format(gun))
    
# def checkpoint(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내]남은 총 : {0}".format(gun))
#     return soldiers, gun
    
# print("전체 총 : {}".format(gun))
# # checkpoint(2)
# soldiers, gun = checkpoint(gun, 2)
# print("남은 총 : {0}, 순찰나간 군인 수 : {1}".format(gun, soldiers))

# gender = ["남자", "여자"]

# def std_weight(height, gender):
#     if gender == "남자":
#         weight = height/100 * height/100 * 22
#     else:
#         weight = height/100 * height/100 * 21
#     return weight, height, gender

# weight, height, gender = std_weight(175, "남자")
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

# gender = ["남자", "여자"]

# def std_weight(height, gender):
#     if gender == "남자":
#         weight = round(height/100 * height/100 * 22, 2)
#         print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))
#     else:
#         weight = round(height/100 * height/100 * 21, 2)
#         print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))
        
# std_weight(173, "남자")

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
    
# height = 173
# gender = "여자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

# import sys
# print("Python", "Java", "JavaScript", file = sys.stdout)
# print("Python", "Java", "JavaScript", file = sys.stderr)

# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(4), str(score).rjust(4), sep = ":")

# 은행 대기 순번표
# 001, 002, 003, ~~
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")