R=[]
size=int(input("Enter the Length of List\t"))
for i in range(size):
    n=int(input("Enter the Value of List\t"))
    R.append(n)
Multiple=1
for i in range(len(R)):
    Multiple=Multiple*R[i]
print(Multiple)
