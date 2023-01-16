# a data structure is used to hold multiple values
# 2 types of data structure in python: list and dictionary
"""
the idea: 
when we access data from internet, it is usally stored as dictionary.
when we access data from excel or CSV files, it is stored as list.
once you master these 2 data structures, we can proceed to 
real applications of using python!
"""

#--- example of multiple values using a list  ---#
name = ["andy", "candy", "mandy"]
age = [24, 25, 33]

# example of single value variables:
name1 = "andy"
name2 = "candy"
name3 = "mandy"
age1 = 24
age2 = 25
age3 = 33


# --- list --- #
# basic properties: [], mutable object, index and slice []
# very basic methods : append(), pop(), sort()
# there are more methods not covered here. refer to PFB contents

# a simple list
list_nation = ["singapore", "malaysia", "indonesia", "thailand"]

# nested list (list within a list)
list_nation2 = [["singapore", 5000], ["malaysia", 10000], ["indonesia", 30000], ["thailand", 8000]]

# index values from list
print(list_nation[0]) #will print singapore 0 = singapore, 1 = malaysia and so on
print(list_nation2[0]) #will print ['singapore, 5000'] 0 = singapore,5000 1 = malaysia,10000 and so on

# append more values to a list
list_nation.append("vietnam") # to add something else into a list
print(list_nation)

# sort values in a list
# note that sort has 2 parameters but we won't be talking about them here.
# refer to PFB contents
list_nation.sort() # A to Z or what not i think, not sure tho go see brightspace

print(list_nation)

# --- practical example of using list  --- #

# create a empty list to store values
empty_list = [] 
print(empty_list) # will print [] if empty

# FYOU means For Your Own Understanding

# use a for loop to iterate over a list
for nation in list_nation2:
    print(nation) # prints out ['singapore',5000]
    print(nation[0]) # prints out singapore
    print(nation[1]) # FYOU: check what is nation[1]
    
    # filter nations with <= 8000 in population
    if nation[1] <= 8000:
        # use append() to add the nation to empty list
        empty_list.append(nation[0])
    
print(empty_list)

# ---- dictionary - key/value pair --- #
# basic properties: {}, mutable, index and slice []
# basic methods: get(), keys(), values()
# there are more methods not covered here. refer to PFB contents
# for simplicity, we will use [] to index and slice

# create a simple dictionary
dict_nation = {
                "singapore": 5000,
                "malaysia": 10000,
                "indonesia":30000,
                "thailand":8000
                }

# check output
print(dict_nation)
# print keys 
print(dict_nation.keys()) 
# print values
print(dict_nation.values())
# print a value of a key
print(dict_nation["singapore"])
# assign new value to a key
dict_nation["indonesia"] = 1

# you can use either way to get a value from a key
print(dict_nation["singapore"]) # index method  
print(dict_nation.get("singapore")) # get() method

# -- practial example of dictionary -- #

# create an empty dict to store values
empty_dict = {}

# use a for loop to iterate over dictionary
# nation in this a temporary variable that represents the key of a dict
for nation in dict_nation:
    print(nation) # prints out the keys
    print(dict_nation[nation]) # prints out the value
    
    # filter nations with <= 8000 in population
    if dict_nation[nation] <= 8000:
        # add the key/value pair to the empty dictionary
        empty_dict[nation] = dict_nation[nation]

print(empty_dict)

