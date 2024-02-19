# #Strings-----------------
#
# #-----Diffrent Ways of creating strings---
s="Welcome"
s='Welcome'
s=str("Welcome")
s=str('Welcome')
# #
# # #--CReating Empty Strings------
# #
name =''
name=" "
name= { }
#
# #------Mutable & Immuatbalr----
# #Mutable- Value can be changed for variable
# #Immutable - value cannot be changed for variable
#
#1) is the strings are imutable ??->Yes  but can be changed after updation
#Ex:-
str1="Welcome"
print(id(str1))       # After printing 1540374401776
print(str1)           #Welocme   -->its imutable
#BUT I am updating the string value
str1=str1+"to Phyton" #Updation so it changed back to mutable
print(str1)           # Welcometo Phyton
# # #-----------------------------------------------------------------------------------------
# # #2)+ and * with String operations
# #
str="Hello world"
print("-----------Its + Operation+++++++++")
print(str+"ofPhyton Programing")               #Hello worldofPhyton Programing

print("-----------Its * Operation+++++++++")
print(str*2)                                 # ->Prints 2 times ->Hello worldofPhyton Programing
print(str*2+"of Devlop Programing")         #-  >Hello worldHello worldof Devlop Programing

# #-----------------------------------------------------------------------------------------
# #3)Slicing  with String operations
#
# #A)Data Pulling using index values
# #Syntax[A:B]
# A)Syntax[A:B]   Reminds ->start postiton
# B)Syntax[A:B]   Reminds ->Ending postiton
#c)if Starting position A is not given  Syntac [-:B] index will start from 0
#d)if Ending position B is not given  Syntac [A:-] index will start from A and ends ith string
#
str ='Welcome'
print(str[1:3])  #el
print(str[0:5])  #Welco
print(str[2:])  #lcome
print(str[1:-1]) #elcom
print(str[1:-2]) #elco
#
# #-----------------------------------------------------------------------------------------
# #4)ord() ,chr()  functions
# #---> For printing Values and nChracters of Ascii values
print(ord('A'))     #-->65
print(chr(65))       #-->A
#
# #-----------------------------------------------------------------------------------------
# #5)max() ,min() , len() functions
# #
print(max("abcddgsg"))  #-->s
print(min("agverh"))    #-->a
print(len("vfbvzgvgrbfz")) #-->12
#
# #-----------------------------------------------------------------------------------------
# #6)in ,notin operstores  and returns boolean values
#
s="Welcome"
#in-->Operatore
print("come" in s)   ##-->True
print("wedl"in s)    ##-->False
# e -->Operatore
print("come" not in s)   ##-->False
print("wedl"not in s)    ##-->True
#
#
# #-----------------------------------------------------------------------------------------
# #7)String comparsions
#
# #Here we use relation operatores the srtrings
# ==, !=, > , >= , < , <= , >
print("tim"=="tie")              #False
print("free"!="freedom")         #True
print("arrow">"aron")            #True
print("right">="left")            #True
print("teeth"<"tee")             #False
print("Yellow"<="fellow")         #True
print("abc">" ")                   #True

# # #-----------------------------------------------------------------------------------------
# #8)Testing strings True(or) false
s="Welcome Phython numer "
#(or)
#We can enter the string into print statment and checkwith function
#1)isalnum()---------
print("4739".isalnum())         # true
print (s.isalnum())            #Faslse --Beacuse its string not number

#2)isalpha()--------
print(s.isalpha())            #False
print("fbgfbvae".isalpha())     #true

#3)isdigit()-------------
print(s.isdigit())              #False
print("36467".isdigit())        # True

#4)is identifier()---------
#Phyton has Specified Default keywords if the string given is not identifier it will return false
print(s.isidentifier())                   #False
print("first number".isidentifier())       #False

#5)is lower()--------
#if the string conits al lower it returns true
print(s.islower())                           #False
print("vgjnergn".islower())                   #True

#6)is Upper()--------
#if the string conits al Upper it returns true
print(s.isupper())                           #False
print("FSKGMRAKGM".isupper())                   #True

#7)is Space()--------
#if the string conits Space it returns true
print(s.isspace())                           #False
print(" ".isspace())                          #True
#
# #*******************************************************************************************
# #9)------------ :- Searching for Substrings-------
# #Exa:-1 --EndsWith()--------
# # #if the string  Ends with particular string it returns true
s="Welcome to python"
print(s.endswith("thon"))           #True
print("welcome".endswith("come"))     #True
#
# #Exa:-2 --StartsWith()--------
# # #if the string  Starts with particular string it returns true
s="Welcome to python"
print(s.startswith("Welco"))           #True
print("welcome".startswith("welC"))     #False

# #Exa:-3 --find()--------
# # #if the string  find with particular string it returns poisition index or False
s="Welcome to python"
print(s.find("to"))                     #8 -->returns position
print("welcome".startswith("welC"))     #False
#
#
# #Exa:-4 --count()--------
# # #if the string  find with particular string charcter it returns count of index or Zero'0'
s="Welcome to python"
print(s.count("o"))                     #3 -->returns position
print("welcome".count("welC"))           #0
#
#
#
# #*******************************************************************************************
# #10)------------ :- Converting strings-------
#
# #Exa:-1 --capatalize()--------
# # these function helps to captalize the first leeter as capital only for first letterr of sentence
s="python to python"
print(s.capitalize())                   #Python to python ->First letter turned capital
print("welcome".capitalize())           #Welcome
print("WELCOME".capitalize())           #Welcome
#
# #Exa:-2 --tittle()--------
# # these function helps to captalize the first leeter as capital of Every word as title case
s="python to python"
print(s.title())                   #Python To Python ->First letter of every word turned capital
print("welcome BACK".title())           #Welcome Back
print("WELCOME".title())           #Welcome

# #Exa:-3--lower()  and upper()--------
# # these function helps to convert capital letters to small letters case vice versa with capital leettes to small
# #A_)lower
s="python to PYTHON"
print(s.lower())                   #python to python
print("welcome BACK".lower())           #welcome back
print("WELCOME".lower())           #welcome
# #B_)Upper
s="python to PYTHON"
print(s.upper())                   #PYTHON TO PYTHON
print("welcome BACK".upper())           #WELCOME BACK
print("WELCOME".upper())           #WELCOME

# #Exa:-4--swapCase()--------
# these function helps to convert and if small letter avialble them capital(camel casing)
s="python to PYTHON"
print(s.swapcase())                   #PYTHON TO python
print("welcome BACK".swapcase())           #WELCOME back
print("Welcome Pyhton".swapcase())           #wELCOME pYHTON

#
#Exa:-5--replace()--------
# these function helps to replace string with desitred user string
s="Welcome to PYTHON"
print(s.replace("PYTHON",'Pyathon'))                   #Welcome to Pyathon
print("welcome BACK".replace('BACK', "Again"))           # welcome Again

# #*******************************************************************************************
# # #11)------------ :- Reverse strings-------
# Method 1---
# ---------
s='welcome'
rev_str=""
for i in s:
    rev_str=i+rev_str
print(rev_str,"is Reversed String")  #emcolew

# Method 2---
# ---------
s='welocme'
rev_str=s[::-1]   #s[0:7: -1]
print (rev_str)                       #emcolew