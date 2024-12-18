import ast  # For reading and parsing accounts file

accounts_file = "accounts.txt"  # File to store account data
user_data = None  # Store the currently logged-in user's data


# Load accounts from the file
def load_accounts():
    try:
        with open(accounts_file, 'r') as file:
            accounts = ast.literal_eval(file.read())  # Safely parse the file
        return accounts
    except (FileNotFoundError, SyntaxError):
        return []  # Return empty list if file doesn't exist or is malformed


# Save accounts to the file
def save_accounts(accounts):
    with open(accounts_file, 'w') as file:
        file.write(str(accounts))  # Write accounts as a string


# Authenticate user by PIN
def authenticate_user(pin):
    accounts = load_accounts()
    for account in accounts:
        if account['pin'] == pin:
            return account
    return None


# Update the account balance and save changes
def update_account_balance(updated_user):
    accounts = load_accounts()
    for account in accounts:
        if account['pin'] == updated_user['pin']:
            account['balance'] = updated_user['balance']  # Update balance
    save_accounts(accounts)  # Save changes back to the file


# Display menu
def show_menu():
    print("\nWelcome to Simple Bank!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


# Banking system
def banking_system():
    global user_data
    print("Welcome to Simple Bank! Please log in to continue.")
    
    while user_data is None:
        try:
            pin = int(input("Enter your PIN: "))
            account = authenticate_user(pin)
            if account:
                user_data = account  # Set the logged-in user data
                print(f"Login successful! Welcome, {user_data['name']}.")
            else:
                print("Invalid PIN. Please try again.")
        except ValueError:
            print("Invalid PIN format. Please enter a numeric PIN.")

    # Main banking operations
    while True:
        show_menu()

        choice = input("Please select an option (1-4): ")

        if choice == "1":
            # Check balance
            print(f"Your current balance is: ${user_data['balance']:.2f}")

        elif choice == "2":
            # Deposit money
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    user_data['balance'] += amount
                    print(f"Successfully deposited ${amount:.2f}. New balance is: ${user_data['balance']:.2f}")
                    update_account_balance(user_data)  # Save updated balance
                else:
                    print("Deposit amount must be greater than zero.")
            except ValueError:
                print("Invalid amount entered. Please enter a number.")

        elif choice == "3":
            # Withdraw money
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if 0 < amount <= user_data['balance']:
                    user_data['balance'] -= amount
                    print(f"Successfully withdrew ${amount:.2f}. New balance is: ${user_data['balance']:.2f}")
                    update_account_balance(user_data)  # Save updated balance
                elif amount > user_data['balance']:
                    print("Insufficient funds!")
                else:
                    print("Withdrawal amount must be greater than zero.")
            except ValueError:
                print("Invalid amount entered. Please enter a number.")

        elif choice == "4":
            # Exit the program
            print("Thank you for using Simple Bank. Goodbye!")
            break

        else:
            print("Invalid option. Please select from the menu (1-4).")


# Start the banking system
banking_system()
