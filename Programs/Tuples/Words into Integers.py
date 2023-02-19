T1=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R1=str(input("Enter the Values to the Tuple\t"))
    T1=T1+(R1,)
print(T1)
M=[]
for i in T1:
    M.append(len(i))
print(M)
