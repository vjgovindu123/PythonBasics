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
f[0]=100
#Bytearray is mutable we can change values
g=[40,30,20,10]
g=bytearray(g)
print(g)