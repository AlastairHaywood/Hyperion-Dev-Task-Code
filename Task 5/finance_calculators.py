import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amounbt you'll have to pay on a home loan")

#ask user for input then convert to lowercase so correct answer is not case-sensitive
choice = input("Enter either 'investement' or 'bond' from the menu above to proceed: \n")
choice1 = choice.lower()
 
if choice1 == "investment":

    #variables necessary for the investment calculation. designated as integers where necessary
    mon_depo = int(input("Enter the amount of money you want to deposit. \n"))
    int_rate = int(input("Enter the interest rate. \n"))
    yrs = int(input("Enter the number of years you plan on investing. \n"))
    interest = input("Choose whether you want to calculate simple or compound interest. \n")
    if interest == "simple":
        #calculation for simple investment, rounded to 2 decimal points printed with "£"
        mod_int = int_rate/100
        sim = (mon_depo*(1 + mod_int*yrs))
        #above equation provides total money after interest so minus that from money deposited to get interest gained
        simple_invest = sim - mon_depo
        simple_invest = round(simple_invest, 2)
        #used https://stackoverflow.com/questions/15286401/how-can-i-print-multiple-things-fixed-text-and-or-variable-values-on-the-same for "sep=""" to find out how to remove the automatic spacing between "£" and the value determined by the calculation
        print("£", simple_invest, " is the interest gained from the simple investment method. \n", sep="")
    elif interest == "compound":
        #calculation for compound investment, rounded to 2 decimal points printed with "£"
        mod_int = int_rate/100
        comp = (mon_depo * math.pow((1+mod_int),yrs))
        #above equation provides total money after interest so minus that from money deposited to get interest gained
        compound_invest = comp - mon_depo
        compound_invest = round(compound_invest, 2)
        print("£", compound_invest, " is the interest gained from the compound investment method. \n", sep="")
elif choice1 == "bond":
    #variables necessary for the bond calculation, designated as integers when necessary
    h_val = int(input("Enter the present value of the house. \n"))
    int_rate2 = int(input("Enter the interest rate. \n"))
    mon = int(input("Enter the number of months to repay the bond. \n"))
    if choice1 == "bond":
        #calculation for bonds, rounded to 2 decimal points printed with "£"
        month_int_rate = (int_rate2/100)/12
        bond = (month_int_rate * h_val)/(1 - (1 + month_int_rate)**(-mon))
        bond = round(bond, 2)
        print("£", bond, " is the value that will have to be repaid on the home loan each month. \n", sep="")
else:
    #if anything other than specific parts are entered, generate error message
    print("You have not entered a valid input. \n")