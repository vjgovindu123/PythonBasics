#Positional Arguments
def disp(a,b,c,d):
    print(a,b,c,d)
disp(10,20,30,40)

#Keyword Arguments in functions
def disp(a,b,c,d):
    print(a,b,c,d)
disp(a=10,c=30,d=20,b=40)

#Positional parameters followed by keyword in functions
def disp(a,b,c,d):
    print(a,b,c,d)
disp(10,30,d=400,c=300)#Position followed by keyword

#Default Parameters
def disp(a=40,b=30,c=20,d=10):
    print(a,b,c,d)
disp(10,20)

def areaofTriangle(l=10,b=10):
    print(0.5*l*b)
areaofTriangle(b=20)

#Accepting any number of Parameters
def Students(*id):
    for i in range(len(id)):
        print(id[i],end="*")
Students([1,2,3,4])

#passing list as a argument
def studentDetails(students):
    for i in range(len(students)):
        print(students[i])


students=["Vijay","Alekya","Henif","Spoorthi","Sandhya"]
studentDetails(students)

x=lambda:print("Lambda Functions")
x()
y=lambda a,b:print("Lambda Function with parameters ")
y(10,20)
#Printing the paramter values
z=lambda c,d:(c*d)
print(z(10,20))