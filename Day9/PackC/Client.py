# # Approach-1---------------------------
# #------------------------------------
import sys
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/PackA")
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/PackB")

import emp
import Stud

# # creating objects for classes and the sending argument to Constructores in the aboce inported class
#
e1=emp.Employee(102," Jonhathan ",18000)
e1.displayemp( )

s1=Stud.Student(25," Thosmon ","86%")
s1.displaystu()

# Approach-2---------------------------
#------------------------------------

import sys
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/PackA")
sys.path.append("F:/Python by pavan sir/PythonTraining/Day9/PackB")
#
from emp import Employee
from Stud import Student

e1=Employee(102," Jonhathan ",18000)
e1.displayemp( )
s1=Student(25," Thosmon ","86%")
s1.displaystu()
 #------------------------USing Stars * after import-----------
from emp import *
from Stud import *
e1=Employee(102," Jonhathan ",18000)
e1.displayemp( )
s1=Student(25," Thosmon ","86%")
s1.displaystu()