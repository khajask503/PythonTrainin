# # -------------------OOPS-------------------
# #------ How to create Class & Object----------------------
# #Example:-1  How to create Class & Object
#
# #When ever we write func() in the class it is called as method
# class myCl:
# # A)Method:-1
#     def myfun(self):            #Self means particular Methods belongs to particular userr definced class and it should not be removed
#         pass                    #-PassMeans none ->if we are implemrning Empty function we use these
# # B)Method:-2
#     def display(self):
#         print("john")
# #
# # #Creating Object of Class-----Come out of class(intendenation)
# # #OBJECT1--# Instantiate the class
# Var1=myCl()              # Synatax :- objet-Var = class  -->When you open () -> it means its method
# #OBJECT2--
# Var2=myCl()
# #
# # #Axcessing the object and Method of the class is by refrence object variabl
# Var1.myfun()
# Var1.display()
# Var2.myfun()
# Var2.display()
# # ---------------------------------------------------
# # Example;2 --Sending Arguments into method--------
# class myCl:
#     def funt(self,name):
#         print(name)
# Obvar1=myCl()
# Obvar1.funt("Johnathan")
#
# # ---------------------------------------------------
# # Example;3 -- 2 types of methods can be defined  within the class--------
# # A)instance Method (We can call through Object)    -> Its Like NON Static Method in java
# # B) Static Method (We can call directly using class and need to used ANnotation keyword @Staticmethod)
# #                  ->Where as Instance Method is default for Python
# #                -> Self keyword requires another Paramenter for Static method and not refering to any class
# #                ->Because self of Instance method and static method are diffrent
# class myClass:
#     def m1(self):
#         print("These is instance method")
#     @staticmethod
#     def m2(self, num):                   #-Here we will give parameter value for Self of static method
#         print(self,num)
# # #--------------Calling by Instance method
# mc=myClass()
# mc.m1()
# mc.m2(100,200)
# # #---------------Calling by class name---
# # myClass.m1()                          #__>Error expected becuase calling NonStatic instance method
# myClass.m2(10,30)
#
# # # ---------------------------------------------------
# # # Example: -- Crrating multiple objects for one -1-Class,.......
#
# class myclass():
#     def display(self,name):
#         print("these is my display method")
#         print(name)
#
# #Object 1------------
# obj1=myclass()
# obj1.display("john")  #these is my display method
#                       #john
# #Object 2-------------------
# obj2=myclass()
# obj1.display("Alxa")  #these is my display method
#                       #Alxa
#
#
# # -------------------#)Class Variables--------------------------------
# # Example:4 -- 2 types of Variable discussed till but there are 3rd one its class variables ,.......
# #Patreen of variables
# # A)Global Variables
# # B)Class Variables
# # C)Local Variables
#
# # A)Class Varaible-----------------
#
# class mCls:
#     a,b=10,20    #Class Variables beacuse we are creating inside the class
#     def add(self):
#         print(self.a + self.b)
#     def mult(self):
#         print(self.a * self.b)
#
# var1=mCls()
# var1.add()             #30
# var1.mult()            #200
#
# # # B)aLL tYPE vARIABLE eXAMPLE------------
#
# i,j=10,25           #Global Variables
# class mycls():
#     a,b=100,200                  #Class Variables
#     def add(self, x, y):          #Method --->
#         print(x+y)                #X & y are -->Axcessing Locall Variables     #550
#         print(self.a + self.b)    #Axcessing class aVaraibles                  #300
#         print(i+j)                #Axcessing i, j are Global variable          #35
#
# #Axcessing Method of all variables
# obj1=mycls()
# obj1.add(350,200)
#
#
# # C)Same Variables Names for aLL tYPE vARIABLE eXAMPLE------------
# #  1) global()['varaibale']                function to axcess when name are same--------------
#
# a,b=15,25           #Global Variables
# class mycls():
#     a,b=10,20                  #Class Variables
#     def add(self, a, b):          #Method --->
#         print(a+b)                 #Axcessing Local varaibles           #-->550
#         print(self.a + self.b)     # Axcesing Class  varaibles          #->30
#         print(globals()['a']+globals()['b'])        #Axcessing Global Variables     #-->40
#
# #Axcessing Method of all variables
# obj1=mycls()
# obj1.add(350,200)
# #******************************************************************************************
#----------------------------------------CONSTRUCTORE--------------------
# 1)__init__Constructore
# 2)--Str__Constructore
# ------------------------------------------
# Example :1
class myClass:
    def __init__(self):                                 #constructore Creation
         print("these is constructore")
    def myMeth(self):                                  #Method
        print("these is my method")
    def mymeth2(self,x,y):
        return (x+y)                                      #MEthod with returning value

var1=myClass() #On creation of method Object the constructore will get inocked-->>#.these is constructore
var1.myMeth()                                                                  #these is my method
v2=var1.mymeth2(15,55)
print(var1.mymeth2(10,20))                    #30
print(v2)                                           #70

#----------------------------------------------------------------------------------------------------------
#Example ;2 --------------------
# Construction With Arguments (Parameterized Constructore)
# ------------------------
class myClass:
    name="john"                                            #Class Variable
    def __init__(self,name):  #Local-variable-argumenrts to constructore-->Constructore is expecting Argument value which will come from object

        print(name)            #---->David
        print(self.name)       #----->John
Var1=myClass("Daid")              #->When ever constructed it gets invocked but here its parmetrized constructr so it expects the argument value

#----------------------------------------------------------------------------------------------------------
#Example ;3 --------------------
# Requiremtn:- 1) Create Class EMP
#               2) create constructore : eid , ename, sal
#                3)create display() method  : print (eid(), enamem ,sal)
# ------------------------
#
class emp:
    def __init__(self, ename, eid,sal):  #These Variables are local and cannot be asxces by method so we converting these local variables to class Var)
        self.ename =ename          #Converted to class Var
        self.eid = eid              #Converted to class Var
        self.sal = sal              #Converted to class Var
    def display(self):                    #Created method and printing the cconverted class variables
            print(self.eid,self.ename,self.sal)
e1=emp("Jonhatan",1047,45000)            #->When ever constructed it gets invocked but here its parmetrized constructr so it expects the --
                                                        # ------argument value
e1.display() #1047 Jonhatan 45000  ->Display() is not constructore so it can self invoke and it need to be called to print
e2=emp("Flexi",1038,72000)  #1038 Flexi 72000
e2.display()
#----------------------------------------------------------------------------------------------------------
#Example ;4 -----------Use ___STR__ constructre---------
#--> Str constructore only returns and prints sting type of data
#-->Second type of Constructoe
#-> Print the objec it will returnt he constructore varaible String data Only
#->Init constructor wont return but Str will return

# Requiremtn:- 1) Create Class EMP
#               2) create constructore : eid , ename, sal
#                3)create display() method  : print (eid(), enamem ,sal)
# ------------------------

class emp:
    def __init__(self, ename, eid, sal):
        self.ename = ename
        self.eid = eid
        self.sal = sal
    def __str__(self):
        return(self.ename)

e1=emp("Jonhatan",1047,45000)
print(e1)                                  #-->Jonhatan

