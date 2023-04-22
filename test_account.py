from pytest import *
from account import *

class Test:
    
    def setup_method(self):
        self.t1 = Account("Me")
        
    def teardown_method(self):
        del self.t1
    
    
    def test_init(self):
        assert self.t1.get_name() == "Me"
    
    def test_deposit(self):
        assert self.t1.deposit(-5.50) is False
        assert self.t1.get_balance() == 0
        
        assert self.t1.deposit(0) is False
        assert self.t1.get_balance() == 0
        
        assert self.t1.deposit(5.75) is True
        assert self.t1.get_balance() == 5.75
        
        
    def test_withdraw(self):
        
        self.t1.deposit(5.75)
        
        assert self.t1.withdraw(-5.50) is False
        assert self.t1.get_balance() == 5.75
        
        assert self.t1.withdraw(0) is False
        assert self.t1.get_balance() == 5.75
        
        assert self.t1.withdraw(100) is False
        assert self.t1.get_balance() == 5.75
        
        assert self.t1.withdraw(2.25) is True
        assert self.t1.get_balance() == 3.50
        







