'''A python program to manage tasks.
This program allows user to add tasks, view his tasks, view all tasks.
Furthermore, A superuser 'admin' can register new users, display statistics and generate reports
'''

# Import libraries like date, os.path
import os.path
from datetime import date
from datetime import datetime

# Global variables of the program
today = date.today()
username = ""
password = ""
user_pass = {}

''' This method will register a new user.
1. The user is required to provide username and then password and finally a confirm password.
2. If the user with same name already exists, message is displayed, and user is asked again to enter name.
3. The password and 'confirm password' should match else a message is displayed 
4. If successful then the new user is written into the user.txt file.
'''
def reg_user():
    while True:
        new_username = input("Enter the new username : ")
        if new_username in user_pass:
            print("This username already exists, please provide a different one :")
        else:
            break
    new_password = input("Enter the new password : ")
    new_password_confirm = input("Confirm the new password : ")
    if new_password == new_password_confirm:
        with open('user.txt', 'a') as f:
            f.write("\n" + new_username + ", " + new_password)
    else:
        print("Password does not match with confirm password")

'''This method allows the logged in user to add a new task
1. It will ask few required details from the user
2. The new tasks is added to the tasks.txt
'''
def add_task():
    task_user = input("Enter the username to whom the task is assigned to :")
    task_title = input("Enter the title of the task :")
    task_description = input("Enter the description of the task :")
    task_due_date = input("Enter the due date of the task :")
    task_current_date = today.strftime("%d %b %Y")
    with open('tasks.txt', 'a') as f:
        f.write(
            task_user + ", " + task_title + ", " + task_description + ", " + task_current_date + ", " + task_due_date + ", " + "No" + "\n")

'''This method allows logged in user to view all the tasks for all registered users
This method reads the tasks from 'tasks.txt' file and then displays to the user.
'''
def view_all():
    print("\nDisplaying all tasks :")
    with open('tasks.txt', 'r') as f:
        for line in f.readlines():
            task_items = line.split(", ")
            print("----------------------------------------------------------------")
            print(f"Task:                      {task_items[1]}")
            print(f"Assigned To:               {task_items[0]}")
            print(f"Date assigned :            {task_items[3]}")
            print(f"Due date :                 {task_items[4]}")
            print(f"Task complete :            {task_items[5].strip()}")
            print(f"Task description :         {task_items[2]}")
            print("----------------------------------------------------------------")

'''This method allows the logged in user to view own task
1. It will read all the tasks from 'tasks.txt' and will display only those tasks which are assigned to logged in user
2. While displaying a task it will also display an unique task number for that task.
3. The user can select the tasks number to take further action on tasks or select -1 to go to previous menu
4. The user can either mark the task as completed or can edit the task if it has not been completed yet.
5. If user want to edit the task then , the task can be reassgned to a different user or its due date can be update.
'''
def view_mine():
    print(f"\n{username}, Displaying your tasks :")

    with open('tasks.txt', 'r') as f:
        vm_file_contents = f.readlines()

    vm_my_task_index = 0
    vm_all_task_index = 0
    my_index_mapping_all_index = {}

    for line in vm_file_contents:
        line_task_items = line.split(", ")
        if username == line_task_items[0]:
            print("----------------------------------------------------------------")
            print(f"Task number:               {vm_my_task_index + 1}")
            print(f"Task:                      {line_task_items[1]}")
            print(f"Assigned To:               {line_task_items[0]}")
            print(f"Date assigned :            {line_task_items[3]}")
            print(f"Due date :                 {line_task_items[4]}")
            print(f"Task complete :            {line_task_items[5].strip()}")
            print(f"Task description :         {line_task_items[2]}")
            print("----------------------------------------------------------------")
            my_index_mapping_all_index[vm_my_task_index] = vm_all_task_index
            vm_my_task_index = vm_my_task_index + 1
        vm_all_task_index = vm_all_task_index + 1


    print()
    vm_user_task_number = int(input("Select a task by entering its number or type -1 to go to previous menu:"))
    if  vm_user_task_number == -1 :
        return 1

    vm_task_action = input('''Select the action that you want to take on this task:
           c - Mark it as completed
           e - Edit the task           
           : ''').lower()

    vm_selected_task_line = vm_file_contents[ int(my_index_mapping_all_index.get(vm_user_task_number-1)) ]

    if vm_task_action == 'c':
        vm_selected_task_line = vm_selected_task_line.rsplit(',',1)[0]

        vm_selected_task_line = vm_selected_task_line + ", Yes\n"

        print("\n")

        vm_file_contents[int(my_index_mapping_all_index.get(vm_user_task_number - 1))] = vm_selected_task_line

        with open('tasks.txt', 'w') as f:
            for line in vm_file_contents:
               f.write(line)
    elif vm_task_action == 'e':
        vm_edit_task_user_choice = input('''What would you like to edit:
           u - If you want to edit the username
           d - Due date of the task           
           : ''').lower()
        if vm_selected_task_line.split(',')[-1].strip() == "Yes":
            print("The tas cannot be edited as it has been already be completed.")
            print()
        elif vm_edit_task_user_choice == "u":
            vm_selected_task_line = vm_selected_task_line.split(',', 1)[1]
            vm_edit_task_new_username = input("Please enter the new user to reassign the task :")
            vm_selected_task_line = vm_edit_task_new_username + "," +vm_selected_task_line
            vm_file_contents[int(my_index_mapping_all_index.get(vm_user_task_number - 1))] = vm_selected_task_line
            with open('tasks.txt', 'w') as f:
                for line in vm_file_contents:
                    f.write(line)
            print("The user has been reassigned")
        elif vm_edit_task_user_choice == "d":
            vm_selected_task_line_lst = vm_selected_task_line.split(',')
            print("due date is " + vm_selected_task_line_lst[4])
            vm_edit_task_new_duedate = input("Please enter the new due date for the task :")
            vm_selected_task_line_lst[4] = " " + vm_edit_task_new_duedate
            mystring=""
            mystring_i=0
            for word in vm_selected_task_line_lst:
                if mystring_i < (len(vm_selected_task_line_lst)-1):
                    mystring = mystring + word + ","
                else:
                    mystring = mystring + word
                mystring_i = mystring_i + 1
            vm_file_contents[int(my_index_mapping_all_index.get(vm_user_task_number - 1))] = mystring

            with open('tasks.txt', 'w') as f:
                for line in vm_file_contents:
                    f.write(line)
            print("The task due date has been updated!")
            print()

''' This method will generate reports.
1. It will write the tasks related reports in task_overview.txt
2. It will write the users related reports in the user_overview.txt
3. For tasks report, 
    3.a)it will read from the tasks.txt and store contents in a list
    3.b)it will do some calculations like finding total tasks, number of completed and overdue tasks , respective percentages
    3.c)it will write the results into the task_overview.txt
4. For users report,
    4.a)it will read from user.txt and store all contents in a list
    4.b)it will do some calculations and compute data for all users and all tasks
    4.c)it will compute data for individual users like user's % of tasks, % of completed and overdue tasks
    4.d)it will write results into user_overview.txt 
'''
def generate_reports():
    with open('tasks.txt') as f:
        gr_file_contents = f.readlines()

    gr_comp_tasks_nbr = 0
    gr_noncomp_tasks_nbr = 0
    gr_task_nonoverdue = 0
    gr_task_overdue = 0

    for line in gr_file_contents:
        #print(line.split(",")[-1].strip())
        if line.split(",")[-1].strip() == "No":
            gr_noncomp_tasks_nbr = gr_noncomp_tasks_nbr + 1
        else:
            gr_comp_tasks_nbr = gr_comp_tasks_nbr + 1
        gr_due_date_str = line.split(",")[-2]
        gr_due_date = datetime.strptime(gr_due_date_str.strip(), '%d %b %Y').date()
        #print(f"task due date {gr_due_date}" )
        #today_date_str = date.strftime("%d %b %Y")
        #today_date = datetime.strptime(today_date_str, '%d %b %Y').date()
        if today > gr_due_date and line.split(",")[-1].strip() == "No":
            gr_task_overdue  = gr_task_overdue + 1
            #print("task overdue")
        else:
            gr_task_nonoverdue = gr_task_nonoverdue + 1
            #print("task not overdue")

    with open('task_overview.txt',"w+") as f:
        f.write(f"The total tasks are:                     {len(gr_file_contents)} \n")
        f.write(f"The total completed tasks are:           {gr_comp_tasks_nbr} \n")
        f.write(f"The total not completed tasks are:       {gr_noncomp_tasks_nbr} \n")
        f.write(f"The total overdue tasks are:             {gr_task_overdue} \n")
        f.write(f"The total non overdue tasks are:         {gr_task_nonoverdue} \n")
        f.write(f"The percentage of completed tasks are:   {gr_comp_tasks_nbr/len(gr_file_contents) * 100} \n")
        f.write(f"The percentage of overdue tasks are:     {gr_task_overdue / len(gr_file_contents) * 100} \n")


    #functionality for user_overview.txt
    lst_user_file_contents = []
    with open('user.txt',"r") as f:
        lst_user_file_contents = f.readlines()

    user_tasks = {}
    user_tasks_completed = {}
    for each_task in lst_user_file_contents:
        user_tasks[each_task.split(",")[0].strip()] = 0
        user_tasks_completed[each_task.split(",")[0].strip()] = 0

    for each_task in gr_file_contents:
        user11 = each_task.split(",")[0].strip()
        user11_iscompleted = ""
        if user11 in user_tasks:
            user_tasks[user11] = int(user_tasks.get(user11)) + 1
            if each_task.split(",")[-1].strip() == "Yes":
                user_tasks_completed[user11] = user_tasks_completed.get(user11) + 1


    with open('user_overview.txt', "w+") as f:
        f.write(f"The total number of all the registered users are:  {len(lst_user_file_contents)} \n")
        f.write(f"The total number of all the managed tasks are:     {len(gr_file_contents)} \n")
        for key in user_tasks:
            f.write(f"The total number of tasks assigned to '{key}' are:                           {user_tasks[key]}\n")
            f.write(f"The percentage of total number of tasks assigned to '{key}' are:             {user_tasks[key]/len(gr_file_contents) * 100}\n")
            if user_tasks[key] != 0:
                f.write(f"The percentage of tasks assigned to user '{key}' that have been completed are:            {user_tasks_completed[key] / user_tasks[key] * 100 }\n")
                f.write(f"The percentage of tasks assigned to user '{key}' that have not been completed yet are:    {(user_tasks[key] - user_tasks_completed[key]) / user_tasks[key] * 100}.\n")
            else:
                f.write(f"The percentage of tasks assigned to user '{key}' that have been completed are:    0\n")
                f.write(f"The percentage of tasks assigned to user '{key}' that have not been completed yet are:   0\n")

    print("The reports have bee successfully generated in report files. Please press options 'ds' to view them.\n")

'''This method will view the statistics about the tasks and the users.
1. It will first read the reports and in case report files are not found, it will generate those files by calling generate report function
2. It will display tasks statistics as well as user statistics
'''
def view_statistics():
    if not ( os.path.isfile('task_overview.txt') or os.path.isfile('user_overview.txt') ):
        generate_reports()

    print("------------------Displaying Statistics------------")
    with open('task_overview.txt', 'r') as f:
        for line in f.readlines():
            print(f"{line}", end="")
    with open('user_overview.txt', 'r') as f:
        lineidx = 0
        print(f"--------All user statistics are --------")
        for line in f.readlines():
            lineidx = lineidx + 1
            if lineidx == 3:
                print(f"--------Individual user's statistics are --------")
            print(f"{line}", end="")
    print("--------------Statistics display completed -------------------\n")


#====Login Section====
'''Read the user credentials from the provied file and store them in a dictionary
'''
with open('user.txt') as f:
    for line in f.readlines():
        split_line = line.split(',')
        user_pass[split_line[0]] = split_line[1].strip()

'''This while loop will ask for user credentials and will check them against the user dictionary we created above.
  Continusouly ask for the credentials until user provides the correct one.
'''
while True:
    username = input("Enter the username :")
    password = input("Enter the password :")
    if username in user_pass:
        if user_pass[username] == password:
            print("Login is successful \n")
            break
        else:
            print("Password provided was wrong")
    else:
        print(f"User {username} not found")
#====Login Section completes====

'''This while loop will display menu to the user
 The while loop will continously run until user enters Exit
 The admin user has more options like registering user, generate reports and display statistcs
 Admin and non-admin user, both type have options like adding a task, view my tasks, view all tasks.
 As per the user input an appropriate method will be called. 
 After displaying data from the called method,  the user will again be presented with a menu. 
'''
while True:
    #presenting the menu to the user and
    if username == "admin":
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - Statistics
    e - Exit
    : ''').lower()
    else :
        menu = input('''Select one of the following Options below:            
            a - Adding a task
            va - View all tasks
            vm - view my task
            e - Exit
            : ''').lower()

    if menu == 'r' and username == "admin":
        reg_user()
    elif menu == 'ds' and username == "admin":
        view_statistics()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        generate_reports()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
