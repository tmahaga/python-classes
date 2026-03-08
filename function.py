#python functions
def myName():
    print("my name is python")
    print("what is your name")
    print("what country are you from?")
    
#function call
myName() 

def add(a,b):
    sum=a+b
    return sum
print(add(10,20))


def myname(name,age):
    print("my name is "+name+"and i am"+str(age)+"years old")
    print(f"My name is {name}and i am{age}years old")
myname("tuzinde",19)  
  
    
    
def username(firstname,age):
    print(f"My name is{firstname}and my age is{age}")
    
firstname=input("Enter your name:")
years=int(input("Enter your age:"))
username(firstname,years)

def simpleintrest(payee,rate,time):
  intrest=(payee*rate/100*time)   
  print(f"The simple intrest is {intrest}")
payee= float(input("Enter the payee amount:"))
rate=int(input("Enter the rate:"))
time=int(input("Enter the time:"))
simpleintrest(payee,rate,time)

def myfuction(item):
    for key,value in item.items():
        print(key,value)
cars=["toyota","honda","nissan"]
student ={
    "name":"tuzinde",
    "age":20,
    "country":"uganda"
}
myfuction(student)