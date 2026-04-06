''' this is the username password real world project. '''

username = input("Enter username: ")
password = input("Enter password: ")

if username == "@Surya111" and password == "@surya111":
    print("Login successful!")
else:
    print("Invalid username or password.")



''' using while loop '''

username = " "
while username != "@surya111":
    username = input("Enter username: ")

password = " "
while password != "123456":
    password = input("Enter password: ")

print("Access Granted!")