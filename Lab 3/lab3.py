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