import mysql.connector


class Mysq:

    def getConnection(self):
        cnx = mysql.connector.connect(user='veerastock', password='veerastock',
                                      host='veerastock.clilr2ftkr50.ap-south-1.rds.amazonaws.com',
                                      database='stock')
        return cnx