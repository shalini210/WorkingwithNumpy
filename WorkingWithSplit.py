import numpy as np
# a = np.array([11,22,33,44,55,66])
# n = np.array_split(a,5)
# print("a is ", a)
abcde=np.array([[[1,2,3,],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
c=np.array_split(abcde,2)
# print(" c is" , c)
# # print("n is ",n)
#
# print((c[1])[0,1,1])
print(abcde)
print(abcde[1,2,1])
# print(n[0])