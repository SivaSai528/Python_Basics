T=()
Size=int(input("Enter the Length of Tuple\t"))
for i in range(Size):
    R=int(input("Enter the Values to the Tuple\t"))
    T=T+(R,)
print(T)
M=T[0]
for i in range(1,len(T)):
    if M>T[i]:
        M=T[i]
print("Minimun Value In The Tuple",M)
