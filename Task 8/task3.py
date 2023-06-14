#used https://pynative.com/print-pattern-python-examples/ to help with task
#outline how many rows are printed
rows = 5
#for loop that prints rows
for i in range(0, rows):
    #for loop to print column
    for j in range(0, i + 1):
        #prints the asterisk
        print("*", end = "")
    print("")