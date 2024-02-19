# ------Range Function=-----------

# range() -> Values between range

print(1,10)                 #Just prints

print (range(10))           #1 10
print (list(range(10)))     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(range(1,10))          #range(1, 10)
print(list(range(5,10)))    #[5, 6, 7, 8, 9]

#********************Print all odd & Even Numbers
#---------------------------
#Syntax ->starting odd number ,range , skip2values
print (list(range(1,10,2)))  #[1, 3, 5, 7, 9]   -->ODD Number
#Syntax ->starting Even number ,range , skip2values
print (list(range(2,10,2)))  #[2, 4, 6, 8]      -->Even Number

#********************Print Numbers on Descending reverse order
#---------------------------
print(list(range(10,1,-1)))  #[10, 9, 8, 7, 6, 5, 4, 3, 2]

print (list(range(-10,-5)))  #[-10, -9, -8, -7, -6]

print(list(range(-10,-5,2)))  #[-10, -8, -6]