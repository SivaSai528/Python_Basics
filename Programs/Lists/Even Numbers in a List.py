R=[]
size=int(input("Enter the Length of List\t"))
for i in range(size):
    n=int(input("Enter the Value of List\t"))
    R.append(n)
print(R)
for x in R:
    if x%2==0:
        print(x,"this is a even number")
    else:
        print(x,"this is a non-even number")
