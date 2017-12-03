class Myemail:
    def __init__(self):
      #print ("Calling parent constructor")
    def subject(message, current, reference):
        return message + " " + str(current) + "/" + str(reference)
    def send_email(self,user, pwd, recipient, subject, body):
        import smtplib
        #Read the buy file and get the data
        file = open("email.txt","r")
        flag="false"
        counter=0
        for line in file:
            line=line.strip()
            #print(line)
            if counter==0:
                user=line
            if counter==1:
                pwd=line
            if counter==2:
                recipient=line
            if counter==3:
                flag=line
            counter=counter+1
        file.close()
        #flag="false"
        gmail_user = user
        gmail_pwd = pwd
        FROM = user
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body
        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
        if flag=="true":
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                server.close()
                print("successfully sent the mail")
            except Exception as e: print(e)
