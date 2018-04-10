class KeyvalueDAO:

    def getValue(self, conn, key):
        cursor = conn.execute("Select value from keyvalue  where key=?", (key,))
        value = ""
        for row in cursor:
            value = row[0]
        return value

    def updateValue(self, conn, key, value):
        conn.execute("UPDATE keyvalue SET value=? where key=?", (value, key))
        conn.commit()

