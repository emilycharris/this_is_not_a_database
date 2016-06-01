import csv


def login_prompt():
    print("Please log in.")
    login_username = input("Login Username: ")
    login_password = input("Login Password: ")
    with open("userdata.csv") as infile:
        data = csv.DictReader(infile, fieldnames=["username", "password", "full name", "favorite color"])
        for row in data:
            if login_username == row['username']:
                if login_password == row['password']:
                    next_step()
                else:
                    login_error()
            else:
                login_error()

def user_input():
    username = input("Username: ")
    username_error(username)
    password = input("Password: ")
    full_name = input("Full Name: ")
    favorite_color = input("Favorite Color: ")
    data = "{},{},{},{}\n".format(username, password, full_name, favorite_color)

    with open('userdata.csv', 'a') as outfile:
        outfile.write(data)

    print("Record Created")
    next_step()


def login_error():
    print("That is not the correct login information.  Please try again.")
    login_prompt()


def username_error(username):
    with open('userdata.csv') as infile:
        userdata = csv.DictReader(infile, fieldnames=["username", "password", "full name", "favorite color"])
        for row in userdata:
            if username == row['username']:
                print('That is not a valid username')
                user_input()

def next_step():
    next_step = (input("Would you like to (c)reate a user or (l)og out? "))
    if next_step == 'c' or next_step == 'create' or next_step == 'create a user':
        user_input()
    if next_step == 'l' or next_step == 'log out':
        print("You have been logged out.")
        login_prompt()
    else:
        exit()

login_prompt()