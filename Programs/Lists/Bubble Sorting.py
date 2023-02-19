L=eval(input("Enter The List\t",))
print("Unsorted List",L)
N=len(L)
for i in range(N):
    for j in range(0,N-i-1):
        if L[j]>L[j+1]:
            temp=L[j]
            L[j]=L[j+1]
            L[j+1]=temp
        print("Convertion Of Unsorted List Into Sorted list", L )
print("Sorted Lisr",L)
 
 
