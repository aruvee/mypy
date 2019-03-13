class KeyvalueDAO:

    def getValue(self, cursor, key):
        query = "select value from keyvalue where keyname = %s"
        retValue = ""
        data = (key,)
        cursor.execute(query, data)
        allvalues = cursor.fetchall()
        for row in allvalues:
            retValue = row[0]
        return retValue

    # def updateValue(self, conn, key, value):
    #     conn.execute("UPDATE keyvalue SET value=? where key=?", (value, key))
    #     conn.commit()

