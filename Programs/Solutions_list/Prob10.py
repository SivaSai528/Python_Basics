#Write a program that takes two lists and returns True if they have at least one member in common, False otherwise
L=eval(input("Enter a list 1  "))
m=eval(input("Enter a list 2  "))
c=0
for i in L:
   if i in m:
       c=1
       break
if c==1:
    print(True)
else:
    print(False)

