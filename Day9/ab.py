#----------------Importing Multiple Clases into single classe---
# Approach --1
# ----------------
import a
import b

a1=a.Animal()        #Object
a1.display()        #I like Elephant

b1=b.Bird()        #Object
b1.display()        #I like Parrot

# Approach --2   -->from module name Importing specific methods ,functions
# ----------------
from a import Animal
from b import Bird

a2=Animal()        #Object
a2.display()        #I like Elephant

b2=Bird()        #Object
b2.display()        #I like Parrot
