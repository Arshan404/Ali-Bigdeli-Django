username = input("Enter username : ")
password = input("Enter password : ")

if username == "admin":
    if password == "admin":
        print("succesful login")
    else:
        print("incorrect password")
else:
    print("user not found")        