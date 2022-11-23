import numpy as np
from numpy import random
# a = random.rand()   //rand is used to take float no's
a=random.randint(10000,104000)
print(a)

# b=np.array(["Apple","Carrot","Pinapple","Guava","MaNGO"])
# intarray = np.array([101,22,3,1,32,42])
# intarray = random.randint(500,size=(2,3))
# print(intarray)

demo =  random.choice([101,201],size=(2))
print(demo)

ran=random.choice([2,3,4,5,6,8],size=(2,3))
print(ran)

fruitbasket = np.array(["Banana","Carrot","Pinapple","Guava","Mango"])
abc=random.choice(fruitbasket,size=(5))
print(abc)
# random.shuffle(fruitbasket)   //make changes to original array
fbp =random.permutation(fruitbasket)  #doesnot make changes to original array

print("fruit basket is ", fruitbasket)
print("fruitbasketPermutataion  is ",fbp)