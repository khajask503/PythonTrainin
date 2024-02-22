# # Example :-1
# #---------------------------------
print("These is starting point of Program")
print("These is starting point of Program")
#
# pritn(x)                                    #Exception occured as Expected now we wil handele it
# #
try:
    print(x)
except:
    print("----------Exception Occured")
    print("and its been handledd-----------------")

print("These is Ending point of Program")
print("These is Ending point of Program")

#  Example :-2--------------------------------------------------------
# # We can give exact Exception name and handle it (Bettr use normal except as first approach))
print("These is starting point of Program")
print("These is starting point of Program")

# print(10/0)                 #-->Expected :- ZeroDivisionError: division by zero
try:
    print(10/0)
except ZeroDivisionError:
   print("The Program is completed") # These is starting point of Program
                                       # These is starting point of Program
                                        # The Program is completed
try:
    print(10/0)
except:
     print("Exception occured and Handled")   # Exception occured and Handled
#
#
# # Example :-3-----MUltiple exception block---try, except, else, finally------------------------------------------------
#
try:
     num1,num2=10,0
     result=num1/num2
     print("Result is ", result)
except ZeroDivisionError:
     print(" ZeroDivision Exception Error occured and Handled")
 #Syntax Error
except SyntaxError:
     print("Thrown Syntax error.......")
except:
     print("Exception Handled")
#if Try Block is not handled above exception will handle


# #---------Else Block_-------------------
# --------> it will exceute only if above try block lines are not throwing exception and exceute properly
else:
    print("No Excecutin occured...........")
#
# #---------Finally Block_-------------------
# #---------> it will exceute always irrespective of any case
finally:
     print("Always Excecute")

# # Example :-4-----Creating user defined exceptions------------------------------------------------
def enternum(num):
    if (num<0):
        raise ValueError("Only Interger are allowed ")
    if num %2==0:
        print("These is even number")
    else:
        print( "These is odd Number")
enternum(2)
enternum(1)
# enternum(-1)       #Expected error-->  raise ValueError("Only Interger are allowed ")

#HAndling exception on calling function
print("Checking the num even is odd Number")
num=76
try:
    enternum(num)
except:
# except ValueError:
    print ("Value error and exception occured and Handled")
print("Program Completed")


