#Write a program to create a list and display the list
L=[]
size=int(input("Enter the lenght for list  "))
for i in range(size):
    n=int(input("Enter a value to list  "))
    L.append(n)
print("List is  ",L)
