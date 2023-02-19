R=eval(input("Enter The List"))
print(R)
ML=len(R[0])
for i in range(len(R)):
    if len(R[i])>ML:
        ML=len(R[i])
        MLS=R[i]
print("Maximun Length of word in The List is\t",MLS)
    

