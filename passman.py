# https://pynative.com/python-create-file/
import hashlib
import os
import os.path
import getpass

destination_folder = "C:\\01110011110\\"


def login():

    def login_opt():
        choice = input("""\nWhat do you want to do?
                       
View passwords (1)
Add new password (2)
Sign out (3)
          
> """)

        if choice == "1":
            with open(destination_folder + user + " " + pass1 + ".txt", 'r') as account:
                for line in account:
                    print(line.split()[0:2])

            if os.stat(destination_folder + user + " " + pass1 + ".txt").st_size == 0:
                print("\nADD A PASSWORD TO YOUR ACCOUNT FIRST.")
                login_opt()
            else:
                pass

            prompt = input(
                "\nGet the plain password (enter the master password) Exit (2): ")

            if os.path.exists(destination_folder + user + " " + pass1 + " " + prompt + ".txt"):
                with open(destination_folder + user + " " + pass1 + " " + prompt + ".txt", 'r') as account2:
                    for line in account2:
                        print(line.split()[0:2])

            elif prompt == "2":
                login_opt()

            else:
                print("\nMASTER PASSWORD INCORRECT.")

            login_opt()

        elif choice == "2":
            new_account = input("\nEnter the new account: ")
            password = input("Enter the password for the account: ")

            hashed = hashlib.md5(password.encode()).hexdigest()

            mastered = input(
                "\nInput your account's master password to confirm: ")

            if os.path.exists(destination_folder + user + " " + pass1 + " " + mastered + ".txt"):
                account = open(destination_folder + user +
                               " " + pass1 + ".txt", 'a+')
                account.write(new_account + " " + hashed + "\n")
                account.close()

                master_account = open(
                    destination_folder + user + " " + pass1 + " " + mastered + ".txt", 'a+')
                master_account.write(new_account + " " + password + "\n")
                master_account.close()

                print("\nACCOUNT ADDED")

            else:
                print("\nMASTER PASSWORD INCORRECT.")
                login_opt()

            login_opt()

        elif choice == "3":
            option()

        else:
            login_opt()

    if len(os.listdir(destination_folder)) == 0:
        print("\nPLEASE SIGN UP FIRST.")
        option()

    else:
        pass

    user = input("\nEnter your username: ")
    pass1 = input("Enter your password: ")

    if os.path.exists(destination_folder + user + " " + pass1 + ".txt"):
        print("\nACCOUNT LOGIN\n")
        login_opt()

    elif FileExistsError:
        print("Account did not exist. Make sure your username and password is correct.")
        option()


def signup():

    user = input("\nEnter your username: ")
    pass1 = input("Enter your password: ")
    pass2 = input("Re-enter your password: ")
    master = input("Input the master password: ")

    if pass2 != pass1:
        print("\nTHE PASSWORD IS NOT THE SAME.")
        signup()

    elif os.path.exists(destination_folder + user + " " + pass1 + ".txt"):
        print("\nACCOUNT ALREADY EXISTS.")
        option()

    else:
        new_user = open(destination_folder + user +
                        " " + pass1 + '.txt', 'x')
        new_user.close()

        hashed_user = open(destination_folder + user +
                           " " + pass1 + " " + master + '.txt', 'x')
        hashed_user.close()

        print("\nACCOUNT REGISTERED.\n")
        option()


def option():

    if os.path.exists(destination_folder):
        pass
    else:
        os.mkdir(destination_folder)

    choice = input("\nLogin (1) or Signup(2): ")

    if choice == "1":
        login()

    elif choice == "2":
        signup()

    else:
        option()


option()
