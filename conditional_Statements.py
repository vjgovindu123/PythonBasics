#IF Block
n=int(input("Enter n Value"))
for i in range(n+1):
    if i%2==0:
        print(i)
print(" End IF")
#IF ELSE Block
#WAP to check you are eligible to vote or not
age=int(input("Enter age Value"))
if age>=18:
    print("Your are eligible to Vote")
else:
    print("You are not eligible to Vote")
print("Validated Age")
#ELIF Block
#WAP to Display WeekDays
i=int(input("Enter a number in a Week"))
#for i in range(n+1):
if i==1:
    print("Monday")

elif i==2:
    print("Tuesday")
elif i==3:
    print("Wednesday")
elif i==4:
        print("Thursday")
elif i==5:
        print("Friday")
elif i==6:
        print("Saturday")
else:
        print("Sunday")

#And OR NOT
#WAP to print even number
a=int(input("Enter a"))
b=int(input("Enter b"))
if a%2==0 and b%2==0:
    print("Even Numbers")
#WAP to print a number is positive or not
c=int(input("Enter number to check number is positive or negative"))
if c==0 or c>0:
    print(" Positive Integer")
else:
    print("Negative Integer")

#WAP to find greatest of two numbers
print("Greatest of Two Numbers")
d=int(input("Enter d"))
e=int(input("Enter e"))
if not d > e:
    print(" E is Greater")
else:
    print(" D is Greater")

