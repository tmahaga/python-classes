#Mbaga Tuzinde mahaga 
#Admission no:BSCIT-01-0064/2025

name="TM"
age=20
tall=True
a=30
b=10
sum=(a+b)
#files2.0
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\tm.txt","w") #create and open file in write mode
#write to file
print("This is a sample text", file=f)
f.close()
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\tm.txt","a")
print("The sum is",sum,file=f)
f.close()
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\tm.txt","a")
last_name =input("Enter your name:")
score = int(input("Enter marks"))
Budget = float(input("Enter budget:"))
#Displaying on the user screen
print("Last name:",last_name)
print("score:",score)
print("Budget",Budget)
#Displaying in a  file
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\tm.txt","a")
print("last name:",last_name,file=f)
print("score:",score,file=f)
print("Budget",Budget,file=f)
f.close()