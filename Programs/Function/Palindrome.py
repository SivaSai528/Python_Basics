def palindrome():
    S=int(input("Enter The Number\t"))
    m=S
    r=0
    while(m!=0):
        d=m%10
        r=r*10+d
        m=m//10
    if r==S:
        print(S,"This a Palindrome Number")
    else:
        print(S,"This not a Palindrome Number")
palindrome()
