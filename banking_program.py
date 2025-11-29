def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def create_account(accounts):
    username = input("Enter a username for your account: ")
    if username in accounts:
        print("Account already exists!")
        return accounts
    else:
        accounts[username] = 0
        print(f"Account '{username}' created successfully with balance $0.00")
    return accounts

def main():
    accounts = {}   # ✅ initialize accounts dictionary
    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("0. Create Account")   # ✅ give create account its own option
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == '0':
            accounts = create_account(accounts)
        elif choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print(f"That is not a valid choice: {choice}")

    print("Thank you, have a nice day!")

main()