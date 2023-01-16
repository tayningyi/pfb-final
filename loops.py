
# say you want to print number 0 to 4, 
# instead of rpeating print statements 4 times, you can write with loops
# print(0)
# print(1)
# print(2)
# print(3)
# print(4)

# ---- WHILE LOOP -----#

# create a variable and assigned a value of 0
number = 0

while number < 5: #while function tells u if number is < than 5, number = the value in line 13

    print(number) #must have 4 indentations

    number += 1 #add number by 1


# ---- FOR LOOP with range() -----#

# create a range of numbers 0 to 5
num0to4 =  range(5) #5 is the stop position, wont print 5

for num in num0to4:

    print(num)






# ---- FOR LOOP with enumerate() -----#
country = "singapore"
for index, char in enumerate(country,1):
    print(index, char)





#---- Example of using for loop ----#
# Given a bank loan amount with a fixed interest rate of monthly 1.00% 
# how much interests do you need to pay for a loan period of 6 months?

loan_amt = 1000
duration = 6
total_interest = 0
interest_rate = 0.01

for year in range(duration):
    total_interest += loan_amt * interest_rate
    
print(total_interest)

