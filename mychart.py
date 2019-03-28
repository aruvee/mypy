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

mysq = Mysq()
rsidao = rsidao_mysql()
conn = mysq.getConnection()
cursor = conn.cursor()
cursor = rsidao.getrsi10(cursor,"TCS")
data = cursor.fetchall()

for row in data:
    datear.append(row[0])
    rsiar.append(row[9])

plt.plot(datear,rsiar)
plt.show()