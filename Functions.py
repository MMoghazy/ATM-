

#This module contains the defination of all the function for the application

#including packages we need
import os
import time


try:
    # read the 'Accounts.txt' file
    # if you try to open non existing file in read mode, this will throw an error
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    # if 'Accounts.txt' file is not found, create it
    f = open('Accounts.txt', 'w')
    f.close()


#This function clear the output of the screen
def clear_screen():
    os.system('clear')
    print()  # print blank line after clearing the screen


#This function is to read a file and return a list
def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)
    return lines_list

#This function is to show some processes and it's called in the show history function
def print_process(process):
    date = '{}'.format(process[2:7])
    print('{0}\t{1}\t{2}{3: ^10} {4: ^10}'.format(
        process[0],
        process[1].center(len('change_password')),
        date.center(len(date)),
        process[7],
        process[8]
    )
    )

#This function is to withdraw money
def withdraw(ls):
    # ls is a list of the information of the account
    # ls[0] id
    # ls[1] name
    # ls[2] password
    # ls[3] balance

    current_balance = int(ls[3])
    # make changes to another variable to keep the previous balance unchanged in ls[3]
    # to print it later, then save ls[3] = current_balance
    print('Your current balance: ' + ls[3])

    withdraw_amount = int(input('Enter withdraw amount: '))

    if withdraw_amount > current_balance:
        print("ERROR: You can't withdraw more than your current balance")
    else:
        current_balance -= abs(withdraw_amount)  # to guarantee the entered value

    file_name = ls[0] + '.txt'
    process_list = read_file(file_name) #opening the file of a certain user containig all it's processes or creating a new one if it's his first time
    id_file = open(file_name, 'a') #opening it in the append mode to modify on it without losing any previous data

    if len(process_list) == 0:
        # if there are no processes in the file
        last_id = 1
    else:
        last_id = int(process_list[len(process_list)-1][0]) + 1
        # get last id and increment it
    #writing the data of the last process in the file of a specific client
    id_file.write('{0}\twithdraw\t\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), ls[3], str(current_balance)))
    id_file.close()
    ls[3] = str(current_balance)
    print('Your current balance: ' + ls[3])

    return ls

#This function is to deposit money
def deposit(ls):
    # ls is a list of the information of the account
    # ls elements are of type string
    # ls[0] id
    # ls[1] name
    # ls[2] password
    # ls[3] balance
    current_balance = int(ls[3])  # make changes to another variable to keep the previous balance
    # to print it later, then save ls[3] = current_balance
    print('Your current balance: ' + ls[3])
    deposit_amount = int(input('Enter deposit amount: '))


    current_balance += abs(deposit_amount)  # to guarantee the entered value

    file_name = ls[0] + '.txt'
    process_list = read_file(file_name)
    id_file = open(file_name, 'a')

    if len(process_list) == 0:  # if there are no processes in the file
        last_id = 1
    else:
        last_id = int(process_list[len(process_list) - 1][0]) + 1  # get last id and increment it

    id_file.write('{0}\tdeposit\t\t\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), ls[3], str(current_balance)))
    id_file.close()
    ls[3] = str(current_balance)
    print('Your current balance: ' + ls[3])

    return ls

#This function is to show the history of the previous processes
def show_history(ls):
    # ls is the list contains account data
    # ls[0] id
    # ls[1] name
    # ls[2] password
    # ls[3] balance

    choice = int(input('1) show deposit processes\n2) show withdraw processes\nchoice>> '))

    file_name = ls[0] + '.txt'
    id_list = read_file(file_name)

    # id_list[line][0]    process_id
    # id_list[line][1]    process_type
    # id_list[line][2:6]  process_date
    # id_list[line][7]    before_process
    # id_list[line][8]    after_process
    top_line = '\nID\t' + 'Type'.center(len('change_password')) + 'Date and Time'.center(40) + 'before'.center(10) + 'after'.center(15)
    print(top_line)
    print('-' * len(top_line))
    if choice == 1:
        for line in id_list:
            if line[1] == 'deposit':
                print_process(line)
    elif choice == 2:
        for line in id_list:
            if line[1] == 'withdraw':
                print_process(line)
    else:
        print('ERROR: Wrong choice')

    input('\nPress Enter to go back..')
    os.system('clear')


#This function is to login to your account
def login(acc_list):

    login_id = input('Please, Enter your info(press "Ctrl+C" to go back) \n>>ID: ')
    login_password = input('>>Password: ')
    found = False
    #this loop is to search for the account if it exists or not
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            found = True
            menu2(account)
            break
        else:
            continue

    if not found:
        clear_screen()
        print('Wrong ID or Password')
        login(acc_list)

    else:
        acc_file = open('Accounts.txt', 'w')
        print('Saving changes...')
        # after logging out of the account
        # write changes to accounts.txt file
        for acc in acc_list:
            for elements in acc:
                acc_file.write("%s\t" % elements)
            acc_file.write('\n')

#This function is to create an account for the first time
def create_account(ls):
    # ls is a list of lists of lines in accounts file
    # ls is the accounts_list
    account_name = input('Enter Your Name (WITHOUT SPACES): ')
    account_password = input('Enter Your Password (WITHOUT SPACES): ')

    print("Creating Your Account .....")
    accounts_file = open('Accounts.txt', 'a')

    if len(ls) == 0:
        new_last_id = 1
    else:
        new_last_id = int(ls[len(ls) - 1][0]) + 1

    line = '{0}\t{1}\t{2}\t0\n'.format(str(new_last_id), account_name, account_password)

    accounts_file.write(line)
    id_file_name = str(new_last_id) + '.txt'
    id_file = open(id_file_name, 'w')

    print("Your Account Has Been Created And Your Id Is " + str(new_last_id))
    id_file.close()
    accounts_file.close()
    ls.append([str(new_last_id), account_name, account_password, '0'])


#This function is to handle each specific user
def menu2(account):
    # account is the list of single logined user
    # account[0] id
    # account[1] name
    # account[2] password
    # account[3] balance
    print("\n---------Hello, {0}--------- ".format(account[1]))
    while True:
        ch = int(input("\n1) show info \n2) show process history\n3) deposit\n4) withdraw\n5) logout\n\nchoice>> "))

        clear_screen()
        if ch == 1:
            print("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))

        elif ch == 2:
            show_history(account)
        elif ch == 3:
            deposit(account)
        elif ch == 4:
            withdraw(account)
        elif ch == 5:
            break
        else:
            print("ERROR: Wrong choice\n")
