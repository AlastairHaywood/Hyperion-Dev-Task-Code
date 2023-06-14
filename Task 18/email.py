### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:

    #constructor
    def __init__(self, email_addess, subject_line, email_content):

        self.email_address = email_addess
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    # Declare the class variable, with default value, for emails. 
    has_been_read = False

    # Initialise the instance variables for emails.
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
    

# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox_list = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():

    # Create 3 sample emails and add it to the Inbox list. 
    email1 = Email("email1@email.com", "email subject 1", "email contents 1")
    email2 = Email("email2@email.com", "email subject 2", "email conents 2")
    email3 = Email("email3@email.com", "email subject 3", "email contents 3")
    
    inbox_list.append(email1)
    inbox_list.append(email2)
    inbox_list.append(email3)


def list_emails():
    #Create a function which prints the email’s subject_line, along with a corresponding number.
    #enumerate starts count at 0

    for position, i in enumerate(inbox_list, 0):
        print(f"{position}: {i.subject_line}")

def read_email(index):
    # Create a function which displays a selected email.
    #to make a list starting at 1 work, minus the index by one in the f-string due to python being 0-indexed

    print(f"Email number {index}: \n{inbox_list[index].email_address} \n{inbox_list[index].subject_line} \n{inbox_list[index].email_content} \n")

    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    print(f"\nEmail from {inbox_list[index].email_address} \nNumber: {index} \nhas been marked as read! \n")

    inbox_list[index].has_been_read = True


# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: \n'''))
       
    if user_choice == 1:
        #add logic here to read an email

        list_emails()

        #try block to catch user entering not an integer
        try:
            index = int(input("\nEnter the corresponding number to read the email \n"))

        except  ValueError:
            print("\nYou have not entered a number, try again. \n")
            continue
        
        read_email(index)
        

    elif user_choice == 2:
        
        for t in inbox_list:
            if t.has_been_read == False:
                print(f"{t.subject_line}")


    elif user_choice == 3:
        print("\n Goodbye! \n")
        break

    else:
        print("Oops - incorrect input.")