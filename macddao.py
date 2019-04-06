from datetime import datetime


class macddao:

    def insert(self, cursor, fdate, symbol, day0, day1, day2, day3, day4, day5, type):
        query = "INSERT INTO macd_archive (fdate,stock,day0,day1,day2,day3,day4,day5,type) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (fdate, symbol, day0, day1, day2, day3, day4, day5, type)
        cursor.execute(query, data)


