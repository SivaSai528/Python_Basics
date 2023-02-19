T=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R=int(input("Enter the Values to the Tuple\t"))
    T=T+(R,)
print(T)
K=T[0]
for i in range(1,len(T)):
    if K<T[i]:
        K=T[i]
print("Maximum Value in the Tuple\t",K)
