def palind(a):
    rev=0
    n=a
    while(a>0):
        rev=(rev*10)+(a%10)
        a=a//10

    if n==rev:
        return True
    else:
        return False    


x=int(input("enter a number"))
if(palind(x)):
    print("number is palindrome")
else:
    print("number is not palindrome")    