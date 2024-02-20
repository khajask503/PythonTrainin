# ---------------2 Types of Arguments /Paramentes -------------------------------
#->to the function we can pass 2 typoes of arguments
# 1)Positional arguments
# 2) Keyword Arguments

#1) Positional Agument------------------
def func(i,j):
    print(i,j)
func(10,20)    #10 , 20     -> Here the values added acording to positions


# #2) Keyword Arguments------------------
def func(i,j):
    print(i,j)
func(j=10,i=20)     #20,10     ->here using Keyword we overlapped he posistions


#Example 1);---Default value Assigned to Positional argument---------
def func(i,j=10):          #Default values are replaced
    print(i,j)
func(100,200)        #100,200
func(190)

# Example 2);---Keyword Argumens examples---------
def func(greetmsg, name):
    print(name +"  "+greetmsg)
func(name="john",greetmsg="Welcome")          #john  Welcome
func(greetmsg="Welcome",name="Twinkle ")      #john  Welcome

# # Example 3);---Positional Argumens examples---------
#
def func1(a,b,c):
    print(a,b,c)
func1(10,20,30)   #10 20 30 ->Posotional
func1(a=10, b=30,c=20)     #10 30 20 ->Keyword Arguments
func1(b=10, a=30,c=20)     #30 10 20 ->Keyword Arguments
func1(10,20,c=40)    #10 20 40  ->Combination of of Keyword and combinational arguments
func1(10,b=20,c=45)     #10 20 45  ->Combination of of Keyword and combinational arguments

#-----IMPORTANT RULE TO Remeber-------------------------
# func1(10,b=20,45)         #-->Error Expected ->.Positional argument after keyword argument->it means positioanl args are expected before any ketword args
                            # SyntaxError: positional argument follows keyword arguments
func1(10,45,b=20)         #Syntax coorect but logcial invaid expected error


# Example 4);---Functios can Retuns Multiple values examples---------

def large(a,b):
    if(a>b):
        print("A--> is greater")
    else:
        print("B-->is greater")
large(33,37.)   #B-->is greater

# B)
def large(a,b):
    if(a>b):
        return a,b
    else:
        return b,a
print(large(33,47.))   # ------>(47.0, 33)
# --------------------------------------------
# Example 5);---Function Retuns collection Arguments types examples---------
def large(a,b):
    if(a>b):
        return a,b
    else:
        return b,a
print(large(33,47.))
#-----String the values in variable---
res=large(20,30)
print(res)              #(30, 20)
print(type(res) )       #<class 'tuple'>
                          #-->Set ->{} = Curly Braces
                          #-->list  ->[] = Square Brackets
                          #--> tupple -> ()= Open Brackets