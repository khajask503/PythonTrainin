#----------Set Colletion-----------------
#-->Set ->{} = Curly Braces
#-->list  ->[] = Square Brackets
#--> tupple -> ()= Open Brackets

#-> its Unordered & Unidexed and represented using curly braces {}
##How to create SET Collection
mySet={"apple","Cherry","Bannaa"}     #Use Curly Brackets
print(mySet)                          #{'Cherry', 'Bannaa', 'apple'}

# #Example-1 Axcccesing items from Set by Loop
# #-------------------------------------------
mySet={"apple","Cherry","Bannaa"}
for i in mySet:
    print(i)                       #Cherry,apple,Bannaa

# #Example-2  items/Values avialbilty  from Set (Boolean) using -"IN"
# -------------------------------------------
mySet={"apple","Cherry","Bannaa"}

print("Cherry"in mySet)   #True
print("cherry"in mySet)   #False   #Case sensiitve

# #Example-3->Add items/Values avialbilty to Set  using -"ADD()",UPDATE()
# -------------------------------------------
#A)ADD()-->it add single item
#B)UPDATE()  --->it adds Multiple items

#A)ADD()--------
mySet={"apple","Cherry","Bannaa"}
mySet.add("Watermelon")
print(mySet)                       #{'Watermelon', 'apple', 'Bannaa', 'Cherry'} ->Unordered& Unindexed

#B)UPDATE()  -----------------
mySet={"apple","Cherry","Bannaa"}
mySet.update(["Watermelon","Pineapple","Mango"])
print(mySet)             #{'Mango', 'Bannaa', 'Pineapple', 'Watermelon', 'Cherry', 'apple'}->Unordered& Unindexed

# #Example-4->Find Number of items/Values avialbile on Set using -len()
# -------------------------------------------
# A)len()
mySet={"apple","Cherry","Bannaa"}
print(len(mySet))                   #3


# #Example-5->Remove items/Values avialbile on Set using - removre(), discard()
# -------------------------------------------
# A)remove()  -->It trhows error if try to remove non avialble items
#B)Discard() -->It Dosent Throw  error if try to remove non avialble items
#--------->It dosent have index values so we need to gives values directly
# A) Remove()
mySet={"apple","Cherry","Bannaa"}
mySet.remove("apple")
print(mySet)                       #{'Cherry', 'Bannaa'}
#------
# #Ex- A.1)-->If wery to remove not avialble item set will throw error
mySet.remove("xyz")                #(KeyError: 'xyz')  -.As expected
print(mySet)

#----------------------------------------------
#B)Discard()
mySet={"apple","Cherry","Bannaa"}
mySet.discard("apple")
print(mySet)                   # {'Cherry', 'Bannaa'}
# # #Ex- B.1)-->If wery to discard() not avialble item set will throw error
mySet.discard("xyz")                #No errore are expected
print(mySet)                        #{'Bannaa', 'Cherry'}


# #Example-6->Clearing and deleting the  items/Values avialbilty to Set  using -"clear()",Del
# -------------------------------------------
#A)Clear()-It removes the data from set
#B) Del  - It removes the ALL set with all data

#A)Clear()-->it clears only data
mySet={"apple","Cherry","Bannaa"}
mySet.clear()
print(mySet)                      #set()
# -----------
#B)Del()-->it Deletes only data
mySet={"apple","Cherry","Bannaa"}
del mySet
print(mySet)          #-.Error Expected because set is deleted before print statment executed

# #Example-7->Joining of 2 set --Union()
# -------------------------------------------
# A)Update
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)                        #{1, 2, 3, 'c', 'a', 'b'}

# B)Update
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)                        #{1, 2, 3, 'c', 'a', 'b'}

