# 퀴즈 8

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type\
            , self.deal_type, self.price, self.completion_year))
        # or print("self.location, self.house_type, self.deal_type, self.price, self.completion_year")

NumberOfHouse = []

a = House("강남", "아파트", "매매", "10억", "2010년")
b = House("마포", "오피스텔", "전세", "5억", "2007년")
c = House("송파", "전세", "월세", "500/50", "2000년")
NumberOfHouse.append(a)
NumberOfHouse.append(b)
NumberOfHouse.append(c)

print("총 {}대의 매물이 있습니다.".format(len(NumberOfHouse)))
for house in NumberOfHouse:
    house.show_detail()