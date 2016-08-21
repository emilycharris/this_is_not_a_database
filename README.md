# this_is_not_a_database
This is not a database homework

_This assignment was completed as part of my coursework at The Iron Yard._

**Assignment Description:**

Interacting with a database is a key part of building web applications. Let's explore how we can interact with a database without actually writing any SQL or installing a database.

I repeat, this is not a database.

It's important to emphasize that this is not how the underlying structure of a database works. This assignment will help us understand the concept of (long term) storage for multiple requests.

**Objectives**
- Understand how to read from a storage system.
- Integrate your database reader into a user interface type program that asks for user actions.

**Description**

You are to write a database type system where your data is stored in a comma separated format like joel,32,205. Your structure should contain the following items:

- username
- password
- full name
- any number of extra data you want to store on the user

**Normal Mode**

When your program runs it will ask you as the user to login with your username and password (as two inputs). Your program will find the username and password combination and if it finds one it will log the user in, show them the stored information on themselves, and allow them to add a new person to the database. This can be a series of inputs as well. Username? Password? Full Name? etc?

Your application should meet the following criteria:

- Allow a user to login given a correct password
- If a login username is valid but a password is incorrect, do not log the user in and prompt them to try again. DO NOT TELL THEM THE USERNAME WAS RIGHT - this is a security vulnerability.
- If no user by the given username is found, prompt them to login again. (same rules as above)
- When a user is logged in, they are not asked to login anymore - instead their prompt asks if they want to create a user or log out.
- If they choose to log out, return the user to a prompt for them to login with their password.
- If they choose to create a user, begin the line of questioning required to add a line to your database file.

Validation concerns - usernames MUST be unique. If you try to login with a username that exists twice in the DB you should see an error. Do not allow duplicate usernames to be created in the database.

I used Python in order to complete this project.
