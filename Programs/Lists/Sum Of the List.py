R=[]
size=int(input("Enter the Length of List\t"))
for i in range(size):
    n=int(input("Enter the Value of List\t"))
    R.append(n)
Sum=0
for i in range(len(R)):
    Sum=Sum+R[i]
print(Sum)
