from proj import chatbot
#from oops import emp

#user1 = chatbot()

#user1.signin() # method
user1 = chatbot()
print(user1.id)

chatbot.set_id(10) # accessing the static method directly
user2 = chatbot()
print(user2.id)

user3 = chatbot()
print(user3.id)

#print(user1._emp__name) # encapsulation - hiding variables 

#print(user1.get_name())  
#user1.set_name('Avi')
#print(user1.get_name())


# Calling the class method from another file and accessing.
#This kind of strcture is called modular coding


# function

# l1 = [1,2,3]
# len(l1) # function