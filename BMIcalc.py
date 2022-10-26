height=float(input("Please Enter Your Height(Metre)"))
weight=float(input("Please Enter Your Weight(Kilogram)"))
bmi=(weight/(height**2))
print("Your BMI is : ",bmi)
if(bmi<18.5):
    print(bmi,"You are UnderWeight!")
elif(bmi>18.5 and bmi<24.9):
    print(bmi,"You are healthy :).")
elif(bmi>25 and bmi<29.9):
    print(bmi,"You are OverWeight!")
else:
    print(bmi,"You are Obese!")
