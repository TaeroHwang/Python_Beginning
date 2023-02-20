# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 :{2}"\
#         .format(name, age, main_lang))
    
# profile("유재석", 20, "Python")
# profile("조세호", 20, "Java")

# 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 :{2}"\
#         .format(name, age, main_lang))
    
# profile("유재석")
# profile("김태호")

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}".format(name, age), end = " ")
#     for lang in language:
#         print(lang, end = " ")
#     print()
    
# profile("유재석", 25, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 20, "Kotlin", "Swift")

gun = 19

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun, soldiers

print("전체 총 : {}".format(gun))
gun, soldiers = checkpoint_ret(gun, 2)
print("남은 총 : {0}, 순찰 군인 수 : {1}".format(gun, soldiers))