#Mbaga Tuzinde mahaga   
#Admission no:BSCIT-01-0064/2025
#bonus

f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\if.txt","w")
salary =float(input("Enter your salary:"))
years=int(input("Enter number of years of service:"))
if (years>10):
    bonus=0.1*salary
elif (years>=6 and years<=10):
    bonus=0.08*salary 
else:
    bonus=0.05*salary
   
   
print("your bonus is:",bonus,file=f)
f.close()