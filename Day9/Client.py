#--Here we aare axcesing Pac1 -Files and functions From an package
# --------------------------------------------------------------------------------------------------

# Approach-1---------------------------
#------------------------------------
import sys                #SYS id a predfined module of Phyton
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/Pack1")

import Module1
import Module2

Module1.display()         #=->These is display function from module 1
Module2.show()            #-.>These is show function from module 2


# NOTE--> Even witjh error program wil raun ssue with pychar]


# Approach-2---------------------------
#------------------------------------
import sys                #SYS id a predfined module of Phyton
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/Pack1")

from Module1 import *
from Module2 import *

display()                          ##=->These is display function from module 1
show()                            # #-.>These is show function from module 2

# NOTE--> Even with error program wil run issue with pychar]