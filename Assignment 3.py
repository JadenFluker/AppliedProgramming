try:
    "Get weight in pounds"
    weight = float(input("Your weight: "))

    "Get height in feet and inches"
    height_feet = float(input("The feet part of your height: "))
    height_inches = float(input("The inches part of your height: "))

    "Ensure the values make sense"
    if weight > 0:
        if weight > 1400:
            raise ValueError("Weight must be less than 1400")
    else:
        raise ValueError("Weight must be greater than 0")

    if height_feet >= 0:
        if height_inches < 0 or height_inches >= 12:
            raise ValueError("Inches must be 0-11")
    else:
        raise ValueError("Feet must not be negative")

    "Calculate total height in feet and inches"
    total_height = (height_feet*12)+height_inches

    "Calculate BMI"
    bmi = (weight/(total_height**2))*703
    bmi_rounded = round(bmi, 1)

    "Sort into BMI category"
    if bmi<18.5:
        category = "Underweight"
    elif bmi<=24.9:
        category = "Normal"
    elif bmi<=29.9:
        category = "Overweight"
    else:
        category = "Obese"

    "Print BMI and category"
    print("Your BMI is: ", bmi_rounded)
    print("Your category is: ", category)

    "Source used for BMI information"
    print("Source: https://en.wikipedia.org/wiki/Body_mass_index")

except ValueError as e:
    "Catches inputs that cause errors"
    print("Incorrect value:", e)