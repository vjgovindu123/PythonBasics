#Problem-1:Find the largest remainder after division with 4 and 5

import math
n=int(input("Enter n"))
x=n%4
y=n%5
if x>y:
    print(x)
else:
    print(y)
#Problem-2:Check whether the remainder of number and remainder of square of a number must be same.
m=int(input("Enter M"))
mrem=m%10
squarerem=(m*m)%10
print(mrem,squarerem)
if(mrem==squarerem):
    print("Equal")
#Problem-3:calculate and square sum of sqrt
import math
a=int(input())
b=int(input())
sumofsquares=a*a+b*b
sqrtofsumofsquares=math.sqrt(sumofsquares)
print(sqrtofsumofsquares)
#Problem-4:Given No of days find no of years,no of weeks and no of days
n=int(input("enter no of days"))
years=n/365
print(int(years))
remdays=n%365
weeks=int(remdays/7)
print(weeks)
days=remdays%7
print(days)

