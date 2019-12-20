from Pattern import Pattern
from datetime import datetime
from Mysq import Mysq
from macddao import macddao
from macdabsdao import macdabsdao
from macdabzdao import macdabzdao
from macdbesdao import macdbesdao
from macdbezdao import macdbezdao
from daoplongleg import daoplongleg


# Initialize the class
pattern = Pattern()
mysq = Mysq()
macddao = macddao()
macdbezdao = macdbezdao()
macdbesdao = macdbesdao()
macdabzdao = macdabzdao()
macdabsdao = macdabsdao()
daoplongleg = daoplongleg()

conn = mysq.getConnection()
cursor = conn.cursor()

# ABS
allstocks = macdabsdao.selectArchive(cursor)
allstocks = allstocks.fetchall()

for row in allstocks:
    macddao.insert(cursor, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'ABS')

macdabsdao.delete(cursor)

# ABZ

allstocks = macdabzdao.selectArchive(cursor)
allstocks = allstocks.fetchall()

for row in allstocks:
    macddao.insert(cursor, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'ABZ')

macdabzdao.delete(cursor)

# BES

allstocks = macdbesdao.selectArchive(cursor)
allstocks = allstocks.fetchall()

for row in allstocks:
    macddao.insert(cursor, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'BES')

macdbesdao.delete(cursor)

#BEZ

allstocks = macdbezdao.selectArchive(cursor)
allstocks = allstocks.fetchall()

for row in allstocks:
    macddao.insert(cursor, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'BEZ')

macdbezdao.delete(cursor)


#LongLeg
allstocks = daoplongleg.selectArchive(cursor)
allstocks = allstocks.fetchall()

for row in allstocks:
    macddao.insert(cursor, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'LLD')

daoplongleg.delete(cursor)

conn.commit()
conn.close()