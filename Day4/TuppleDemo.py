#----------Tupple Colletion-----------------
##How to create Tupple Collection
# myTupple=("apple","Bannaa","Cherry")     #Use Normal Brackets
# print(myTupple)                          #('apple', 'Bannaa', 'Cherry')

# #Example-1 Axcccesing items from Tupple by (Range Of Indexes)
#-------------------------------------------
#A) ByIndex
# myTupple=("apple","Bannaa","Cherry")
# print(myTupple[1])                   #Bannaa
# print(myTupple[-1])                  #Cherry

#B) By Range of Indexes  i want to pull mutlitple values

# myTupple=("apple","Bannaa","Cherry","Goa","Kiwi","watermelon")
# print(myTupple[2:5])                                          #('Cherry', 'Goa', 'Kiwi')
# print(myTupple[-4:-2])                                        #('Cherry', 'Goa')

# #Example-2 Changing/Modifing item vaues from Tupple by converting to list and next reconverting back to Tupple
#-------------------------------------------------------------------------------------------------------
#By Default tupple is Immutable hence it will not allow modifictions
#But there is an workarroung
#Tuuple ->Convert to list  -->Reconvert to tupple

# myTupple=("apple","Bannaa","Cherry",65,34,"A")
# myList=list(myTupple)         #Tupple converted List
# myList[0]="Orange"             #Needed changes done on tupple
# myTupple=tuple(myList)        #Converted back to tupple
# print(myTupple)              #('Orange', 'Bannaa', 'Cherry', 65, 34, 'A')

# #Example-3 Reading Tupple Items from Loop
#----------------------------------------------
#A)LOOP
# myTupple=("apple","Bannaa","Cherry",65,34,"A")
# for i in myTupple:
#     print(i)           #"apple","Bannaa","Cherry",65,34,"A

# #Example-4 Searching items on Tupple avialble or not using if loop
#----------------------------------------------
#A)LOOP
# myTupple=("apple","Bannaa","Cherry",65,34,"A")
#
# if "Banna" in myTupple:
#     print("Yes the Serch item avialble")
# else:
#     print("No Search item not aviablr")  #No Search item not aviablr

# #Example-5 Tuple lenght -Count lenght of  items on Tupple
#----------------------------------------------
#A)len() --Length Function
# myTupple=("apple","Bannaa","Cherry",65,34,"A")
# print(len(myTupple))                            #6

# #Example-6 -Add Items into Tuplee
#----------------------------------------------
#Here we can convert to list and do the change and reconvert back

# #Example-7 -Coping Tuplee
#----------------------------------------------
# myTupple=("apple","Bannaa","Cherry",65,34,"A")
# myTupple2=myTupple
# print(myTupple2)          #('apple', 'Bannaa', 'Cherry', 65, 34, 'A')

# #Example-8 -Removinf items in Tuplee --> Not possible because its immutable
#----------------------------------------------
# myTupple=("apple","Bannaa","Cherry",65,34,"A")
# myTupple.remove("Bannaa")   #Error as epected-> AttributeError: 'tuple' object has no attribute 'remove'
# print(myTupple)

# #Example-9 Deleting whole Tuplee
#----------------------------------------------
# myTupple=("apple","Bannaa","Cherry",65,34,"A")
# del myTupple
# print(myTupple)    #Error -> Beacusee its all ready delted  ->NameError: name 'myTupple' is not defined

# #Example-10 Joining /Combining  of whole Tuplee
#----------------------------------------------
#A)Using + Operation
# Tuple1=(10,20,30)
# Tuple2=("A","B","C")
# tuple3= Tuple1+Tuple2
# print(tuple3)     #(10, 20, 30, 'A', 'B', 'C')

# #Example-11 Comparing  of whole Tuplees
#----------------------------------------------------
#Sample-1
# Tuple1=(10,20,30)
# Tuple2=("A","B","C")
# if Tuple1==Tuple2:
#     print("Values of Tupple are Equal")
# else:
#     print("Values of Tupple are NOTEQUAL")  #Values of Tupple are NOTEQUAL

#Sample2
Tuple1=(10,20,30,"A")
Tuple2=(10,20,30,"A")
if Tuple1==Tuple2:
    print("Values of Tupple are Equal") #Values of Tupple are Equal
else:
    print("Values of Tupple are NOTEQUAL")
