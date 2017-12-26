from Myemail import Myemail
from Nifty50 import Nifty50

print("Invoked the Daily advanced decline")
nifty50 = Nifty50()
output = nifty50.getnifty50()

file = open("poscont.txt","w")
counter = 0
message = ""
while counter < 5:
    message = output["data"][counter]["symbol"] + "\n"
    file.write(message)
    counter = counter + 1
#print(message)
file.close()

file = open("negcont.txt","w")
counter = 49
#print("inside the neg")
message = ""
while counter > 44:
    #print("inside the counter")
    message = output["data"][counter]["symbol"] + "\n"
    file.write(message)
    counter = counter - 1
#print(message)
file.close()


#myemail = Myemail()
#myemail.send_email("aruna", "aruna", "veera", subject, message)



