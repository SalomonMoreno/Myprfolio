height = float(input("What is your height in M?\n"))
weight = float(input("What is your weight in kg?\n"))
bmi = int(round(weight/height**2,0))

if bmi <=18.5:
    status = "underweight"
elif bmi <=25:
    status = "normal weight"
elif bmi <=30: 
    status = "slightly overweight"
elif bmi <=35:
    status = "obese"
else: 
    status = "clinically obese"

if status == "normal weight":
    print(f"Your BMI is {bmi}, you have a "+status+".")
else:
    print(f"Your BMI is {bmi}, you are "+status+".")
