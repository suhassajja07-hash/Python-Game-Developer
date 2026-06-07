users = {"alice":"pass123", "bob":"hello456", "charlie":"abc789", "david":"mypassword", "emma":"secure321"}

username = input("Enter username: ")
password = input("Enter password: ")

if username not in users:
    print("You are not a valid user of the system.")
elif users[username] != password:
    print("Invalid password.")
else:
    print("You are now logged in to the system.")