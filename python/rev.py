a=int(input("enter a number"))
rev=0
n=a

while(a>0):
    rev=(rev*10)+(a%10)
    a=a//10

print(rev)