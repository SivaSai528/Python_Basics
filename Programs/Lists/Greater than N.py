R=[]
size=int(input("Enter the Length of List\t"))
for i in range(size):
    n=int(input("Enter the Value of List\t"))
    R.append(n)
print(R)
for x in R:
    if x>10:
        print(x,"These  are Greater Than 10")
