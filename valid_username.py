user_name = input("Enter username: ")

if " " in user_name:
    print("No spaces allowed")
elif not user_name.isalpha():
    print("Username can't contain numbers or symbols")
elif len(user_name) > 12:
    print("Username should not be more than 12 characters")
else:
    print(f"Welcome {user_name}")