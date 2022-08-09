user = []
adminPassword = []

user = input("UserName: ")
adminPassword = input("Password: ")


name = input("Name:")
password = input("Username:")

if name == user:
    print("valid Username!")
else:
    print("invalid")

if password == adminPassword:
    print("Valid Password!")
else:
    print("invalid")