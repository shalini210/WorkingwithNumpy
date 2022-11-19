import  numpy as np
a = np.array([23,44,23,12,44,5522,22])
#
# b =[True,False,False,True,False,True,False]
#
# n =a[b]
# print(n)
f=[]
for x in a:
    if(x%2==0):
        f.append(True)
    else:
        f.append(False)
print("a is ", a)
print("filter is ",f)
n = a[f]
print("filtered array is ",n)