#Write a program to print the average of the elements in the list
L=eval(input("Enter a list  "))
s=0
n=len(L)
for i in L:
   s=s+i
print("average of a list ",s/n)
