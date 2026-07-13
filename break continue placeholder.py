#break
'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(20):
    if i==14:
        break
    print(i)'''

'''a="python"
if a=="h":
    break
print(a)'''#error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    print(a)
    a=a-1'''

'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue'''

'''a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(15):
    if i==7:
        continue
    print(i)'''

'''a="yasaswini"
for i in a:
    if i=="s":
        continue
    print(i)'''
#pass
#placeholder
'''a=30
while a>10:
    print(a)
    a=a-1
    if a==20:
        pass'''

'''for i in range(40):
    if i==10:
        pass
    print(i)'''

# real world project experience
# ATM APPLICATION
'''account = 100000
pwd=1234
card=input("insert the card")
if card == "c":
    print("welcome vijitha")
    password=int(input("enter the password"))
    if password==pwd:
        option=int(input("""choose the option
                            1.balance enquire
                            2.withdraw"""))
        if option==1:
            print("acc balance is",account)
        elif option==2:
            money=int(input("enter the amount"))
            print(money)
            balance=account-money
            print("The remaining amount is",balance)
        else:
            print("invalid option")
    else:
        print("incorrect password")
else:
    print("invalid card")'''
