# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "박명수", "나이" : 26, "취미" : ["축구", "코딩", "볼링"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("taero.text", "w", encoding="utf8") as kk:
#     kk.write("파이썬을 열심히 공부하고 있어요")

# with open("taero.text", "r", encoding="utf8") as kk:
#     print(kk.read())

# for i in range(51):
#     with open("{}주차.txt".format(i), "w", encoding="utf8") as taero:
#         taero.write("{} 주차 주간보고".format(i))
#         taero.write("\n부서 : ")
#         taero.write("\n이름 : ")
#         taero.write("\n업무 요약 : ")
#     with open("{}주차.txt".format(i), "r", encoding="utf8") as taero:
#         print(taero.read())

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")

# 클래스

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음

# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크2"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 하지만 실제로는 이보다 훨씬 더 많은 유닛이 있을 수 있으며 유닛마다 이렇게
# 프로그램을 일일이 짜줄 수 없다.

# class Unit:
#     def __init__(self, name, hp, damage): # __init__ : 파이썬에서 객체가 만들어질 때 쓰이는 생성자
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
# marine1 = Unit("마린", "40", "5")
# marine2 = Unit("마린", "40", "5")
# tank1 = Unit("탱크", "150", "35")

# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린/ 등을 수송. 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스        
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
        
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
Valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
Valkyrie.fly(Valkyrie.name, "3시")
    

