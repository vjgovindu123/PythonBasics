print("Hello!")
str="Welcome to Python Learning Zone.\n"
str1="Lets Start With Variable Declarations"
print(str+str1)
a=10
print(a)
b=1.3
print(b)
c=0b1010
print(bin(c))
c=int(c)
print(c)
d=0o1234
print(oct(d))
print(type(d))
e=0x1234
print(hex(e))
print(type(e))
#Boolean Declaration
f=True
g=False
print(f+g,f*g,g/f,f-g)
print(type(f))
print(f>g)
# String Operations
str2="Spoorthi"
str3="Vijay"
print(str2[0:8])
print(str3+" "+str2)
print(str3*1,str2*4,str3*3)
print(id(str2),id(str3))

#Indexing
print(str2[0],str3[0])
for i in range(0, len(str)):
    print(str[i])
#Slicing
print("Slicing")
print(str2[0:8:2])
print(str2[1:8:2])
print(str2[::-1])
print(str2[0:len(str2):2])
print(len(str2))
for i in range(len(str2)):
    print(str2[i],end=",")

