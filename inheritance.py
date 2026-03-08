class calculation1:
    def addition(self,a,b):
        return a+b;

class calculation2:
    def addition(self,a,b):
        return a+b;
class calculation3(calculation1,calculation2):
    def multiplication(self,a,b,c,d):
        return a*b*c*d;
    
    
c=calculation3()
print(c.addition(2,3))
print(c.addition(2,50))    
print(c.multiplication(2,3,4,5))
