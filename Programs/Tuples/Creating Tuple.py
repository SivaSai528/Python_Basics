T=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R=str(input("Enter the Values to the Tuple\t"))
    T=T+(R,)
print(T)
m=len(T[0])
mm=""
for i in range(len(T)):
    if len(T[i])>m:
        mm=T[i]
print(mm)
