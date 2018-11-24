import json


class Stock(object):

    type = ""
    price = 0.0
    change = ""
    buyPrice = 0.0
    qty = 0
    days = 0
    notes = ""

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

    def setBuyPrice(self, buyPrice):
        self.buyPrice = buyPrice

    def setQty(self, qty):
        self.qty = qty

    def setDays(self, days):
        self.days = days

    def getBuyPrice(self):
        return self.buyPrice

    def getQty(self):
        return self.qty

    def getDays(self):
        return self.days

    def getNotes(self):
        return self.notes

    def setNotes(self, notes):
        self.notes = notes

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #                       sort_keys=True, indent=4)