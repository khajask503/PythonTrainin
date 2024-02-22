# # ------------File Handling----------------
# We sent 2 paraments in Predefined function open(path, mode)
# 1)Path
# 2)Mode -->Read, write & Append mode
# 3) Every time file should be opend it should be closed dont forget
# 4) and to to mode operations in use letters at end --> w,r,a

# Example:1----Write into file------------
#
file=open("F:/Python by pavan sir/Pyhton Notes/DemoFiles.txt",'w')
file.write(" These is First Statment \n")
file.write(" These is Second Statment \n")
file.write(" These is Third Statment \n")
# file.write(" These is Fourth Statment \n")
file.write(" These is Fifth Statment \n")
file.close()
print("Program is completed")

# Example:2----Reading file------------
# ------------------------------------------------
file=open("F:/Python by pavan sir/Pyhton Notes/DemoFiles.txt",'r')    #Changed "r" to read
print(file.read())
file.close()
# --------------OUTPUT RECIVED_------
# These is First Statment
#  These is Second Statment
#  These is Third Statment
#  These is Fourth Statment
#  These is Fifth Statment

# Example:3----Appending data file------------
# ------------------------------------------------
file=open("F:/Python by pavan sir/Pyhton Notes/DemoFiles.txt",'a')    #Chmaged " a" to append the file
file.write(" These is Sixth Statment \n")
file.write(" These is Seventh Statment \n")
file.close
print("program is closed")
