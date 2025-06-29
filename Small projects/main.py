from bmi_tool import calculate_bmi # import the calculate_bmi function from the bmi_tool module

print("Welcome to the BMI Calculator!")  # print a welcome message

weight = float(input("Please enter your weight in kg: "))  # take weight input from the user
height = float(input("Please enter your height in meters: "))  # take height input from the user

calculate_bmi(weight, height)