'''
A banking system where registered user can deposite, withdraw and check 
thier account balance..
'''
# This is the assumed data base where user fullname and password is stored
account_info = {
    'user1':['DAMIAN MALEY', 1234], 
    'user2':['JUDITH AJALA', 5678]
    }

print('*' *50)
print('='*10,'WELCOME TO ZENITH BANK...','='*10)

# Allow user to enter password and if password is not in our db after the user tries 3 times,
# the program terminates....

for tries in reversed(range(0,3)):
    password = int(input('\nenter your digit pin \n'))
    if password == account_info['user1'][1]:
        print('\nwelcome {}\n'.format(account_info['user1'][0]))
        break
    elif password == account_info['user2'][1]:
        print('\nwelcome {}\n'.format(account_info['user2'][0]))
        break
    else:
        print(f'\nWrong password... Your card will be swallowed after {tries} attempt\n')
else:
    raise SystemExit('\nYour Card has been swallowed.. Meet the customer care for complaint\n')

# Bank management system using oop.

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def fullname(self):
        return f'{self.name}'

    def deposite(self, amount):
        self.balance+=amount
    
    def Witdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Sorry... Insufficient fund')

    def check_balance(self):
        print(f'\n{self.fullname()}, Your balance are: {self.balance}\n')

# Creating a common interface for multiple form.
def main(p):

    # creating an instance of a BankAccount class. 
    customer1 = BankAccount(p)
    done = False
    while done == False:
        print("""=====MAIN MENU=====
            1. Deposite
            2. Withdrawal
            3. Check Balance
            4. Exit
        
        """)
        choice = int(input('\nEnter Choice: \n'))
        if choice == 1:
            customer1.deposite(int(input('\nhow much do you want to deposite?: \n')))
        elif choice == 2:
            customer1.Witdrawal(int(input('\nhow much do you want to withdraw?: \n')))
        elif choice == 3:
            customer1.check_balance()
        elif choice == 4:
            raise SystemExit(f'\n {customer1.fullname()}, THANK YOU FOR BANKING WITH US\n')
if password == account_info['user1'][1]:
    main(account_info['user1'][0])
elif password == account_info['user2'][1]:
    main(account_info['user2'][0])

