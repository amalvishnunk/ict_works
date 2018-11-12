a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))

if(a>b):
    g=a
else:
    g=b
if (c>g):
    g=c
    
print(str(g)+" is the greatest")