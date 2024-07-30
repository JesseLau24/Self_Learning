# Function is reusable code
def thing():
    print('Hello')
    print('There')

thing()
print('this is called calling the function.')
thing()

# And here is a return function with parameters
def cal_tax(income):
    if income <= 5000:
        tax = 0
    else:
        tax = 0.2 * (income - 5000)
    return tax

# we can store the returned value to a variable,
# and perhaps use it later
tax = cal_tax(23131.78)
print('Tax amount:', tax)

# or print it directly like this
print('Tax amount:', cal_tax(12000))


