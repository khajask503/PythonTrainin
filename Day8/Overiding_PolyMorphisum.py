###------------Polymorphisum--------------------
# One Method shouwing diffrent outputs is called as polymoprphisum
#
# class Human:
#     def wishes(self,Name=None):
#         if Name is not None:
#             print("Hello " +Name)
#         else:
#             print("Hello")
# m1=Human()
# m1.wishes("John")       #Hello John
# m1.wishes()             #Hello

# EX:1--------------------
# ---------------------------

class Calci:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
var=Calci()
var.add()                    #0
var.add(10,20,0)     #30
var.add(25,67,35)   #127
