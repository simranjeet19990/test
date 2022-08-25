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
                print(f'try again {Attemt} attemt left') #here we modefied
                Attemt-=1
                continue

        print('know game is over')

x=Lottery()
x.my()



