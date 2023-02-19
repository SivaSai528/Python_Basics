T=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R=int(input("Enter the Values to the Tuple\t"))
    T=T+(R,)
print(T)
for x in T:
    if x%2==0:
        print(x,"this is a Even Number in the Tuple")
for i in T:
    if i%2==0:
        print(i)


