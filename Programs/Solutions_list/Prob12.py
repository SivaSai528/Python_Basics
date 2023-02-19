#Take a list of words and create another list of integers representing the lengths of the correponding words.
L=eval(input("Enter a list   "))
m=[]
for i in L:
   m.append(len(i))
print("lengths of a list",m)

