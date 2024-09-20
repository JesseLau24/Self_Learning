# Temperature Checker
temperature = float(input('Input Temperature: '))
if temperature < 35:
    print('A bit too cold.')
elif 35 <= temperature <= 37:
    print('You are alright.')
else:
    print('Possibily fever.')

# Holidy Bonus Calculator
years = int(input('HNumber of Years Worked: '))
salary = float(input('Monthly Salary: '))
if years > 2:
    bonus = (years - 2) * 0.15 * salary
else:
    bonus = 0
print(f'Your Christmas bonus is: ${bonus}.')

# Order the number
num1 = int(input('1st number: '))
num2 = int(input('2nd number: '))
num3 = int(input('3rd number: '))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num3, num2, num1)
    else:
        print(num2, num3, num1)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num3, num1, num2)
    else:
        print(num3, num1, num2)
elif num3 >num1 and num3 > num2:
    if num1 > num2:
        print(num2, num1, num3)
    else:
        print(num1, num2, num3)