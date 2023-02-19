def factors():
    S=int(input("Enter The Number\t"))
    c=0
    for i in range(1,S+1):
        if S%i==0:
            print(i)
factors()
