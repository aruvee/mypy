from Mysq import Mysq
from keyvaluedao_mysql import KeyvalueDAO

class KeyValueService:

    def updateKeyValue(self, key, value):
        mysq = Mysq()
        keyValueDao = KeyvalueDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        keyValueDao.updateValue(cursor,key,value)
        conn.commit()
        conn.close()