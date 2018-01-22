from watchdao import WatchDAO
watchDAO = WatchDAO()
entry = input("Enter C/R/D -----> ")

if entry == "D":
    watchDAO.delWatch()
elif entry == "C":
    stype = input("Enter the Type of Symbol")
    symbol = input("Enter the Symbol")
    price = input("Enter the price")
    watchDAO.insertWatch(stype, symbol, price)
elif entry == "R":
    cursor = watchDAO.selectWatch()
    for row in cursor:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])