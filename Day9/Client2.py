# Packages Relation of requiremnt

# 1) Package1 ->Module1()
# 2)Package1->Package 2 (Subpackage) -- Module2()
# Req;- Mod 1 hsould be from pack1 and Mod2 should be from Subpack of pack1
# Approach-1---------------------------
#------------------------------------
import sys
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/Package1")
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/Package1/Package 2")
import Module1
import Module2

Module1.display()  #These is display function from module 11
Module2.show()     #These is show function from module 22
# NOTE--> Even with error program wil run issue with pychar]
# Approach-2---------------------------
#------------------------------------
import sys
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/Package1")
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/Package1/Package 2")
from Module1 import *                  #These is display function from module 11
from Module2 import *                 # These is show function from module 22

display()
show()
# NOTE--> Even with error program wil run issue with pychar]