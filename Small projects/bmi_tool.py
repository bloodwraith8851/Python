def calculate_bmi(weight, height):
    """ Calculate Body Mass Index (BMI) based on weight and height."""
   # print(calculate_bmi.__doc__)
    bmi = weight / (height ** 2)
    print (f"\nyour Bmi is {bmi:.2f} kg/m^2\n")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print ("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print ("You are overweight.")
    else:
        print ("You are obese.")