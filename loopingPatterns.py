#Pattern-1 :Stars Printing
n=int(input("Enter n Value"))
while(n!=0):
    print("*"*5)
    n=n-1
print("Outside While")
#Pattern-2:Numbers Printing RowWise
print("pattern2")
n=int(input("Enter N value"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()
#pattern-3:Numbers Printing RowWise with indexing
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

#pattern-5:
n=int(input(" enter n"))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()