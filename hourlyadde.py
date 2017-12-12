from Myemail import Myemail
from Nifty50 import Nifty50

print("Invoked the advanced decline")
nifty50 = Nifty50()
output = nifty50.getnifty50()
advance = output["advances"]
decline = output["declines"]

subject = "Advance: " + str(advance) + " Decline: " + str(decline)

counter = 0
message = " "
while counter < 50:
    message = message + output["data"][counter]["symbol"] + " " + output["data"][counter]["per"] + "\n"
    counter = counter + 1
#print(message)

myemail = Myemail()
myemail.send_email("aruna", "aruna", "veera", subject, message)



