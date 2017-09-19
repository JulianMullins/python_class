def calculate_bmi(weight, height):

    bmi = 703 * weight / (height * height)

    if bmi < 18.5:
        print('You are underweight')
    elif bmi >= 18.5 and bmi < 25:
        print('You are at a normal weight')
    elif bmi >= 25 and bmi < 30:
        print('You are overweight')
    else:
        print('You are obese')

weight = float(input('What is your weight in pounds? '))
height = float(input('What is your height in inches? '))
calculate_bmi(weight, height)