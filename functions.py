# built in functions
#print(abs(-100))

# function from built-in modules that require import keyword
import math #math is a module from python
print (4 ** 1/2 )# want to find the square root of 4
print(math.sqrt(4)) #to use math. you need to import math

# custom function
# assignment : convert meter to km

#def convertMetretoKm(metre) :#def then (name of function)
     #return metre * 0.001

# use the function
#a = convertMetretoKm(1000)
#print(a)

def bmi(weight,height) :
    return weight/height **2

b = bmi (65, 1.78)
print(round(b,2)) # round to 2dp
