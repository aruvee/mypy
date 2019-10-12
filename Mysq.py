import mysql.connector


class Mysq:

    def getConnection(self):
        cnx = mysql.connector.connect(user='veera', password='veera',
                                      host='13.233.94.163',
                                      database='stock')
        return cnx
