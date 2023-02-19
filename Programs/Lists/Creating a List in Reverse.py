R=[]
size=int(input("Enter the Length of List\t"))
for i in range(size):
    n=int(input("Enter the Value of List\t"))
    R.append(n)
M=R
for i in range(len(R)-1,-1,-1):
    print(i,"index value is",R[i])
    print(M)
