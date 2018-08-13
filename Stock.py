class Stock(object):

    type = ""
    price = 0.0
    change = ""

    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setChange(self, change):
        self.change = change

    def getChange(self):
        return self.change