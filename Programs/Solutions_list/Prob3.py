#Write a program to print sums and multiplies (respectively) all the numbers in a list of numbers.
L=eval(input("Enter a list  "))
s,m=0,1
for i in range(len(L)):
    s=s+L[i]
    m=m*L[i]
print("sum of a list ",s)
print("Multiplication of a list ",m)    
    
