#Pattern-1 :Stars Printing in Square Format
print("Pattern-1")
n=int(input("Enter n Value"))
while(n!=0):
    print("*"*n)
    n=n-1

#Pattern-2:Numbers Printing RowWise in Square Format
print("pattern-2")
n=int(input("Enter N value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()

#pattern-3:Numbers Printing RowWise with indexing
print("Pattern-3")
for i in range(1,n+1):
    for j in range(0,i):
        print(i,end="")
    print()

#Pattern-4:Numbers Printing Rowwise to the end side
"""
n=int(input("Enter N"))

for i in range(1,n+1):

    for k in range(n-i+1,n+1):
        print(i,end="")
    for j in range(1, n - i + 1):
        print("", end="")
    for l in range(1,n):
        print("",end="")
    for m in range(5,i,-1):
        print("",end="")
    for k in range(0,i):
        print(i,end="")
    print()
    # for j in range(1,i+1):
    #     print(i,end=" ")
    # print()
    """

#pattern-4:Numbers Printing in Column Wise
print("Pattern-4")
n=int(input(" enter n"))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Pattern-5: Stars Printing in increasing order in right angled triangle.

n=int(input("Enter n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    for j in range(1,n-i+1):
        print("_",end="")
    for j in range(1,n-i+1):
       print("_",end="")
    for j in range(1,i+1):
       print(i,end="")
    print()

