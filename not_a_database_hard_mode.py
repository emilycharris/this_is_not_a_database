import csv
import os


def login_prompt():
    print("Please log in.")
    login_username = input("Login Username: ")
    login_password = input("Login Password: ")
    with open("userdata_test.csv") as infile:
        data = csv.DictReader(infile, fieldnames=["username", "password", "full name", "favorite color"])
        for row in data:
            if login_username == row['username']:
                if login_password == row['password']:
                    next_step(login_username)
                else:
                    login_error()
        else:
            login_error()


    return login_username


def user_input():
    username = input("Username: ")
    username_error(username)
    password = input("Password: ")
    full_name = input("Full Name: ")
    favorite_color = input("Favorite Color: ")
    data = "{},{},{},{}\n".format(username, password, full_name, favorite_color)

    with open('userdata_test.csv', 'a') as outfile:
        outfile.write(data)

    print("Record Created")
    next_step()


def login_error():
    print("That is not the correct login information.  Please try again.")
    login_prompt()


def username_error(username):
    with open('userdata_test.csv') as infile:
        userdata = csv.DictReader(infile, fieldnames=["username", "password", "full name", "favorite color"])
        for row in userdata:
            if username == row['username']:
                print('That is not a valid username')
                user_input()

def next_step(login_username):
    next_step = (input("Would you like to (c)reate a user, (e)dit your information, or (l)og out? "))
    if next_step == 'c' or next_step == 'create' or next_step == 'create a user':
        user_input()
    if next_step == 'e' or next_step == 'edit:':
        edit_what = input("Would you like to edit your (p)assword, (n)ame, or (c)olor?")
        if edit_what == 'p' or 'password':
            with open('userdata_test.csv') as infile, open('userdata_test.new.csv', 'w') as outfile:
                data = csv.DictReader(infile, fieldnames=["username", "password", "full name", "favorite color"])
                writer = csv.writer(outfile)
                for row in data:
                    if login_username == row['username']:
                        new_password = input("Enter new password: ")
                        writer.writerow([new_password] + row['username'] + row['full name'] + row['favorite color'])
                        os.rename('userdata_test.csv.new', 'userdata_test.csv')
    if next_step == 'l' or next_step == 'log out':
        print("You have been logged out.")
        login_prompt()
    else:
        exit()

login_prompt()