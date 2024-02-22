#importing and calling the modules from diffrent python files (Callculatore File)
# -------------------------------------------------------------------
# APPROACH -1
# -------------------
import Calculatore                       #-------IMPORTING CLASS later Methods

Calculatore.add(100,20)    #120
Calculatore.mul(5,9)       #45

# APPROACH -2
# -------------------
from Calculatore import add,mul         #-------IMPORTING CLASS with specific methods
add(100,350)           #450
mul(2,18)             #36

# APPROACH -3
# -------------------
from Calculatore import *         #-------IMPORTING CLASS with All methods using * Symboll
add(25,89)          #114
mul(19, 5)          #95

