import math
from index import Index


class MyGann:

    def getGannValues(self, stype, symbol):
        index = Index()
        gannlist = []

        current = index.getStockPrice(stype, symbol)
        sqrtvalue = int(math.sqrt(current))
        starting = sqrtvalue - 1
        #print(starting)

        # Formulate the
        gannlist.append(starting ** 2)
        counter = 0
        while counter < 3:
            secondCounter = 1
            while secondCounter < 9:
                value = (starting + (secondCounter * 0.125)) ** 2
                gannlist.append(value)
                secondCounter = secondCounter + 1
            counter = counter + 1
            starting = starting + 1

        #print(gannlist)
        listcount = len(gannlist)

        listcounter = 0
        index = 0
        while listcounter < listcount:
            # print(gannlist[listcounter])
            if current < gannlist[listcounter]:
                index = listcounter
                break
            listcounter = listcounter + 1

        # print(index)
        buylist = []
        selllist = []
        newcounter = 5
        while newcounter >= 0:
            buylist.append(round(gannlist[index - 1 + newcounter], 0))
            newcounter = newcounter - 1
            selllist.append(round(gannlist[index - 1 - newcounter], 0))

        return buylist + selllist
