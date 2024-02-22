class Student:
    def __init__(self,sid,sname,grade):          #local variables  in Constructore
        self.sal=sid
        self.sname=sname
        self.grade=grade
    def displaystu(self):
        print(self.sal,self.sname,self.grade)