class Employee:
    def __init__(self,getid,getname,getage,getsal):
        self.emp_id=getid
        self.name=getname
        self.age=getage
        self.salary=getsal
    def printdata(self):
        print("ID : ",self.emp_id)
        print("NAME : ",self.name)
        print("AGE : ",self.age)
        print("SALARY : ",self.salary)
        print("\n")

e1=Employee(101,"anil",26,25000)
e2=Employee(102,"athul",24,20000)
e3=Employee(103,"joseph",34,35000)
e4=Employee(104,"aji",25,22000)
e5=Employee(105,"sam",30,28000)


e1.printdata()
e2.printdata()
e3.printdata()
e4.printdata()
e5.printdata()
