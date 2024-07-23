# Get user location
choice = input('1 if in Europe, 2 fin American: ')

# Europe to American
if choice == '1':
    euro_floor = int(input('which floor: '))
    am_floor = euro_floor + 1
    print(f"This is {am_floor} floor in US")

# American to Europe
elif choice == '2':
    am_floor = int(input('which floor: '))
    euro_floor = am_floor - 1
    print(f"This is {euro_floor} floor in US")

# Error Message
else:
    print('Wrong input!')