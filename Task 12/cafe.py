
#menu list
menu = ["Mocha", "Tea", "Espresso", "Latte"]

#stock dictionary
stock = {"Mocha": 20,
         "Tea": 35,
         "Espresso": 15,
         "Latte": 25
         }

#price dictionary
price = {"Mocha": 3.50,
         "Tea": 4.00,
         "Espresso": 3.00,
         "Latte": 4.50
         }

#variable for final value so for loop can add to it in the first loop
total_stock = 0

#for loop that iterates through menu list and multiplies stock value by price value for the corresponding key
for item in menu:
    total_stock += stock[item] * price[item]

print(total_stock)