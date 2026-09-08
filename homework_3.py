TRIP_COST = 20
class TransportCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Вложите корректную сумму!")

    def pay_for_trip(self):
        if TRIP_COST > self.__balance:
            raise ValueError("Недостаточно средств на карте.")
        else:
            self.__balance -= TRIP_COST

card1 = TransportCard("Николай")
card2 = TransportCard("Акылай")

card1.add_money(100)
card2.add_money(40)

print(card1.get_owner())
print(card1.get_balance())
print(card2.get_owner())
print(card2.get_balance())

card1.pay_for_trip()
print(card1.get_balance())

card2.pay_for_trip()
card2.pay_for_trip()
card2.pay_for_trip()
print(card2.get_balance())

try:
    card2.pay_for_trip()
except ValueError as e:
    print(e)

try:
    card1.add_money(-50)
except ValueError as e:
    print(e)
