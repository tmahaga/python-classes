#Mbaga Tuzinde mahaga   
#Admission no:BSCIT-01-0064/2025
#grade
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\grade.txt","w")
subject1 =int(input("Enter marks for subject1:"))
subject2 =int(input("Enter marks for subject2:"))
subject3 =int(input("Enter marks for subject3:"))
avarage =(subject1 + subject2 + subject3)/3
if (avarage >= 70 and avarage <= 100):
    grade = "A"
elif(avarage >=60 and avarage <70):
    grade = "B"
elif(avarage >=50 and avarage <60):
    grade = "C"
elif(avarage >=40 and avarage <50):
    grade = "D" 
else:
    grade = "F"
print("your grade is:",grade,file=f)
f.close()