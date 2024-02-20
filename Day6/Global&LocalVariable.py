# ---------------Global & Local Variable-------------------------------
# Global Vatiables can be created and axccesed IN-Side & Out_side of Function
#local varaible if created need to be done within the initndation of function to get created

#Example --1) Creating And Understand of Global & Local Variable
Global_Var=20           #--Global variable
def fun():
    local_Var=10
    print(local_Var)     #-Local variable with in fucntion intindation
    print(Global_Var)
#Calling Function
fun()

# print(local_Var)      #->Error Expected -> Because local variable axced out of Function intindation
print(Global_Var)

# --------------------------
# Example ;_2  --Priority of global or local in Funcxtin??
xy=100     #-->GlobalVariable
def cool():
    xy=200
    print(xy)        #200  -->Prints Local variable from function as Priority
cool()

# --------------------------
# Example ;_3  --Axcessing and updating local variable from function "Global keword"-----
# ----Using Global Variable  inlocal varibael  and he updating the value usin keyword
xy=200     #-->GlobalVariable
def cool():
    global xy          #local variable but by giving Global word its proeprties changed to global
    xy=300             #Changed to global variable
    print(xy)          #300  -->
cool()
print(xy)               #300 #changes will be effected ever were iresepective of in or out of funct()


# --------------------------
# Example ;_4  - Global keyword can be created inside of function even we dont have global variable outside
def cool():
    global xy
    xy=10
    print(xy)
cool()              #10
print(xy)           #10
