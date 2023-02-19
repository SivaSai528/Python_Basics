T=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R=int(input("Enter the Values to the Tuple\t"))
    T=T+(R,)
print(T)
C=0
for i in T:
    C=C+1
print("Length Of the Tuple is ",C)
