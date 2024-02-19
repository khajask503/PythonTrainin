#  #--input AND output formatinG
# #A)iNPUT APPROACH---1
# name='john'
# age='30'
# sal=5000.60
# #b)iNPUT APPROACH---2
# name,age,sal='john',30,5000.60
# #-----------------
# #A)output/o/p APPROACH---1
# print(name)
# print(age)
# print(sal)
# #B)output/o/p APPROACH---2
# print(name, age, sal)

#--To Print Meaning full data with Genral infor ---
#Approach 1---
# name,age,sal='john',30,5000.60
# print ("-------------------Approach 1 ----------------")
# print("Name is ", name)
# print("age is ",age)
# print("Sal is ", sal)

#
# #Approach 2---
# # # name,age,sal='john',30,5000.60
# # we use % after General data with data type representing letter for example
# # Int=%d is (%d=digit)\
# # String=%s is (%s=string)
# # dcimale=%g is(%g=decimal)
#
# name,age,sal='john',30,5000.60
#
# print("Name is :%s Age is :%s Salary is :%g" %(name,age,sal))


#Approach 3---

name,age,sal='john',30,5000.60
print("Age is {} ,Name is {}  ,Sal is {}".format(age,name,sal))







