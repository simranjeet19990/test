class Person:     #if we are creating a class the name of clain   is firstword is in capytel 
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self): # this is the method we are using 
        print(self.firstname,self.lastname)

x=Person('simranjeet','singh')# here we creat the object.using person class
x.printname()