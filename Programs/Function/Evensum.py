def evensum():
    S=int(input("Enter The Number\t"))
    M=0
    for i in range (1,S+1):
        if i%2==0:
            M=M+i
    print("Sum of the Even numbers Preceeding the Given Number",M)
evensum()
            
