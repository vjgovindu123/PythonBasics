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