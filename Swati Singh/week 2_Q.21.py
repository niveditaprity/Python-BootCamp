# 21. A company decided to give bonus to employee according to following criteria:
      ## Time period of Service        Bonus
      ## More than 10 years             10%
      ## >=6 and <=10                   8%
      ## Less than 6 years              5%
      ## Ask user for their salary and years of service and print the net bonus amount.
salary=int(input("Enter salary: "))
YoS=int(input("Enter years of service: "))
if YoS>10:
    bonus=salary*0.10
elif 6<=YoS<=10:
    bonus=salary*0.08
else:
    bonus=salary*0.05
print("Net bonus amount = ",bonus)
