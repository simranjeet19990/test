"""
# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

"""

class Check():
    def __init__(self,number):
        self.num= number
    # make a function num is prime or not
    def prime(self):
        number = self.num

        if number>1:
            for i in range(2,number):
                if (number%i) == 0:
                    return "num is not a prime number"# agar hum return ma print()use karta hato none aya ga 

        return "num is prime number"
        

x=Check(8)
print(x.prime())                   
            
            



    
        




