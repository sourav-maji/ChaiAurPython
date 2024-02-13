import math
print(math.pi)
import random
print(random.random())
# choice with random
print(random.choice([6,1,2,3,4,5]))
userName = "chaiaurcode"
print(len(userName))
print(userName[0])
# userName[0] = "A"   # todo: typeError: 'str' object does not support item assignment
print(userName[-1])
print(userName[1:3])
print(dir(userName))
myList =[1,"Sourav",3.5]
print(myList[-2])
print(dir(myList))

myD ={"one": "lemon tea" , "two" : "masala chai" , "three": "ginger tea"}
print(myD["two"])
print(dir(myD))

myTup = (1,2,4)
print(myTup[2])
print(dir(myTup))
print(len(myTup))
print(myTup[-1])