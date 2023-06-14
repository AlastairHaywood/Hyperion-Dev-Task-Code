#used https://www.geeksforgeeks.org/python-alternate-cases-in-string/ to help inform answer to task
#choose between alternate character capitalisation and alternate word capitalisation
choice = input("Choose charcter or word capitalisation change \n character = alternate upper and lower capitalisation of string \n word = alternate words captialised \n")

if choice == "character":
#variable for a user input string
 user_string_char = input("Input string \n")
 #empty string for new string
 new_string = ""
 #for loop to iterate over the string
 for i in range(len(user_string_char)):
    #if character position is even then the letter is added to a new string and changed to lowercase, else it is changed to uppercase
    if i % 2:
        new_string = new_string + user_string_char[i].lower()
    else:
        new_string += user_string_char[i].upper()

 print(new_string)

#used https://stackoverflow.com/questions/74547765/making-each-alternative-word-lower-and-upper-case to help solve problem

elif choice == "word":
 #empty string for new string
 #variable used to help iterate through input string
 input_string = input("Enter a string \n")
 word_string = ""
 word = 1
 #for loop to iterate through input string which is split into a list, removing all whitespace
 for i in input_string.split():
    if word != 1:
       word_string += " "
    #if variable is even change to upper case else change to lowercase
    if word % 2 == 0:
       word_string += i.upper()
    else:
       word_string += i.lower()
    word += 1
 
 print(word_string)