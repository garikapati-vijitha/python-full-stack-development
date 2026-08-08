# Email automation
# otp authentication
import random
import math
import smtplib #simple mail transfer protocol library

digits="0123456789"
OTP=""#empty string

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your otp"
msg=otp
    
s = smtplib.SMTP("smtp.gmail.com", 587)#standard port number
s.starttls()
s.login("garikapativijithachowdary2004@gmail.com","ayzj rfre btzu awkn")
user="garikapativijitha@gmail.com"
mailid=input("enter the mail which u wanna send otp:")
s.sendmail(user,mailid,msg)

while True:
    a=input("enter the otp")
    if a==otp:
        print("otp is correct")
    else:
        print("Incorrect otp")
