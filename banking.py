def show_menu():
    print("\nWelcome to Simple Bank!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def banking_system():
    balance = 0  # Start with a balance of 0
    while True:
        show_menu()
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            # Check balance
            print(f"Your current balance is: ${balance}")
        
        elif choice == "2":
            # Deposit money
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"Successfully deposited ${amount}. New balance is: ${balance}")
                else:
                    print("Deposit amount must be greater than zero.")
            except ValueError:
                print("Invalid amount entered. Please enter a number.")
        
        elif choice == "3":
            # Withdraw money
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if 0 < amount <= balance:
                    balance -= amount
                    print(f"Successfully withdrew ${amount}. New balance is: ${balance}")
                elif amount > balance:
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
