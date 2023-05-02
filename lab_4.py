class Human:
    default_name='John Doe'
    default_age=0
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 'homeless'
    def info(self):
        print (self.name, self.age, self.__money, self.__house)
    @staticmethod
    def default_info(default_name=default_name, default_age=default_age):
        print(default_name, default_age)
    def earn_money(self, earned_money):
        self.__money+=earned_money
    def buy_house(self, house, discount):
        newPrice=house.final_price(discount)
        if self.__money < newPrice:
            print('Пополните баланс')
        else:
            self.__make_deal(house, newPrice)
    def __make_deal(self, house, price):
        self.__money=self.__money-price
        self.__house=house
class House:
    def __init__(self, area, price):
        self.__area = area
        self.__price = price
    def final_price(self, discount):
        return discount*self.__price/100
        
class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)
        
Human.default_info()
subject1 = Human('sahar', 20)
subject1.info()
houseSmall=SmallHouse(200)
subject1.buy_house(houseSmall, 50)
subject1.earn_money(200)
subject1.buy_house(houseSmall, 50)
subject1.info()