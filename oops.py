# initiate a class
class emp:
    # constructor
    def __init__(self): # need not call manually, automatic execution
        print('Executing attributes')
        self.id='123'
        self.salary='50000'
        self.role='DS'
    
    def loc(self,city):  # function needs to call manually
        print('Calling function')
        print(f"Emp {self.id} lives in {city}")

#creating an object - instance of class 
abhi = emp()
# print(abhi.id) # printing the attributes

#function needs to call manually to print the outputs
abhi.loc('Hyderabad') # printing the function call output by passing parameter,  

