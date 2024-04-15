#Area of Triangle
a,b=5,5
# a=int(input("enter value of A "))
# b=int(input("Enter Value of B"))
print(1/2*a*b)
a,b,c,d=10,20,30,40
print(a,b,sep="->",end=",")
print(c,d,sep=",",end="->")
#or
e=10,20,30,40
print("End Attribute",e,end="\n")#End Attribute is used to define the end iterable value reached
print(a,e,sep="*")#Sep attribute which is used to separate the custom values.
print()
#Format Specifier
f=90
g=12.5
h="SAI Vijay"

print("%i"%(f))
print("%f"%(g))
print("%s"%(h))

#Replacement Operator
id=2
Applicant="SAi"
Height=5.6
print("Name={},RollNo={},Height={}".format(Applicant,id,Height))
print("ID={x},Name={y},Height={z}".format(x=id,y=Applicant,z=Height))
print("Id={0},NameofApplicant={1},Height={2}".format(id,Applicant,Height))
print("Applicant's Name={1},ID={0},Height={2}".format(id,Applicant,Height))

#eval() function
print(eval("5+6"))
print(eval("5*5"))

#Write a Program to Evaluate Calculator program

while True:
    expression = eval(input("Enter Expression"))
    if expression=="exit":
        break
    try:
      #  res=eval(expression)
        print(eval(expression))
    except:
        print("Invalid Expression")
