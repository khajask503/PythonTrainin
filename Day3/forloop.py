#-----------------LOOPING STATMENTS--------------
#**********************************************
#1) While Loop
#2) For Loop

# 2) For loop--------------
#---------------------
#A) Print 1 to 10 Numbers using For loop
#1)
for i in range(10):
    print(i)           #0,1,2,3,4,5,6,7,8,9
# #2)
for i in range(1,11):
    print(i)             #1,2,3,4,5,6,7,8,9,10
#---------------------------------------------------------------------------
#B) Print only Even Numbers using from 1 to 20
# #1)
for i in range(0,12,2):
    print(i)            #Even number0,2,4,6,8,10
#------------------------------------------------------------------------------
#C)Print only odd Numbers using from 1 to 25
for i in range(1,25,2):
    print(i)            #ODD number 1,3 ,5,7,9,11,13,15,17,19,21,23
#------------------------------------------------------------------------------
#D)Prin Numbers  from 1 to 20 Descending order reverse

for i in range(20,1,-1):
    print(i)              #20,19,18,17,.....3,2.
#------------------------------------------------------------------------------
#=E)Prin Numbers  from 1 to 100 with diffrens of 5
for i in range(0,100,5):
    print(i)             #0,5,10,15....85,90,95.