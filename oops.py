# initiate a class
class emp:
    # constructor
    def __init__(self): # need not call manually, automatic execution
        print('Executing attributes')
        self.__name = 'Abhilash'
        self.id='123'
        self.salary='50000'
        self.role='DS'

    def get_name(self):   # getter
        return self.__name
    
    def set_name(self,value):   # setter
        self.__name = value
     
    def loc(self,city):  # function needs to call manually
        print('Calling function')
        print(f"Emp {self.id} lives in {city}")

#creating an object - instance of class 
abhi = emp()
# print(abhi.id) # printing the attributes

#function needs to call manually to print the outputs
abhi.loc('Hyderabad') # printing the function call output by passing parameter

abhi.name = 'Abhilash' #creating attributes outside of class using object
print(abhi.name)

