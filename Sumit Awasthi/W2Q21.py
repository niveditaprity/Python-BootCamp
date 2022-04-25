sal = int(input("Enter your salary in rupees: "))
tp = int(input("Enter your timeperiod of service: "))
if tp > 10:
    print("Your bonus amount is:",sal*.10)
elif tp>=6 and tp<=10 :
    print("Your bonus amount is:",sal*.08)
else:
    print("Your bonus amount is:",sal*.05)
