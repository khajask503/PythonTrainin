# -------------INHERITENCE-----------------

# EXAMPLE-1  --- Inheritence creation-----
#--------------------------------------------
class A:
    def m1(self):
        print("These is M1 -method of claas A")
class B(A):
    def m2(var):
        print("These is M2 -method of claas A")
var=B()
var.m1()
var.m2()

# EXAMPLE-2  --- Single Inheritence -----  1 parent 1 child
#--------------------------------------------
class A():
    x,y=10,20         #Class Variables
    def m1(self):
        print(self.x + self.y)

class B(A):
    a,b=200,100         #Class Variables
    def m2(self):
        print(self.a - self.b)
var1=B()
var1.m1()                    #30
var1.m2()                    #100

# EXAMPLE-3  --- Multi Level Inheritence -----  Parent A-to child follow single line
# #--------------------------------------------
class A():
    x,y=10,20         #Class Variables
    def m1(self):
        print(self.x + self.y)

class B(A):
    a,b=200,100         #Class Variables
    def m2(self):
        print(self.a - self.b)
class C(B):
    i,j=5,3
    def m3(self):
        print (self.i * self.j)
var1=C()
var1.m1()                    #30
var1.m2()                    #100
var1.m3()                    #15
#
# # EXAMPLE-4  --- HIREARCHY Inheritence -----  1 paent -2 child
# # #--------------------------------------------
class A():
    x,y=10,20         #Class Variables
    def m1(self):
        print(self.x + self.y)

class B(A):
    a,b=200,100         #Class Variables
    def m2(self):
        print(self.a - self.b)
class C(A):
    i,j=5,3
    def m3(self):
        print (self.i * self.j)
var1=B()
var1.m1()                    #30
var1.m2()                    #100

var2=C()
var2.m1()                        #30
var2.m3()                        #15


# EXAMPLE-5  --- MULTIPLE Inheritence ----- 2parents 1 single child
# #--------------------------------------------
class A():
    x,y=10,20         #Class Variables
    def m1(self):
        print(self.x + self.y)

class B:                 #Class agree even we dont gives ()
    a,b=200,100         #Class Variables
    def m2(self):
        print(self.a - self.b)
class C(A,B):
    i,j=5,3
    def m3(self):
        print (self.i * self.j)
var1=C()
var1.m1()      #30
var1.m2()      #100
var1.m3()      #15
#--------------------------------------------------------
#2)Inheritence ->Overiding Concept---------------------
# ->Creating two same methods with same names
#--> SUPER KEYWORD----USAGE----------
#-->It used to invoke parent class method
#-->Calling parent class from CHild class method using super()

# EXAMPLE-1  --- Method OverRiding
# #--------------------------------------------
class A():
    def m1(self):
        print("These is M1-Method from class A")

class B(A):
    def m1(self):
        print("These is M2-Method from class B")
        super().m1()
var1=B()
# var1.m1()  # With out super keyword/Function it retuns New Methods result -->#These is M2-Method from class B
var1.m1()    #With Super()-->   #These is M2-Method from class B
                               # These is M1-Method from class A


# # EXAMPLE-2  --- Axcessing parent  variable in child classses
# # #--------------------------------------------
class A:
    a,b=10,20                    #-->Class Varaibles
class B(A):
    i,j=100,300                   #-->Class Varaibles
    def m1(self,x,y):               #-->Local Varaibles
        print(x+y)                  #27
        print(self.i + self.j)      #400
        print(self.a+self.b)        #30
var=B()
var.m1(3,24)

# # EXAMPLE-3  --- Variable Overriding
# # #--------------------------------------------
class Parent:
    name="Scott"
class Child(Parent):
    name="Johnathan"
var=Child()
print(var.name)      #Johnathan

# # EXAMPLE-4  --- Variable Overriding and usage od Super() among variable
# # #--------------------------------------------
class Parent:
    name="Scott"
class Child(Parent):
    name="Johnathan"
    def m1(self):
        print(super().name)                 #By Using Super() we are cancling the overiding at avariable level
var=Child()
print(var.name)            #Johnathan
var.m1()                    #Scott


#--------------------------------------------------------
#3) ->Overiding METHODS---------------------
class Bank:
    def rateofInterst(self):
        return 0
class Ybank(Bank):
    def rateofInterst(self):
        return 10
class Xbank(Bank):
    def rateofInterst(self):
        return 20
var=Ybank()
print(var.rateofInterst())          #10
var=Xbank()
print(var.rateofInterst())            #20