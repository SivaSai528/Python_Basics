T2=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R2=int(input("Enter the Values to the Tuple\t"))
    T2=T2+(R2,)
print(T2)
T1=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R1=int(input("Enter the Values to the Tuple\t"))
    T1=T1+(R1,)
print(T1)
c=0
for i in T1:
    if i in T2:
        c=c+1
        break
if c==1:
    print("true")
else:
    print("false")
