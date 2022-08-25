#Here is tempary idea for random numbergame 
"""import random
print("Enter any number between 0 to 20")    
choss=input()
gauss=random.randint(0,20)

if gauss==choss:
    print("you are pass")

elif gauss!=choss:
        print("you are fail try again")
""" 
#here we useing loop for repting the program
"""
  
import random
gauss=random.randint(0,20)
print('Number',gauss)

attemt=5
while attemt>0:
    choss=int(input('Enter any number b/w 0 to20:'))
    if gauss==choss:
        print('you win')
    
        break
    elif gauss!=choss:
        print(f'try again {attemt} attemt left')
        attemt-=1
        #print('you lost')
        continue
print('know game is over')   """
# NAME OF THE GAME IS (LOTTERY MACHINE)
import random
class Lottery():
    # def __init__(self,number):
    #     self.number=number
       
    #gauss=random.randint(0,20)
    #choss=int(input('Enter any number b/w 0 to20:'))
    #attemt=5

    def my(self):
        Gauss=random.randint(0,20)
        
        Attemt=5
        while Attemt>0:
            number=int(input('Enter any number b/w 0 to20:'))
            if Gauss==number:
                print("you win")
                break
        
            elif Gauss!=number:
                Attemt-=1
                print(f'try again {Attemt} attemt left')
                continue
            
        print('know game is over')

x=Lottery()
x.my()



    


    