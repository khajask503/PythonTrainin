#When we want to import from two modules but we have same methods
#---------------------------------------------------------------------------------------
#Approach-1
# -----------
import Animal
import Bird

Animal.fly()              #Animal can't fly
Animal.colour()           #  Animal is green

Bird.fly()               #Bird can fly
Bird.colour()            #Bird is green

#Approach-2       with * ->symbol     (Practically these is badd approach rwriting import agaiun & Again go with 1st approach)
# -----------
from Animal import *
from Bird import *

# There is an Problem Calling import * at at time for two modules That is
# By calling the latest one only work previoues will be disabled,Once Example is done will show resolution
#Exampl:1  #---------Even we imported 2modules latest -2nd module methods are working & 1st module stopped/disabled

fly()                    #Bird can fly
colour()                 #Bird is green


# Resolution for above Issue--------
#Define Module and its imports INDIVIDUALYY one after anothe ***************(IMP POINT to remeber)

#Module 1----
from Animal import *
fly()                    #Animal can't fly
colour()                 #Animal is green

#Module 2----
from Bird import *
fly()                  #Bird can fly
colour()               #Bird is green