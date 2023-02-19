def isprime():
    S=int(input("Enter The Number\t"))
    print(S)
    c=0
    for i in range(1,S+1):
        if S%i==0:
            i=c+1
    if c==2:
        print(S,"This is a Prime Number")
    else:
        print(S,"This is Not a Prime Number")
isprime()
