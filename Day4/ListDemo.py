#----------List Colletion-----------------
##How to create List Collection
# #Example-1
myList1=[10,20,30,40,50]
myList2=["apple","Bannaa","Cherry"]
myList3=["Apple","10","Bannaa","20"]
myList=list()

print(myList1)
print(myList2)
print(myList3)
print(myList)

# #Example-2 Axcccesing items from list
#-------------------------------------------
myList=["apple","Bannaa","Cherry"]
#A)----------Axcessing by Index
print(myList[0])
print(myList[1])
print(myList[-1])
print(myList[-2])

# #Example-3 Axcccesing items from list by (Range Of Indexes)
#-------------------------------------------
# A)
myList =["Apple","Bannana,""Cheery","Orangr","Kiwi","Melon","Mango"]
print(myList[2:5])           # Orangr","Kiwi","Melon
#B)Negative ranges
print(myList[-3:-1])          #['Kiwi', 'Melon']

# #Example-4 Changing items values from list by Index
#-------------------------------------------
#A)
myList =["Apple","Bannana,""Cheery"]
print(myList)           #["Apple","Bannana,""Cheery"]
myList[0]="orange"
print(myList)

# #Example-5 Read items from list using loop
#-------------------------------------------
#A)
myList =["Apple","Bannana,","Cheery"]

for i in myList:
    print(i)    #"Apple","Bannana,","Cheery"

# #Example-6Check items if list avialble or not
#-------------------------------------------
#A)
myList =["Apple","Bannana,","Cheery"]

if "Apple" in myList:
    print("Yes Desied fruit avialble")  #with "Apple" ->Yes Desied fruit avialble
else:
    print("No Apple is not avialble")  #When i given condition  (if "apple" in myList:)  like these
                                    #it returned No Apple is not avialble -,Because case sensitive


 # #Example-7---Check items avalble count from  list
 # -------------------------------------------
 # A) --Len()->Length Function find out the length of list

myList =["Apple","Bannana,""Cheery","Orangr","Kiwi","Melon","Mango"]
print(len(myList))          #6

# #Example-8 Pushing items into list using append() , insert()
#-------------------------------------------
#A)APPEND()
myList =["Apple","Bannana","Melon","Mango"]
myList.append("Goa")                       #-.['Apple', 'Bannana', 'Melon', 'Mango', 'Goa']
myList.append("Bannana")                   #-['Apple', 'Bannana', 'Melon', 'Mango', 'Goa', 'Bannana'] -->Duplicate added
print(myList)

#B)Insert()  --> it pan push new value at user prefered location my index values
myList =["Apple","Bannana","Melon","Mango"]
myList.insert(1,"Goa")          #-.['Apple', 'Goa', 'Bannana', 'Melon', 'Mango']-> Here we inserted after index one 1
print(myList)

# #Example-9- Deleting items into list
#-------------------------------------------
# A)POP()   -->Uses Index to remove
myList =["Apple","Bannana","Melon","Mango"]
myList.pop(0)
print(myList)                                    #  ['Bannana', 'Melon', 'Mango']

#B)Del Keyword not function   --> Uses Index to remove

myList =["Apple","Bannana","Melon","Mango"]
del myList [2]
print(myList)                                        #['Apple', 'Bannana', 'Mango']

# C)Clear()   -->Uses to clear all the List
myList =["Apple","Bannana","Melon","Mango"]
myList.clear()
print(myList)                           #[]


# #Example-10- Coping list
#-------------------------------------------
#A) list() --> Normal Assigning
myList1  =["Apple","Melon","Mango"]
myList2=list(myList1)
print(myList2)                           #['Apple', 'Melon', 'Mango']

#B) copy()  --> copying the whole list
myList1  =["Apple","Melon","Mango"]
myList2=myList1.copy()
print(myList1)                    #['Apple', 'Melon', 'Mango']
print(myList2)                    #['Apple', 'Melon', 'Mango']

# #Example-11- Combiing list -or- Joining List
#-------------------------------------------
#A) Using + Operatore
List1 =["A","B","C"]
List2 =[1,2,3]
List3=List1+List2
print(List3)       #['A', 'B', 'C', 1, 2, 3]

#B) Using Loop Statment ---
List1 =["A","B","C"]
List2 =[1,2,3]
for i in List1:
    List2.append(i)
print(List2)                #[1, 2, 3, 'A', 'B', 'C']

#c) Using Extend () ---
List1 =["A","B","C"]
List2 =[1,2,3]
List1.extend(List2)
print(List1)                  #['A', 'B', 'C', 1, 2, 3]

# #Example-12 Comparing  of whole Lists
#----------------------------------------------
#Sample-1
List1=(10,20,30)
List2=("A","B","C")
if List1==List2:
    print("Values of List are Equal")
else:
    print("Values of List are NOTEQUAL")  #Values of List are NOTEQUAL

#Sample2
List1=(10,20,30,"A")
List2=(10,20,30,"A")
if List1==List2:
    print("Values of List are Equal") #Values of List are Equal
else:
    print("Values of List are NOTEQ")