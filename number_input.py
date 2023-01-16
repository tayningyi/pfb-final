#create a program to convert km to miles
#1km = 0.6213688756 miles

mile_input = float(input('enter your running distance in KM:')) #written as string
km_to_mile = 0.6213688756 #float
convert = mile_input * km_to_mile #km input times miles conversion
print(f"your running distance is {convert} miles") #curly bracket is where your variable will go 
print(f'your running distance is {round(convert,3)} miles') #round = round to how many decimals uw

