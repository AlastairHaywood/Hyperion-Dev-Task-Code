swim = input("Enter the time taken to finish the swimming section in minutes. \n")
cycle = input("Enter the time taken to finish the cycling section in minutes. \n")
run = input("Enter the time taken to finish the running section in minutes. \n")

#specified int in the next line to allow the variables to be added together numerically as opposed to being printed sequentially
total = int(swim) + int(cycle) + int(run)
print("Your total time is", total)

if total <= 100:
    print("You have recieved the Provincial Colours award.")
elif total > 100 and total <= 105:
    print("You have recieved the Provencial Half Colours award.")
elif total > 105 and total <= 110:
    print("You have recieved the Provincial Scroll award.")
else:
    print("You have not qualified for an award.")