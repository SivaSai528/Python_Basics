def amstrong():
    n=int(input("Enter The Number "))
    c,m=0,n
    while (m!=0):
        m=m//10
        c=c+1
    s,a=0,n
    while (a!=0):
        d=a%10
        s=s+d**c
        a=a//10
    if s==n:
        print("This is a Amstrong Number")
    else:
        print("This is Not a Amstrong Number")
amstrong()
    
