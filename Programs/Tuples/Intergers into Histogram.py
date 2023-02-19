T1=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R1=int(input("Enter the Values to the Tuple\t"))
    T1=T1+(R1,)
print(T1)
for i in T1:
    for j in range(i):
        print("$",end="")
    print("\n")
