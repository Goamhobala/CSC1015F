# login.py
'''
A simple login system
'''
        
class Registration:
    
    def __init__(self, all_users):
        self.__all_users = all_users
             
    def add_user(self):
        self.__all_users[self.username] = self.password

    def sign_up(self):
        self.username = input("Please enter a username: ")
        validity = False
        while not validity:
            validity = self.__check_username(self.username, self.__all_users)
            
        
        self.password = input("Please enter a password: ")
    
    def __check_username(self, username, all_users):
        if username in all_users:
            self.username = input("Please enter a username: ")
            return False
        return True
        
        
    def get_all_users(self):
        return self.__all_users
        
    
def main():
    all_users = {"madboy1": "69696969"}
    newUser = Registration(all_users)
    newUser.sign_up()
    newUser.add_user()
    print(newUser.get_all_users())

main()
