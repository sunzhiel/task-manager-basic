# This is a task management application designed for a small business.
# It works with 2 text files in which are stored user login details &
# allocated tasks respectively. The program can read & write data
# from & to these files.

# Import required libraries.
import datetime

# Login Section
# Handle login requests by creating an empty dictionary and reading
# usernames and associated passwords into it from user text file.
login_details = {}
with open("user.txt", "r") as users:
    for line in users:
        # Remove the new line character to prevent errors.
        user_prep = line.strip("\n")

        if user_prep != "":
            key, value = user_prep.split(", ")
            login_details[key] = value

# Request user to login.
username = input("Please enter your username: ")
password = input("Please enter your password: ")
print()

# Make sure that username and password are the correct key/value pair.
if username in login_details:
    passcode = login_details[username]
else:
    passcode = 0

# Use while loop to users are guided to provide correct
# login details. Display error messages if otherwise.
while True:
    if username not in login_details or password != passcode:
        print("You entered an invalid username and/or password! Try again.")
        print()
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        print()
        if username in login_details:
            passcode = login_details[username]
        elif username not in login_details:
            passcode = 0

    
    else:
        print(f"Login successful. Welcome, {username}!")
        print()
        break

# Set admin priviledges.
if username == "admin":
    admin_privilege = True
else:
    admin_privilege = False

# Display 2 different menu versions depending on whether
# user has admin privileges or not.
# Use while loop to manage menu navigation.
while True:
    if admin_privilege == True:

        menu = input('''Select one of the following options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
d - Display statistics
e - Exit
: ''').lower()

    else:
        menu = input('''Select one of the following options below:
a - Add a task
va - View all tasks
vm - View my tasks
e - Exit
: ''').lower()

# This menu option is visible only to those with admin privileges.
# It allows them to register new users. Implement a check for
# admin rights to make sure only authorised users can use this.
    if menu == 'r':
        if admin_privilege == True:
            print()
            new_user = input("Please enter a username for the new user: ")
            print()
            while True:
            # Make sure duplicate user names are not allowed.
                if new_user in login_details:
                    print("This username is already in use. Try again")
                    print()
                    new_user = input("Please enter a username for the new user: ")
                else:
                    new_pass = input(f"Please enter a password for {new_user}: ")
                    pass_check = input("Please type in the password again: ")
                    print()
                    while True:
                    # Check that new password is confirmed accurately.
                        if new_pass != pass_check:
                            print("The passwords do not match! Try again")
                            print()
                            new_pass = input(f"Please enter a password for {new_user}: ")
                            pass_check = input("Please type in the password again: ")
                        else:
                            print()
                            print(f"New user {new_user} added!")
                            print()
        

# Write new user login details to user text file.
                            with open("user.txt", "a") as user_reg:
                                user_reg.write("\n")
                                user_reg.write(f"{new_user}, {new_pass}")
                                break
                break         
        else:
            print() 
            print(f"You do not have admin privileges, {username}! Try something else.")
            print()

# This menu option is for assigning new tasks to users.
    elif menu == 'a':
        print()
        assignee = input("Please enter the username of the person you are assigning this to: ")
        print()
        task_title = input("Enter a title for the task: ")
        print()
        description = input("Please enter a description of the task: ")
        print()

# Get the current date using datetime module and format as appropriate.
        date_today = datetime.date.today()
        date_assigned = date_today.strftime("%d %b %Y")
        print(f"Today\'s date is {date_assigned}.")
        print()
        due_date = input("Please enter the task due date in the format dd mmm yyyy: ")
        task_status = "No"

# Write new task details to tasks text file in the prescribed format.
        with open("tasks.txt", "a") as new_task:
                            new_task.write("\n")
                            new_task.write(f"{assignee}, {task_title}, {description}, {date_assigned}, {due_date}, {task_status}")

# This menu option allows users to view all tasks.
    elif menu == 'va':
        print()
        task_count = 1
        with open("tasks.txt", "r") as tasks:
            for line in tasks:
                task_prep = line.strip("\n")

# Display a user friendly view of task details.
                if task_prep != "":
                    task = task_prep.split(", ")
                    print(f"Task {task_count}")
                    print("________________________________________________________")
                    print(f"Task:            {task[1]}")
                    print(f"Assigned to:     {task[0]}")
                    print(f"Date assigned:   {task[3]}")
                    print(f"Due date:        {task[4]}")
                    print(f"Task complete?   {task[5]}")
                    print("Task description:")
                    print(f"  {task[2]}")
                    print("________________________________________________________")
                    task_count += 1
                    print()
        
# With this menu option, we display only the tasks allocated to the current user.
    elif menu == 'vm':
        print()
        task_count = 0
        with open("tasks.txt", "r") as task_list:
            for line in task_list:
                task_prep = line.strip("\n")

                if task_prep != "":
                    task = task_prep.split(", ")
                    if username == task[0]:
                        task_count += 1
                        print(f" My Task {task_count}")
                        print("________________________________________________________")
                        print(f"Task:            {task[1]}")
                        print(f"Assigned to:     {task[0]}")
                        print(f"Date assigned:   {task[3]}")
                        print(f"Due date:        {task[4]}")
                        print(f"Task complete?   {task[5]}")
                        print("Task description:")
                        print(f"  {task[2]}")
                        print("________________________________________________________")
                        print()
        if task_count == 0:
            print(f"{username}, you have no tasks assigned to you!")
            print()
                    

# This is another menu option reserved for users with admin privileges.
# It gives a high level overview of users and tasks.
    elif menu == 'd':
        if admin_privilege == True:
            print()
            task_counter = 0
            with open("tasks.txt", "r") as task_overview:
                for line in task_overview:
                    task_prepz = line.strip("\n")

                    if task_prepz != "":
                        task_z = task_prepz.split(", ")
                        task_counter += 1
            print("Statistics - users & tasks")
            print("_____________________________________________")
            print(f"Total number of tasks: {task_counter}")

            user_counter = 0
            with open("user.txt", "r") as user_overview:
                for line in user_overview:
                    user_prepz = line.strip("\n")

                    if user_prepz != "":
                        user_y = user_prepz.split(", ")
                        user_counter += 1
            print(f"Total number of users: {user_counter}")
            print("_____________________________________________")
            print()

# Discourage any users trying to access secret menu options.
        else:
            print() 
            print(f"You do not have admin privileges, {username}! Try something else.")
            print() 

# Option to log out and exit menu.
    elif menu == 'e':
        print()
        print(f"Goodbye, {username}!!!")
        exit()

# Error message for invalid inputs.
    else:
        print("You have entered an invalid choice. Please try again!")
        print()