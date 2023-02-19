def leapyear():
    S=int(input("Enter The Year\t"))
    if (S%4==0 and S%100!=0):
        print("This is a Leap Year")
    else:
        print("This is not a leap year")
leapyear()
