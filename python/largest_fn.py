def large(a,b,c):
    g=0
    if(a>b):
        g=a
    else:
        g=b
    if(c>g):
        g=c
    return g

x=int(input("enter number 1: "))
y=int(input("enter number 2: "))
z=int(input("enter number 3: "))
print("largest= ",large(x,y,z))
