# break Statments
#Break  continue

#A)Break
for i in range(1,20):
    if i==5:
       break
    print(i)    #1,2,3,4 -->once break meets loop exists

#B) Conitune
for i in range(1,20):
    if i==5:
       continue
    print(i)       #1,2,3,4 , ,6,7,8,..19,20  ->5 is missing but conitunes to 20 untils loop exists

#B) Conitune with multiple value Skips
for i in range(1,10):
    if i==5 or i==3 or i==7:
        continue
    print(i)              # 1,2,4,6,8,9