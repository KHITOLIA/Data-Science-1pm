# l = [1, 2, 3]

# print(type(l))

# s = "Hello"
# print(type(s))


# l.append(4)
# print(l)

# s.append(2)

# print(s)
# methods are written inside any class and are used to perform operations on the objects of that class.
# In Python, strings are immutable, which means that you cannot change them after they are created. 
# Therefore, the `append` method does not exist for strings, and trying to call `s.append(2)` will result in an AttributeError.


# l = []
# print(l)
# l = list([1, 2, 3])
# print(l)

# while calling a class it means you are creating an object of that class. 

# class Person:
#     pass

# obj = Person()
# print(obj)

# a = Person()
# print(a)


# class Atm:
#     name = "YES BANK"
#     location = "Noida" # attributes

#     def greet(self):       # methods
#         print("hello")

# a = Atm()
# print(a.name, a.location, a.greet())



# class Atm:
#     def __init__(self): # constructor : method automatically call at the moment your class is called
#         print(id(self))

#     def greet(self):
#         print("hello")

# a = Atm()
# print(id(a))

class Atm:
    def __init__(self):
        self.pin = ''  # instance variable : object variable having different value for different object
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input('''
hi how can i assist you : 
Press 1 to create pin
Press 2 to change pin
Press 3 to check balance
Press 4 to withdraw money
Press 5 to deposit money
Press 6 to exit
''')       
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw_money()
        elif user_input == "5":
            self.deposit_money()
        else:
            print("Thank you visit again")
    
    def create_pin(self):
        user_pin = input("Enter the pin : ")
        self.pin = user_pin

        user_balance = input("Enter your balance : ")
        self.balance = user_balance
        print("Pin Created successfully")
        self.menu()
    
    def check_balance(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            print("Your balance : ", self.balance)
        else:
            print("Wrong pin")
        self.menu()

obj = Atm()