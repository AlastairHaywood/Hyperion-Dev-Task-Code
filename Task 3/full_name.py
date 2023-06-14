fullname = input("Please enter your full name. \n")

if len(fullname) == 0:
    print("You have not entered anything. Please enter your full name.")
elif len(fullname) > 1 and len(fullname) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(fullname) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")