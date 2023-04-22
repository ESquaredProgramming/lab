class Account:
    
    def __init__(self, name: str) -> None:
        """
        Initialization function for the object.
        
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0
    
    
    def deposit(self, amount: float) -> bool:
        """
        Function to add (deposit) an amount to the account's balance.
        
        :param amount: Amount being deposited.
        :return: True if deposit was successful, False if invalid amount.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        return False
    
    
    def withdraw(self, amount: float) -> bool:
        """
        Function to subtract (withdraw) an amount to the account's balance.
        
        :param amount: Amount being withdrawn.
        :return: True if withdraw was successful, False if invalid amount.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    
    
    def get_balance(self) -> float:
        """
        Function to access the account balance.
        
        :return: Account balance.
        """
        return self.__account_balance
    
    
    def get_name(self) -> str:
        """
        Function to access the account name.
        
        :return: Account name.
        """
        return self.__account_name