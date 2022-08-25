"""
f= open("/home/simranjeet/test/opaly/demo1.txt","r")
for x in f:
    print(x)
    # if you are give the name of the file then you have togive complet path
    f.close()#afther work is done close the file
    """

   # now we are using 'w','r','a' .
"""
f = open("/home/simranjeet/test/opaly/demo1.txt","a")
f.write("now the has more contant!")
f.close()
f= open("/home/simranjeet/test/opaly/demo1.txt","r")
print(f.read())
# 'a' append is use for add anew line an contant
"""
# here we are write inthe file.
"""
f=open("/home/simranjeet/test/opaly/demo2.txt","w")
#x=input()
#f.write(x)
f.write("hi simranjeet")# There is methode ot write 1 is by using (input) & by using (write)
f.close()
f=open("/home/simranjeet/test/opaly/demo2.txt",'r')
print(f.read())
f.close()

"""
#here we are creating a file name myfile.
#x=open("myfile.txt","x")
x=open('dok.txt','w')# here we using two differen method ot creart a new file by using of 'w','x' .
x.write('hello ji kihal chal kida\nmy name is amandeep singh\nmy age is 23 years old ') 
x.close()
x=open("/home/simranjeet/test/dok.txt","r")
print(x.read())
x.close()
