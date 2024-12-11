from client import Client
# ANSI escape codes
RESET = "\033[0m"    # Reset to default color
RED = "\033[31m"     # Red text
GREEN = "\033[32m"   # Green text
YELLOW = "\033[33m"  # Yellow text
BLUE = "\033[34m"    # Blue text
user = None

def setup_account():
    global user
    try:
        name = input("Please Enter your Name:")
        if name == "":
            raise ValueError("Name cannot be empty")
        balance = float(input("Please Enter your initial deposit:"))       
        
        if balance < 0:
            raise ValueError

        ##set the client
        user = Client(name, balance)
        print(f"\n{GREEN}You have successfully created an account, {user.getName()}.{RESET}")
    except ValueError:
        print(f"\n{RED}Error Creating Account: Initial Balance must be a non-negative number.{RESET}")
        # print(f"Error: {e}")


def user_exists():
    if user == None:
        print(f"\n{BLUE}No account has been setup yet.{RESET}")
        return False
    else:
        return True


def check_balance_withdraw(amount) -> bool:
    ##check the amount against the current balance
    current_balance = user.get_balance()
    if current_balance >= amount: 
        return True
    else:
        print(f"\n{RED}Requested Amount is greater than you current Balance.{RESET}")
        return False
    

def show_start_menu():
    print("\nWelcome to the Cash App.")
    print("1 - Setup Account")
    print("2 - Check Balance")
    print("3 - Deposit")
    print("4 - Withdraw")
    print("5 - Exit")


def cash_app():
    while True:
        show_start_menu()

        try:
            choice = int(input("Select an option (1-5): "))
            if choice == 1:
                if not(user_exists()):
                    setup_account()
                else:
                    overwrite = input(f"\n{YELLOW}Another account is currently active, do you want to overwrite it? Y/N: {RESET}")
                    if overwrite == "Y" or overwrite == "y":
                        setup_account()
            elif choice == 2:
                if user_exists():
                    print(f"\n{GREEN}Your Current Balance is {user.get_balance()}{RESET}")
            elif choice == 3:
                #deposit
                if user_exists():
                    try:
                        amount = float(input(f"{YELLOW}Enter amount to deposit: {RESET}"))
                        if amount >=0:
                            user.deposit(amount)
                            print(f"\n{GREEN} You have successfully deposited {amount} to your Account {RESET}")
                            print(f"{GREEN} Your new Balance is {user.get_balance()} {RESET}")
                        else:
                            #given number is negative
                            print(f"\n{RED}Error - Amount must be a non-negative number. {RESET}")
                    except ValueError:
                        print(f"\n{RED}Error - Amount must be a non-negative number. {RESET}")
                    
            elif choice == 4:
                #withdraw
                if user_exists():
                    try:
                        amount = float(input(f"{YELLOW}Enter amount to withdraw: {RESET}"))
                        if check_balance_withdraw(amount):
                            if amount >= 0:
                                user.withdraw(amount)
                                print(f"\n{GREEN} You have successfully withdrawn {amount} from your Account {RESET}")
                                print(f"{GREEN} Your new Balance is {user.get_balance()} {RESET}")
                            else:
                                print(f"\n{RED}Error - Amount must be a non-negative number. {RESET}")
                    except ValueError:
                        print(f"\n{RED}Error - Amount must be a non-negative number. {RESET}")
                        
            else:
                #exit the app
                print("\nExiting the Cash App now")
                break
        except TypeError:
            print("\n Not a Valid Option (Select from 1-5 only)")
        except ValueError:
            print("\n Not a Valid Option (Select from 1-5 only)")
    

cash_app()