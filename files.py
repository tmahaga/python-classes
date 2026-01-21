

from os import name

#Mbaga Tuzinde mahaga 
#Admission no:BSCIT-01-0064/2025
print("Hello world")
#pthon files:create/open, write, close
f = open("C:\\Users\\Admin\\Desktop\\pyhton class\\sample.txt","w") #create and open file in write mode
print("This is sample text", file=f)
#write to file
a=20
b=40.3
sum=(a+b)
print("a=20",file=f)
print("b=40.3",file=f)
print("name ='Tuzinde'",file=f)
print("tall = True",file=f)
print("sum = (a+b)",file=f)
print("sum",sum, file=f) #60.3
print("The sum is", sum, file=f)        
print("Name is" + name + "and sum is", str(sum),file=f)
f.close()