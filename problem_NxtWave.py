"""#Problem-1:Find the largest remainder after division with 4 and 5

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
#Leap Year or not
year=int(input("Enter year"))
if(year%4==0 and year%400==0 and year%100!=0):
    print("Year is leap year")
else:
    print("Year is non-leap year")


#Find Day of given Date
day=input("Enter Day")
dat=int(input())
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
index=0
for i in range(len(days)):
    if days[i]==day:
        index=i
        print(index)
daysleft=(dat%7)
print(days[index+daysleft-1])
import math

#prime,perfect number,armstrong
#Prime number is a number divisible by 1 and itself is called prime find n=1-100
n=int(input("Enter number"))
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)
#Perfect number:Sum of divisors/factors of a number is equal to the given number
n=int(input("Enter number"))
for i in range(1,n+1):
    sum=0
    if n%i==0:
        sum+=i
    if sum==n:
        print("Perfect Number")

#armStrong:Sum of powers of the number is equal to the given number
#Say 153=1*1*1+5*5*5+3*3*3=1+125+27=153
n=input('enter number')
lenofn=len(n)
n=int(n)
num=n
sum=0
while(n!=0 and n>0):
    rem=n%10
    sum=sum+math.pow(rem,lenofn)
    print(sum)
    n=int(n/10)
    print(n)

if num==sum:
    print("number is ArmStrong")
else:
    print("number is not an ArmStrong")
#Sum of N terms given X and N
X=int(input("Enter X"))
N=int(input("Enter N"))
sum=0
for i in range(1,2*(N)+1,2):
    sum=sum+math.pow(X,i)
print(sum)
#Pattern Printing Diamond
n=int(input("Enter N"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("_",end="")
    for j in range(1,i+1):
        print(i,end="")
    for j in range(2,i+1):
        print(i, end="")
    for j in range(1, n - i + 1):
        print("_", end="")

    print()
#2-Way Mountain
n=int(input("Enter Number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,n-i+1):
        print("_",end="")
    for j in range(1,n-i+1):
        print("_",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()"""
#One-Sided Inverted Mountain
n=int(input("Enter N"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print(i,end="")
    print()


# for i in range(n-1,0,-1):
#     for j in range(i,0,-1):
#         print(i,end="")
#     print()



