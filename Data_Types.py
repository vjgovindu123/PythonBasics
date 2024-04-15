#Integer can be defined in 4ways
a=10
a1=0b1010
a2=0o123
a3=0x123
print(a,type(a),end="\n")
print(a1,type(a1),end="\n")
print(a2,type(a2),end="\n")
print(a3,type(a3))
print("Integer Data Type Ended")
#Float
b=10.5
print(b,type(b),end="\n")
print("Float Data Type Ended")
#String
c='v'
print(c,end="\n")
c1="Vijay Govindu"
print(c,type(c),end="\n")
print("String Data Type Ended")
#Boolean
d=True
print(d,type(d),end="\n")
print("Boolean Data Type Ended")

#Complex
e=2+3j
print(e,type(e))

#Bytes:Bytes are immutable in nature and mostly used for binary images ,audio and videos
f=[10,20,30,40]
print(type(f))
f=bytes(f)
print("After Conversion")
for i in range(len(f)):
    print(f[i])
print(type(f))
#f[0]=100 Since Bytes are immutable does not support item assignment

#Bytearray is mutable we can change values
g=[40,30,20,10]
g=bytearray(g)
for i in range(0,4):
    print(g[i],end=",")
print()
g[0]=35
for i in range(0,4):
    print(g[i],end=",")
print()
#Range :Three ways to write the range function
#Syntax:1
for i in range(10):#Prints the indexes from 0-9
    print(i,end=",") #Prints indexes from 0-9
print()
for i in range(0,10):
    print(i,end=",")
print()
for i in range(0,10,2):
    print(i,end=",")
print()

#9.List:List is a homogenious data structure which stores any one particular data type
h=[10,"True",12.5]#Both Homogenious and Heterogenious data types are speciallly allowed in python.
print(type(h))#returns list
print(h)
h[2]="False"
print(h)

#10.Tuple :Tuple is a heterogenious data structure and immutable in nature"
#Ways to Declare Tuple using () and without using {()}
#Syntax-1
i=(20,"Tuple",2.5,"False")
print(i)
print(type(i))
#i[1]="Tuple data Type"
#print("The error is ",i)
#Syntax -2
i1=(3.3,"False","String")
print(type(i1))

# #11:Set is a non-homogenious data structures and mutable in nature and does not
# allow duplicates to store.
j={"Vijay","Spoo","Sai Chamakuri",10,3.2,"False"}
print(j,type(j))


#12:FrozenSet:Frozenset is immutable and remainig all other rules are same as set
k=frozenset(j)
print(j,type(k))

#13;Dictionary:Dict is used to store key value pairs
#Dictionary uses Key-Value Pairs to store values and keys are unique
#Insertion order is not preserved
#It is immutables
l={1:"Vijay",2.0:"SAi",3.9:"Spoorthi"}
print(l)
l[2]="Chamakuri"
print(l)

#14:None
m=None
print(m,type(m))




