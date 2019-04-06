#Importing pyplot
from matplotlib import pyplot as plt
from Mysq import Mysq
from rsidao_mysql import rsidao_mysql


#Plotting to our canvas
#plt.plot([1,2,3],[4,5,1])

#Showing what we plotted
#plt.show()
datear = []
rsiar = []

datear1 = []
rsiar1 = []

mysq = Mysq()
rsidao = rsidao_mysql()
conn = mysq.getConnection()
cursor = conn.cursor()
cursor = rsidao.getrsi10(cursor,"TCS")
data = cursor.fetchall()

for row in data:
    datear.append(row[0])
    rsiar.append(row[9])

plt.plot(datear, rsiar, 'k--', label='TCS', linewidth=2)
#plt.text(datear, rsiar, 'TCS')
#plt.show()

cursor = rsidao.getrsi10(cursor,"INFY")
data = cursor.fetchall()

for row in data:
    datear1.append(row[0])
    rsiar1.append(row[9])

plt.plot(datear1,rsiar1,label='TCS', linewidth=2)
plt.show()