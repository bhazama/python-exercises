# 1. As a valued customer at the Bank of Honolulu, you make a deposit of $1000. Your savings account balance prior to the deposit has an amount of $8000. Calculate the new savings account balance. Print the new savings account balance and concatenate the dollar sign.
deposit = 1000
savings_balance = 8000
balance = deposit + savings_balance
print("BALANCE: " + "$" + str(balance))
# 2.You need to pay taxes on the $500 cash prize that you won to the IRS ( The tax rate is 30%). Calculate the tax amount and subtract this from your savings balance. Print the updated savings account balance and concatenate the dollar sign.
cash_prize = 500
tax_rate = .30
tax_amount = 500 * .30
new_balance = balance - tax_amount
print("NEW BALANCE: $" + str(new_balance))

# 3. The savings account accrues an annual interest rate of 2%. Calculate the interest earned for the first quarter of 2018, using the original account balance from Question 1. Print the interst earned in the first quarter and concatenate the dollar sign.
interest_rate = .02
quarter_interest_rate = interest_rate / 4
interest_earned = savings_balance * quarter_interest_rate
print("INTEREST EARNED: $" + str(interest_earned))

# 4. Function add
# Create a function that will take two parameters named num1 and num2. This function will add two numbers. Print your result.
def add(num1,num2):
    return num1 + num2
total = add(5,5)
print("ADD: " + str(total))

# 5. Function subtract
# Create a function that will take two parameters named num1 and num2. This function will subtract two numbers. Print your result.
def subtract(num1,num2):
    return num1 - num2
difference = subtract(8,4)
print("DIFFERENCE: " + str(difference))

# 6. Function add-then-subtract
# Create a function that will take in three parameters named num1, num2 and num3. The function will sum up the first two parameters (num1 and num2) and subtract it from the third parameter (num3). Please use your previous functions (i.e. add or subtract) for this exercise. Print your result.
def add_then_sub(num1,num2,num3):
    return subtract(add(num1,num2),num3)
result = add_then_sub(10,10,5)
print("ADD THEN SUB: " + str(result))


# 7. Function shoe size
#  Create a function that will take in a parameter named inches. This function will convert inches to centimeters(cm). Print your result. 
def shoe_size(inches):
    return inches * 2.54
shoes = shoe_size(12)
print("SHOE SIZE: " + str(shoes))
# 8. Create a function that will take in a parameter named cel. The function will convert Celsius into Fahrenheit. Print your result.
def cel_to_far(cel):
    return cel * 1.8000 + 32
temp = cel_to_far(100)
print("FAHRENHEIT: " + str(temp))

# 9. Function all caps
#  Create a function that will take in a parameter named str. This function will capitalize all the letters in the string. Print your result. 
def all_caps(str):
    return str.upper()
caps = all_caps("yelling")
print("ALL CAPS: " + caps)
# 10. Function one cap
#  Create a function that will take in a parameter named str. The function will capitalize only the first letter in the string. Print your result.
def one_cap(str):
    return str[0].upper() + str[1:]
first_cap = one_cap("brendan")
print("FIRST CAP: " + first_cap)
# 11. Use the extend method to combine the following lists together. Print your result.

east_side = ['Biggie', 'Nas', 'Wu-Tang Clan']
west_side = ['Tupac', 'Dre', 'Snoop']
east_side.extend(west_side)
print("BOTH SIDE: " + str(east_side))


# 12. Use the clear method to remove all items from the following list. If you are using Python 2 or 3.2, use the del operator instead. Print your result.

haters = ['Keyshia Cole', 'Wendy Williams', '50 Cent', 'Lil Kim']
haters.clear()
print("CLEAR: " + str(haters))

# 13. Create a function that will print that last digit of an integer. 
def last_digit(num):
    return num % 10
last_num = last_digit(24586974)
print("LAST DIGIT: " + str(last_num))











