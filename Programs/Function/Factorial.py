def factorial():
    s=int(input("Enter The Number  "))
    fact=1
    if s==1:
        fact=1
    else:
        for i in range(1,s+1):
            fact=fact*i
        print(fact)
factorial()
        

       
