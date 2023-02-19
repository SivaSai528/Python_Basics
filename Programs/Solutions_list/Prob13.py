#Write a program that takes a list of words and returns the length of the longest one.
L=eval(input("Enter a list   "))
mxstrlen=len(L[0])
mxstr=""
for i in range(len(L)):
   if len(L[i])>mxstrlen:
       mxstr=L[i]
print("longest word in alist",mxstr)

