# need to run python file when executing input function (not run code)

set_pw = "0789" # this is the pw set by user
# print (set_pw == pw) # == is to compare if value is exactly the same (if 0789==0789)
# print(f"your pin number is {pw}")
# if pw == set_pw: # pw == set_pw will show as true is pw same
#     print("welcome to private banking services!") # the space in front is impt,dont flush to the side
while True: # this is a loop, need flush everything to the right when using this (highlight and press Tab)
    pw= input("welcome to DBS! please enter your PIN number :") # ALWAYS put below while true
    if pw != set_pw: # != means not equal
        print("sorry your pin number is incorrect, please try again")
    else: 
        print("welcome to private banking services")
        break