import Functions


accounts_list = Functions.read_file('Accounts.txt')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WELCOME<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
count = True
while count:
    choice = int(input('1) Login\n2) Create Account\n3) Exit\n\nchoice>> '))
    if choice == 1:
        Functions.clear_screen()
        try:
        # to enable the option of (ctrl+c) to go back
            Functions.login(accounts_list)
        except KeyboardInterrupt:
            Functions.clear_screen()
    elif choice == 2:
        Functions.create_account(accounts_list)
    elif choice == 3:
        # close the program
        exit()
    else:
        Functions.clear_screen()
        print("ERROR: Wrong choice\n")
