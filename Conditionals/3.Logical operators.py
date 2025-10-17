Strategy = True
Risk_management = True 
Over_trade = False

if Strategy and Risk_management and not Over_trade:
    print("profitable")
else:
    print("not profitable")
print("process done")



High_grade = False
Good_CV = True

if High_grade or Good_CV:
    print("you'll get admission")
else:
    print("you'll not get admission")

high_income = False 
good_credit = True 
student = False 

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
