def strong():
    s=int(input("Enter the Number  "))
    a=1
    n=0
    while (s!=0):
        q=s%10
        for i in range(1,q+1):
            a=a*i
        n=n+a
        s=s//10
    print(n)
strong()
