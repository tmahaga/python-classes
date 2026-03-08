#Mbaga Tuzinde mahaga   
#Admission no:BSCIT-01-0064/2025
#dictionary
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\dictionary.txt","w")
person ={
    "name": "Mbaga Tuzinde Mahaga",
    "age":20,
    "Reg_NO":"bscit-01-0064/2025",
    "bank balance":25000000,
    "DoB": "14th February 2006"
    }
student =person.copy()
student = person.get("bank balance")
student =person.items()
print(student,file=f)
print(person,file=f)
f.close()