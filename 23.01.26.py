# students = list(range(1,11))
# students = [i+100 for i in students]
# print(students)

# students = ["Iron Man", "Thor", "Ultra man"]
# # students = [len(i) for i in students]
# students = [i.upper() for i in students]
# print(students)

#Quiz 5

# from random import *
# time = list(range(5,51))
# shuffle(time)
# customer = list(range(1,51))
# customer_1 = list(range(5,16))
# # customer_1 = [for i in customer_1]
# while customer == 50:
#     print("{0}번째 손님 (소요시간 : {1}분".format(customer,time))
#     cutomer += 1
#     if customer ==50:
#         print("총 탑승 승객 : {}분".format(customer_1.count()))

# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님(매칭 성공)
#         print("[O] {0}번째 손님 (소요시간 : {1}분".format(i, time))
#         cnt += 1
#     else: # 매칭 실패
#         print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))
               
# print("총 탑승 승객 : {}분".format(cnt))


# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {}분".format(cnt))

def open_account():
    print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 불가능합니다. 현재 잔액은 {}원입니다.".format(balance))
        
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


def deposit(balance, money):
    print("{0}원 입금이 완료되었습니다. 현재 잔액은 {1}원입니다.".format(money,balance + money))
    return balance + money

def withdraw(balance, money1, money2):
    if balance >= money1 + money2: 
        print("보험료 {0}원이 출금되었습니다. 카드대금 {1}원이 출금되었습니다. 현재 잔액은 {2}원입니다.".format(money1, money2, balance - money1 - money2))
    else:
        print("현재 잔액이 부족합니다. 출금이 불가합니다. 현재 잔액은 {}원입니다.".format(balance))
    return balance - money1 - money2

def withdraw_night(balance, money, commission):
    return commission, money, balance - money - commission


balance = 5000000
balance = deposit(balance, 3000000)
balance = withdraw(balance, 1000000, 2000000)
commission, money, balance = withdraw_night(balance, 4500000, 1000)
print("수수료는 {0}원입니다. {1}원이 출금되었습니다. 현재 잔액은 {2}원입니다.".format(commission, money, balance))


















