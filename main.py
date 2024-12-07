h = float(input("Enter height in cm"))
w = float(input("Enter weight in kg"))
BMI = w / (h/100)**2
print("Your BMI is " ,BMI)
if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are serverely overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are serverely obese")
