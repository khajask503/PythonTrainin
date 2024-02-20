#----------Dictionary Colletion-----------------
#-->Set ->{} = Curly Braces
#-->list  ->[] = Square Brackets
#--> tupple -> ()= Open Brackets
#-> its Unordered & Changeble(Mutable) and UNIndexed and represented using curly braces {}
#These has Curly braces
#Key are Unique but Values can be duplicated
#  KEY          Value
#produt1         100
#produt2         100(Duplcate values are allowed)
#produt3         500
#produt2         300

# #Example:1--Creaing an Dictionary
Dict={101:'X', 102:45, 103:'Salary'}
print(Dict)                            #{101: 'X', 102: 45, 103: 'Salary'} ->Unorderd outputs also expected

#Example:2--Axccesing the items from an Dictionary Using key and Get()
#1)Accesing by Key
#2)Using Get ()

Dict={
    "Brand":"Huwaie",
    "Model":"i10",
    "Year": 2021
}
# #A)Accesing by Key
print(Dict["Brand"])        #Huwaie
print(Dict["Model"])        #i10

# #B)Using Get ()
x=Dict.get("Brand")
print(x)                     #Huwaie
print(Dict.get("Model"))     #i10

#---------------------
#Example:3--Change  the items/Values in Dictionary Using key
#1)Changing by Key & also adding we can notice
Dict={
    "Brand":"Huwaie",
    "Model":"i10",
    "Year": 2021
}
print(Dict)        #{'Brand': 'Huwaie', 'Model': 'i10', 'Year': 2021}                  ->Before changing

# Dict["year"]=2024    #{'Brand': 'Huwaie', 'Model': 'i10', 'Year': 2021, 'year': 2024} -->Added
Dict["Year"]=2024      #{'Brand': 'Huwaie', 'Model': 'i10', 'Year': 2024}                -->After changed
print(Dict)
#---------------------
#Example:5--Reading  the items/Values in Dictionary Using loop
#1)Looping
#2)Value() only pull values but no keys
#3)items()  Pulss both key and values

Dict={
    "Brand":"Huwaie",
    "Model":"i10",
    "Year": 2021
}
#A) By Looping we can extract only keys later valuees you can learn
for i in Dict:
    print(i)       #Brand, Year, Model  -->Recived only keys

# #B) Now we will try to get values
for i in Dict:
    print(Dict[i])   #Huwaie, i10,2021

#C)--Using Values() funcion-------------
for i in Dict.values():
    print(i)           # #Huwaie, i10,2021

#D)Using items() function-------------
for x,y in Dict.items():
    print(x,y)            #Brand Huwaie ,Year 2021,Model i10

#---------------------
#Example:6--Chekcing/finding the key avialbilty in Dictionary Using loop
# A)
Dict={
    "Brand":"Huwaie",
    "Model":"i10",
    "Year": 2021
}
if "Model" in Dict:
    print ("Key Avialble")             #Key Avialble
else:
    print("Key not avialble")

#B)-----------
print(2021 in Dict)    #its a value -->False
print("Year" in Dict)    #its a Key -->True
#---------------------
#Example:7--Number of items avialbile in Dictionary using len()
# A)len() Function

Dict={
    "Brand":"Huwaie",
    "Model":"i10",
    "Year": 2021
}
print(len(Dict))                  #3   ->Number of items
# # #---------------------
#Example:8--Adding items into Dictionary using
# 1)Using key

Dict={
    "Brand":"Huwaie",
    "Model":"i10",
    "Year": 2021
}
Dict["Colour"]="Red"
print(Dict)         #{'Brand': 'Huwaie', 'Model': 'i10', 'Year': 2021, 'Colour': 'Red'}

#Example:9--Remove and clearing only data items from Dictionary using and deleting whole dictionary
# A)Using POP()
#B) USing del to remove individal or whole dectionary
#3)Clear()   -->it used to clear all the data insude dictionary but Dictinary will be avialble

# A)Using POP()
Dict={
    "Brand":"Huwaie",
    "Model":"i10",
    "Year": 2021
}
Dict.pop("Year")
print(Dict)                     #{'Brand': 'Huwaie', 'Model': 'i10'}

#B) USing del

del Dict ["Year"]
print(Dict)                        #{'Brand': 'Huwaie', 'Model': 'i10'}

#C) Usinf Del to remove dictionary

del Dict
print(Dict)                           #Error Expected --.NameError: name

#D) Usinf Clear to Clear all list from dictionary

Dict.clear()
print(Dict)                              # {}  ->empty directory


#Example:10--Copiying dictionary
# A)Using" = " Operatore witout using copy().
#B)Using copy()
#--------------------------
# A)Using" = " Operatore
Dict={
    "Brand":"Huwaie",
    "Model":"i10",
    "Year": 2021
}
Dict2=Dict
print(Dict)                            #{'Brand': 'Huwaie', 'Model': 'i10', 'Year': 2021}

#B)Using copy()----------------------
Dict2=Dict.copy()
print(Dict2)           #{'Brand': 'Huwaie', 'Model': 'i10', 'Year': 2021}