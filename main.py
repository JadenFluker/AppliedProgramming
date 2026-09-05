weight = float(input("Your weeight: "))
height_feet = float(input("The feet part of your height: "))
height_inches = float(input("The inches part of your height: "))
total_height = (height_feet*12)+height_inches
bmi = (weight/(total_height**2))*703
bmi_rounded = round(bmi, 1)

if bmi<18.5:
    category = "Underweight"
elif bmi<=24.9:
    category = "Normal"
elif bmi<=29.9:
    category = "Overweight"
else:
    category = "Obese"

print("Your BMI is: ", bmi_rounded)
print("Your category is: ", category)


print("Source: https://en.wikipedia.org/wiki/Body_mass_index")