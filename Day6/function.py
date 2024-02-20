#--------------------Functions---------------
#Example -1 ---Creating FUnctions----------
#----------------------------------
#A)Creating Function and calling it---------
def myfun():                 #Here We defined one gunction
    print("Hello")           #0 -> but it will be printed on calling similar to method in jave
myfun()                      #Prints -->Hello
# ---------------------------------------------------------------------------------------
# #B)Sending parameter varaible in function  and calling it---------
def myfun(Name):              #Arguments
    print("Hello", Name)
#--Calling Function with Parameter Input--
myfun("john")                 #  Hello john

#---------------------------------------------------------------------------------------
#C)Sending Multiple parameter varaible in function  and calling it---------
def cal(a,b):
    return(a+b)
# C.1) Intitliazing with Variable
sum=cal(100,300)
print(sum)                     #400

# # C.2) Direct intilaztion of values to Function
print(cal(100,300))      #400

#C.3-------Printng and Intilizing ways of Functions
def cal(a,b):
    print(a+b)         #Printing
cal(10,30)                   #40

def cal2(a,b):
    return(a+b)        #intilizing through return
print(cal2(10,30))
# ---------------------------------------------------------------------------------------

# D)------None Print using empty function()---------
def Fun():
    return        # If we didint specifiy any alue the func()n will return none

N=Fun()
print(N)               #None

#D.1 ) None -2 Prgm mehod
def fun():
    i=76
print(fun())            #None
