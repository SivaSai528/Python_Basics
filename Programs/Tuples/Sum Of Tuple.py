T=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R=int(input("Enter the Values to the Tuple\t"))
    T=T+(R,)
print(T)
G=list(T)
Sum=0
for i in range(len(T)):
    Sum=Sum+G[i]
print(Sum)
