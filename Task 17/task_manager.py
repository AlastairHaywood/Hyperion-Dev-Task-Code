
#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

#created a function to call the main menu in order to return to it
def main_menu():
    while True:
    # presenting the menu to the user and 

    # making sure that the user input is converted to lower case.
     print()
     menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

     if menu == 'r':
        reg_user()

     elif menu == 'a':
        add_task()

     elif menu == 'va':
        view_all()

     elif menu == 'vm':
        view_mine()
        
     elif menu == "gr":
        generate_reports()        

     elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''

        create_tasks_file()
        create_user_file()
        
        #opens text files and readlines() creates a list with each line as an element
        with open("user.txt", "r") as file_user:
            disp_stats_users = file_user.readlines()

        with open("tasks.txt", "r") as file_task:
            disp_stats_tasks = file_task.readlines()

        #len of the list gives the number of elements which is the number of users and tasks
        print("-----------------------------------")
        print(f"Number of users: \t\t {len(disp_stats_users)}")
        print(f"Number of tasks: \t\t {len(disp_stats_tasks)}")
        print("-----------------------------------")    

     elif menu == 'e':
        print('Goodbye!!!')
        exit()

     else: 
        print("You have made a wrong choice, Please Try again")


def reg_user():
    '''Add a new user to the user.txt file'''
    #while loop that prevents the user entering a duplicate username
    while True:
        new_username = input("New Username: ")
        if new_username in username_password.keys():
            print("Username already exists. Try again. \n")
        else:
            break

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
            
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            #write file line taken out of for loop so the file is written once the for loop has finished and not for every iteration
            out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


#function to input due date
def input_due_date():
    #while loop used to ensure correct format is used when input
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD: \n")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified \n")
    
    return due_date_time


def add_task():
    #while loop that prevents the user adding a task to a user that doesnt exist
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else:
            break

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    due_date_time = input_due_date()

    #then get current date
    curr_date = date.today()
    ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)

    write_to_task_file(task_list)

    print("Task successfully added. \n")

#function that returns the current day (datetime format)
def get_current_day():
    return datetime.today()


#function to write to the tasks.txt file
def write_to_task_file(task_list):
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


def view_all():

    #prevents errors if no tasks exist
    if total_num_tasks() == 0:
        print("No tasks to view! \nYou can create tasks by selecting 't' at the main menu. \n")
    
    else:
        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)


#function to print the selected task from the task lit
def print_task(t, task_num):
        
        disp_str = f"Task number:\t {task_num}\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        disp_str += f"Completed: \t {t['completed']}\n"
        print(disp_str)


#function that displays all tasks that have that users username 
def view_mine():

    #prevents errors if no tasks exist
    if total_num_tasks() == 0:
        print("\nNo tasks to view! \nYou can create tasks by selecting 't' at the main menu \n")
    
    else:

    #for loop that iterates through the task list and printing every task associated with the current user
    #also numbers the tasks

        task_num = 0
        for t in task_list:
                task_num += 1
                if t['username'] == curr_user:
                    print_task(t, task_num)

        #while loop that allows the user to return to the main menu. Leads on to editing the tasks via the task_editor()
        #try block for catching not integer
        while True:
            try:
                select_task = int(input("Enter the task number to select a task, or enter -1 and return to the main menu \n"))
            except ValueError:
                print("\nNot a number \n")
                continue

            #allows user to return to main menu
            if select_task == -1:
                main_menu()

                #this function uses the input number as the index for the task
            elif task_list[select_task -1]['username'] == curr_user:
                break

            else:
                print("\nTask associated with that number does not exist. \nOr you do not have access to that task. \nPlease try again. \n")

        task_editor(select_task)

#function that edits the tasks, 'completed' and 'due_date'
def task_editor(select_task):
    #task numbers start at 1 although python is 0-indexed so minusing 1 equates them
    task_num = select_task
    task_index = task_num -1

    #re-print the selected task for better responsiveness and user experience
    print_task(task_list[task_index], task_num)

    is_complete = input("Is this task complete? yes or no. \n").lower()

    #if user enters yes the task is changed to complete in the list and then written to the text file
    if is_complete == "yes":
        task_list[task_index]['completed'] = True
        write_to_task_file(task_list)
        print_task(task_list[task_index], task_num)

        #prevents the user from editing tasks marked as complete
    elif task_list[task_index]['completed'] == False:     

            edit_date = input("Do you want to edit the date? yes or no \n")
            if edit_date == "yes":

                new_date = input_due_date()
                #edits the list to the new date
                task_list[task_index]['due_date'] = new_date

            edit_username = input("Do you want to edit the username? yes or no. \n").lower()
            if edit_username == "yes":
                new_username = input("Enter the new username: \n")

                #logic that checks whether the new username is a user that exists in the dictionary
                if new_username not in username_password.keys():
                    print("\nUser does not exist! \n")
                    main_menu()

                #edits the list to the new username
                task_list[task_index]['username'] = new_username
    else:
        #prevents tasks from being edited if the task is marked as complete
        print("\nYou cannot edit a task that has been marked as complete. \n")
        main_menu()

    #writes changes to the task list text file from the task_list
    write_to_task_file(task_list)


def generate_reports():
    #generate appropriate text files if they dont exist
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as default_file:
            pass

    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as default_file:
            pass
    #calls functions to populate the text files with data
    generate_task_overview()
    generate_user_overview()


def generate_task_overview():
    
    #logic that prevents zero division errors by returning 0
    total_tasks = total_num_tasks()

    if total_tasks == 0:

        comp_tasks = 0
        incomplete_tasks = 0
        incomp_and_overdue_tasks_var = 0
        percent_incomp = 0
        percent_overdue = 0

    else:
        comp_tasks = total_number_of_comp_tasks()

        incomplete_tasks = total_tasks - comp_tasks

        incomp_and_overdue_tasks_var = incomplete_and_overdue_tasks()

        percent_incomp = percentage_incomp_tasks()

        percent_overdue = percentage_overdue()


    #variable to write to the file
    task_overview = f'''\nTask overview:
The total number of tasks: \t {total_tasks}!
The total number of completed tasks: \t {comp_tasks}!
The total number of incomplete tasks: \t {incomplete_tasks}!
The total number of overdue and incomplete tasks: \t {incomp_and_overdue_tasks_var}!
The percentage of incomplete tasks: \t {percent_incomp}%!
The percentage of overdue tasks: \t {percent_overdue}%!
'''
    
    #writes the task_overview variable to the task_overview.txt text file
    with open("task_overview.txt", "w") as file:
        file.write(task_overview)


def generate_user_overview():

    total_tasks = total_num_tasks()

    user_overview = f'''\nUser Overview:
    The total number of users: \t {total_num_users()}!
    The total number of tasks: \t {total_tasks}! \n'''

    with open("user_overview.txt", "w") as file:
        file.write(user_overview)


    for i in username_password.keys():

        #following prevents zero division error by setting variable to 0 if total task and total user tasks is 0
        if total_tasks == 0:
        
            user_task_number = 0
            percent_of_total_assign_user = 0
            percent_comp_task_user = 0
            percent_incomp_task_user = 0
            percent_incomp_and_overdue_task_user = 0

        else:
            user_task_number = total_tasks_assign_to_user(i)

            percent_of_total_assign_user = percentage_of_total_assign_to_user(i)

            percent_comp_task_user = percentage_tasks_assign_user_comp(i)

            percent_incomp_task_user = percentage_tasks_assign_to_user_incomp(i)

            percent_incomp_and_overdue_task_user = percentage_tasks_assign_to_user_incomp_and_overdue(i)

        if user_task_number == 0:

            percent_comp_task_user = 0
            percent_incomp_task_user = 0
            percent_incomp_and_overdue_task_user = 0

        else:

            percent_comp_task_user = percentage_tasks_assign_user_comp(i)

            percent_incomp_task_user = percentage_tasks_assign_to_user_incomp(i)

            percent_incomp_and_overdue_task_user = percentage_tasks_assign_to_user_incomp_and_overdue(i)

        user_overview_for_loop = f'''
    User: \t {i}
    The total number of tasks assigned to user: \t {user_task_number}!
    The percentage of the total number of tasks that have been assigned to user: \t {percent_of_total_assign_user}%!
    The percentage of the tasks assigned to user that have been completed: \t {percent_comp_task_user}%!
    The percentage of the tasks assigned to user that have not been completed: \t {percent_incomp_task_user}%!
    The percentage of the tasks assigned to user that have not been completed and are overdue: \t {percent_incomp_and_overdue_task_user}%!
    '''
        
        #writes the user_overview variable to the user_overview.txt text file
        with open("user_overview.txt", "a") as file_for_loop:
            file_for_loop.write(user_overview_for_loop)


#function that returns the total number of tasks tracked by the software
def total_num_tasks():
    return len(task_list)


#function that returns the total number of completed tasks by iterating through the task list and adding to a counter for every task with True in the 'completed' field
def total_number_of_comp_tasks():
    total_number_of_comp_tasks = 0
    for t in task_list:
        if t['completed'] == True:
            total_number_of_comp_tasks += 1
    return total_number_of_comp_tasks


def total_num_incomp_tasks():
    return total_num_tasks() - total_number_of_comp_tasks()


#function that returns all the incomplete and overdue tasks by iterating through the task list and adding to a counter for every task that is marked as not complete and the date today is later than the due date
def incomplete_and_overdue_tasks():
    incomp_overdue_tasks = 0
    for t in task_list:
        if t['completed'] == False and t['due_date'] < get_current_day():
            incomp_overdue_tasks += 1
    return incomp_overdue_tasks


#function that returns the percentage value of tasks that are incomplete by using the total number of incomplete tasks function and the total number of tasks function and performing a calculation to determine the percentage

#result is rounded to one decimal place
def percentage_incomp_tasks():

    percentage_incomp = 100 * total_num_incomp_tasks() / total_num_tasks()

    return round(percentage_incomp, 1)


#function that returns the percentage value of tasks that are overdue by using the incomplete and overdue function and the total number of tasks function and performing a calculation to determine the percentage

#result is rounded to one decimal place
def percentage_overdue():

    percentage_overdue = 100 * incomplete_and_overdue_tasks() / total_num_tasks()

    return round(percentage_overdue, 1)


#returns the total number of users by taking the length of the username_password dict keys
def total_num_users():
    return len(username_password.keys())


#function that returns the total tasks that have been assigned to the user that is logged in by iterating through the task list and adding to a counter for each task with the current users username
def total_tasks_assign_to_user(i):
    user_task_number = 0
    for t in task_list:
        if t['username'] == i:
            user_task_number += 1
    return user_task_number


#function that returns the percentage of the total tasks assigned to the user that is signed in by using the total tasks assigned to user function and total number of tasks function

#and performing a calculation to determine the percentage value

#result is rounded to one decimal place
def percentage_of_total_assign_to_user(i):

    percentage_of_total_assign_to_user = 100 * total_tasks_assign_to_user(i) / total_num_tasks()
    return round(percentage_of_total_assign_to_user, 1)


#function that returns the percentage of the tasks assigned to the user that are complete by iterating through and using a counter for each task that is completed and is assigned to the current user

#then uses the total number of tasks function to calculate the percentage value
def percentage_tasks_assign_user_comp(i):
    num_of_tasks_assign_to_user_comp = 0
    for d in task_list:
        if d['completed'] == True and d['username'] == i:
            num_of_tasks_assign_to_user_comp += 1

    return round(100 * num_of_tasks_assign_to_user_comp / total_tasks_assign_to_user(i), 1)
    

#function that returns the percentage of tasks assigned to the current user that are incomplete by using a counter that increases for every task that is not completed and assigned to the current user

#uses the total tasks assigned to user function for the percentage value calculation
def percentage_tasks_assign_to_user_incomp(i):
    num_of_tasks_assign_to_user_incomp = 0
    for d in task_list:
        if d['completed'] == False and d['username'] == i:
            num_of_tasks_assign_to_user_incomp += 1

    return round(100 * num_of_tasks_assign_to_user_incomp / total_tasks_assign_to_user(i), 1)


#function that returns the percentage of the tasks assigned to the current user and are incomplete and overdue by iterating through the task list and using a counter that increases for every task

#that is completed and the current date is later than the due date and the username is the same as the current user

#uses the total tasks assigned to user function to determine the percentage value
def percentage_tasks_assign_to_user_incomp_and_overdue(i):
    incomp_overdue_tasks = 0
    for t in task_list:
        if t['completed'] == False and t['due_date'] < get_current_day() and t['username'] == i:
            incomp_overdue_tasks += 1
    
    return round(100 * incomp_overdue_tasks / total_tasks_assign_to_user(i), 1)
    

#function that creates a tasks.txt file if it does not already exist
def create_tasks_file():
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass


#function that creates a user file if one does not already exist
def create_user_file():
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")


#====Read Section====

# Create tasks.txt if it doesn't exist
create_tasks_file()

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
create_user_file()

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


main_menu()