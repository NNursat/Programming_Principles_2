class StringMethods:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input()

    def printString(self):
        print(self.text.upper())

sm = StringMethods()
sm.getString()
sm.printString()

class Shape:
    def area():
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length 
    
n = Square(5).area()
print(n)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

Rectangle(10, 20).area()

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, " ", self.y)

    def move(self):
        print("na skolko menyaesh x?")
        temp = int(input())
        self.x = self.x + temp
        print("na skolko menyaesh y?")
        temp = int(input())
        self.y = self.y + temp

    def dist(self):
        print(self.x - self.y)


# coordinates = Point()
# coordinates.move()
# coordinates.show()
# coordinates.dist()

class Account:
    def __init__(self, owner = "Richard", balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        print("kanwa deposit salasn?")
        temp = int(input())
        self.balance = self.balance + temp

    def withdraw(self):
        print("kanwa shygarasn?")
        temp = int(input())
        if self.balance - temp < 0:
            print("ty che, u tebya net takih babok")
        else:
            self.balance = self.balance - temp

    def showBalance(self):
        print(self.balance)
        
        
# bank = Account()
# bank.deposit()
# bank.withdraw()
# bank.showBalance()5

is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
numbers = [2, 3, 4, 5, 10, 11, 13, 15, 17, 19, 21, 23]
prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers:", prime_numbers)