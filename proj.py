class chatbot:
    def __init__(self):
        self.username = ''
        self.pwd = ''
        self.loggedin = False
        self.main_menu()


    def main_menu(self):
        user_input = input("""
How would you like to proceed?  
1. Press 1 to SignUp    
2. Press 2 to Sign-IN  
3. Press 3 to write a post 
4. Press 4 to message a friend 
5. Press any other key to exit""")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

obj = chatbot()
