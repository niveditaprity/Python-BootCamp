mp = int(input("Enter the marked price: "))
if mp > 10000:
    print("You have to pay:",mp-(mp*.2),"only.")
elif mp>7000 and mp<=10000 :
    print("You have to pay:",mp-(mp*.15),"only.")
else:
    print("You have to pay:",mp-(mp*.1),"only.")
