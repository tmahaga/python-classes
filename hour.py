#hours
#file
f=open ("C:\\Users\\Admin\\Desktop\\pyhton class\\hour.txt","a")
hours_worked =int(input("Enter Hours:"))
rate_per_hour = float(input("Enter Rate:"))
Gross_pay =(hours_worked * rate_per_hour)
f.close()
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\hour.txt","a")
print("hours",hours_worked)
print("Rate",rate_per_hour)
print("Gross pay",Gross_pay)
f.close
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\hour.txt","a")
print("hours:",hours_worked,file=f)
print("Rate:",rate_per_hour,file=f)
print("Gross pay",Gross_pay,file=f)
f.close()