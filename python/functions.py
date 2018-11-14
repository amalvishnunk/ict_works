def display():
    print("welcome to python")

def add(a,b):
    return (a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)


x=int(input("enter number 1: "))
y=int(input("enter number 2: "))
print("sum = ",add(x,y))
print("diffrence = ",sub(x,y))
print("product = ",mul(x,y))
print("div = ",div(x,y))
