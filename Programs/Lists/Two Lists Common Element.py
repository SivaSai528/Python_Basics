l1=eval(input("Enter the List\t"))
l2=eval(input("Enter the List\t"))
c=0
for i in l1:
    if i in l2:
        c=c+1
        break
if c==1:
    print("true")
else:
    print("false")

    

