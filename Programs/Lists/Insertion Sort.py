arr = [16,19,11,15,10]
for i in range(1,len(arr)):
    key=arr[i]
    #print(key)
    j=i-1
    #print(key,"<",arr[j])
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j=j-1
        #print(arr)
    arr[j+1] = key
print ("sorted list is :",arr) 
