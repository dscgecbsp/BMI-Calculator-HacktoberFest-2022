height=float(input("Please Enter Your Height (Metre)"))
weight=float(input("Please Enter Your Weight(Kilogram)"))
Bmi=(weight/(height**2))
print("Your BMI is : ",Bmi)
if(Bmi<18.5):
    print(Bmi,"UnderWeight")
elif(Bmi>18.5 and Bmi<24.9):
    print(bmi,"NormalWeight")
eiif(Bmi>24.9 and Bmi<30):
  print(Bmi,"OverWeight")
elif(bmi>30):
    print(Bmi,"Obesity)
