#Write a program to print all the elements in reverse order with out using reverse function and slicing
L=eval(input("Enter a list  "))
m=[]
for i in range(len(L)-1,-1,-1):
    m.append(L[i])
print("Revesre list ",m)
    
    
