height=float(input("Please Enter Your Height(Metre)"))
weight=float(input("Please Enter Your Weight(Kilogram)"))
bmi=(weight/(height**2))
print("Your BMI is : ",bmi)
if(bmi<18.5):
    print(bmi,"UnderWeight")
elif(bmi>18.5 and bmi<24.9):
    print(bmi,"NormalWeight")
eiif(bmi>24.9 and bmi<30):
  print(bmi,"OverWeight")
elif(bmi>30):
    print(bmi,"Obesity)
