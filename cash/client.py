class Client:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def getName(self):
        return self.__name
    
    def setName(self, name):
        if isinstance(name, str) and name.strip():  # Ensure 'name' is a valid string
            self.__name = name
        else:
            raise ValueError("Name must be a non-empty string.")
    
      # Getter for 'balance'
    def get_balance(self):
        return self.__balance

    # Setter for 'balance'
    def __set_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:  # Ensure 'balance' is non-negative
            self.__balance = balance
        else:
            raise ValueError("Balance must be a non-negative number.")
        
    def deposit(self, amount):
        new_amount = self.__balance + amount #add the new amount to existing balance
        self.__set_balance(new_amount)

        

    def withdraw(self, amount):
       new_amount = self.__balance - amount #resuce the amount from existing balance
       self.__set_balance(new_amount)