import math


def myfuction(item):
    for x in item:
        print(x)
cars=["toyota","honda","nissan"]
myfuction(cars)

def myfunction(x,y):
    radius=x
    hieght=y
    math.pi=3.142
    volume=math.pi*radius*radius*hieght
    print(f"The volume of the cylinder is {volume}")
    return volume
print(myfunction(40,20))
    

    