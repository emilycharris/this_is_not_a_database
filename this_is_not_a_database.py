import csv

def login_prompt():
    print("Welcome.  Please log in.")
    with open("userdata.csv") as infile:
        userdata = csv.DictReader(infile, fieldnames=["username", "password", "full name", "favorite color"])
        login_username = input("Your Username: ")
        login_password = input("Your Password: ")
        for row in userdata:
            if login_username == row['username'] and login_password == row['password']:
                next_step = (input("Would you like to (c)reate a user or (l)og out? "))
                if next_step == 'c' or next_step == 'create' or next_step == 'create a user':
                    user_input()
                    break
                else:
                    break
            else:
                print("That is not the correct login information.  Please try again.")
                login_prompt()

def user_input():
    username = input("Username: ")
    error_checking(username)
    password = input("Password: ")
    full_name = input("Full Name: ")
    favorite_color = input("Favorite Color: ")
    data = "{},{},{},{}\n".format(username, password, full_name, favorite_color)

    with open('userdata.csv', 'a') as outfile:
        outfile.write(data)

    print("Record Created")
    return username
    

def error_checking(username):
    with open('userdata.csv') as infile:
        userdata = csv.DictReader(infile, fieldnames=["username", "password", "full name", "favorite color"])
        for row in userdata:
            if username in row['username']:
                print('That is not a valid username')
                user_input()


login_prompt()