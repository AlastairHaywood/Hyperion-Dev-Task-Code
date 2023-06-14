#used following stack overflow page to help complete task: https://stackoverflow.com/questions/62894271/find-average-with-user-input-under-condition-until-user-press-enter-without-valu
#creating variables for calculating the mean
count = 0
sum = 0

while True:
    num = input("Enter a number. \n")
    if num != "-1":
        #if number is not -1 it is added to the sum variable
        sum = sum + int(num)
        #if number is not -1 the count variable increases by 1 which ensures that -1 is not included in the average calculation
        count += 1
    else:
        #when -1 is chosen, loop stops
        break

#f in print function allows to input variables in {}, after above while loop has finished then print 
print(f"Average: {sum/count}")