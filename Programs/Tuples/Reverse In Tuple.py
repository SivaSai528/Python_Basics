T=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R=int(input("Enter the Values to the Tuple\t"))
    T=T+(R,)
print(T)
def S(T):
    for i in reversed(range(len(T))):
        yield T[i]
for j in S(T):
    print(j)
        
