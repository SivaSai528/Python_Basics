R=eval(input("Enter The List"))
print(R)
M=R[0]
for i in range(1,len(R)):# we take 1 it is index that's means compare the first element with 1 index
    if M<R[i]:
        M=R[i]
print("Maximun Value in The List\t",M)
    
