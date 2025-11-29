def create_account(accounts):
    username = input("Enter a username: ")
    if username in accounts:
        print("Account already exists!")
    else:
        accounts[username] = 0   # start with balance = 0
        print(f"Account '{username}' created successfully!")
    return accounts

def login(accounts):
    username = input("Enter username: ")
    if username in accounts:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Account not found. Please create one first.")
        return None

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} deposited.")
    else:
        print("Deposit must be greater than 0.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
    elif amount <= 0:
        print("Withdrawal must be greater than 0.")
    else:
        balance -= amount
        print(f"${amount:.2f} withdrawn.")
    return balance

def main():
    accounts = {}
    current_user = None
    is_running = True

    while is_running:
        print("\n=== Banking Program ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Show Balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Logout")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            accounts = create_account(accounts)

        elif choice == '2':
            current_user = login(accounts)

        elif choice == '3':
            if current_user:
                show_balance(accounts[current_user])
            else:
                print("You must log in first.")

        elif choice == '4':
            if current_user:
                accounts[current_user] = deposit(accounts[current_user])
            else:
                print("You must log in first.")

        elif choice == '5':
            if current_user:
                accounts[current_user] = withdraw(accounts[current_user])
            else:
                print("You must log in first.")

        elif choice == '6':
            if current_user:
                print(f"User {current_user} logged out.")
                current_user = None
            else:
                print("No user is logged in.")

        elif choice == '7':
            is_running = False

        else:
            print("Invalid choice. Try again.")

    print("Thank you, have a nice day!")

main()