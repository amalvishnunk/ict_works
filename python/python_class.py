class Students:
    def __init__(self,x,y):
        self.name=x
        self.rollno=y
    def printdata(self):
        print("name= ",self.name)
        print("rollno= ",self.rollno)

    def getage(self,myage):
        print("age= ",myage)

s=Students("aaaaa",23)
# x=int(input("enter the age"))
# print(s.name)
# s.getage(x)
s.printdata()
