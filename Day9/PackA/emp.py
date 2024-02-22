class Employee:
    def __init__(self,eid,ename,sal):          #local variables  in Constructore
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def displayemp(self):
        print(self.eid,self.ename,self.sal)