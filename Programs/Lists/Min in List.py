R=[]
size=int(input("Enter the Length of List\t"))
for i in range(size):
    n=int(input("Enter the Value of List\t"))
    R.append(n)
min= R[0]
for x in R:
    if x < min:
        min= x
print (min)
