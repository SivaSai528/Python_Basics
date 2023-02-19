def perfect():
    S=int(input("Enter The Number\t"))
    c=0
    for i in range(1,S):
        if S%i==0:
            c=c+i
    if S==c:
        print("This is a Perfect Number")
    else:
        print("Not a Perfect Number")
perfect()
