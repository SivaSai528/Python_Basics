#Write a program to find the Maximum element in the list (don’t use max())
L=eval(input("Enter a list  "))
mx=L[0]
for i in range(1,len(L)):
    if L[i]>mx:
        mx=L[i]
print("Maximum number in a list ",mx)

    
