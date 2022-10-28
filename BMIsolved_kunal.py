height=float(input("Please Enter Your Height(Metre) :"))
weight=float(input("Please Enter Your Weight(Kilogram) :"))
bmi=(weight/(height**2))
print("Your BMI is : ")
if(bmi<18.5):
    print(round(bmi, 2),", UnderWeight")
elif(bmi>=18.5 and bmi<25):
    print(round(bmi, 2),", NormalWeight")
elif(bmi>=25 and bmi<30):
    print(round(bmi, 2),", OverWeight")
elif(bmi>=30):
    print(round(bmi, 2),", Obesity")
