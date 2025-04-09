class chatbot:

    __user_id = 0

    def __init__(self):
        self.id = chatbot.__user_id
        chatbot.__user_id+=1
        self.username = ''
        self.pwd = ''
        self.loggedin = False
        #self.main_menu()
    
    @staticmethod
    def get_id():   # getter
        return chatbot.__user_id
    
    @staticmethod
    def set_id(value):   # setter
        chatbot.__user_id = value
     


    def main_menu(self):
        user_input = input("""
How would you like to proceed?  
1. Press 1 to SignUp    
2. Press 2 to Sign-IN  
3. Press 3 to write a post 
4. Press 4 to message a friend 
5. Press any other key to exit

->""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.mypost()
        elif user_input == "4":
            self.msg()
        else:
            exit()
    
    def signup(self):
        mail = input('Enter your email here')
        pwd = input('Setup your password here')
        self.username = mail
        self.pwd = pwd
        print('Signup successful')
        print('\n')
        self.main_menu()
    
    def signin(self):   
        if self.username=='' and self.pwd=='':
            print('Please signup by selecting 1 on the main menu')
        else:
            user = input('Enter your username:')
            pwd = input(' Enter your Password')
            if self.username == user and self.pwd == pwd:
                print('Sign-in Success')
                self.loggedin = True 
            else:
                print('Invalid Credentials')
        print('\n')
        self.main_menu()
    
    def mypost(self):
        if self.loggedin == True:
            text = input('What you want to post?')
            print(f'Info has been posted {text}')
        else:
            print('Need to sign-in to post') 
        print('\n')
        self.main_menu()
    
    def msg(self):
        if self.loggedin == True:
            text = input('Enter your msg here !!')
            frnd = input('Whom to send the msg?')
            print(f'YOur msg has been send to{frnd}')
        else:
            print('Need to sign-in to post') 
        print('\n')
        self.main_menu()

    

obj = chatbot()
