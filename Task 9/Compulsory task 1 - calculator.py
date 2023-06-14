
#define a function in order to make the code reusable and robust
def calculator():
 #create variable to ask user to choose between using calculator or viewing text
 choice1 = input("Choose to use the calculator or print all the equations and results from a new txt file. \n c = calculate \n r = read file \n")

 if choice1 == "c":
  #numbers used for calculation and the operation being performed are asked to be input defined as integer when necessary
  #try except block used to prevent value error from occuring by entering non-integer, return stops code from continuing after error
  try:
    num1 = int(input("Enter the first number you would like to calculate with. \n"))
    num2 = int(input("Enter the second number you would like to calculate with. \n"))
  except ValueError as value_error:
    print("You have not entered a valid input")
    print(value_error)
    return
  operation = input("Enter the operation you want to perform on the prior numbers. \n + for addition \n - for subtraction \n / for division \n * for multiplication \n")

#following block deals with addition, subtraction, division and multiplication calculations with if, elif and else statements
  if operation == "+":
    #variable for the answer to the calculation
    addition_answer = num1 + num2
    #variable for the equation calculated so it can be displayed and written to a text file
    addition_equation_var = f"{num1} {operation} {num2} = {addition_answer}"
    print(addition_equation_var)
    #write the same string that is displayed to a text file
    with open("equation.txt", "a") as file:
       file.write(addition_equation_var + "\n")

  elif operation == "-":
    subtract_answer = num1 - num2
    subtraction_equation_var = f"{num1} {operation} {num2} = {subtract_answer}"
    print(subtraction_equation_var)
    with open("equation.txt", "a") as file:
       file.write(subtraction_equation_var + "\n")

#try except block to deal with zero division error
  elif operation == "/":
    try:
     division_answer = num1/num2
     divide_equation_var = f"{num1} {operation} {num2} = {division_answer}"
     print(divide_equation_var)
     with open("equation.txt", "a") as file:
        file.write(divide_equation_var + "\n")
    except ZeroDivisionError:
     print("Cannot divide by zero. \n")


  elif operation == "*":
    multiplication_answer = num1 * num2
    multiplication_equation_var = f"{num1} {operation} {num2} = {multiplication_answer}"
    print(multiplication_equation_var)
    with open("equation.txt", "a") as file:
      file.write(multiplication_equation_var + "\n")

  else:
    print("You have not entered a valid input.")

#choice to read and print from txt file
 elif choice1 == "r":
   #use of while true to ask user for filename again if they enter an incorrect filename
   while True:
     #use of try except to prevent the program from crashing if the txt file does not exist
     try:
      file_input = input("Please enter the filename \n")
      with open("equation.txt", "r") as equation_file:
         equation_file_print = equation_file.read()
     except FileNotFoundError:
      print("File not found")
      break
     if file_input != "equation":
      print("Incorrect filename entered. \n")
      continue
     else:
      break
   print(equation_file_print)
     

calculator()
