import numpy as np
# a = np.array([11,12,13,14])
# b =a.copy()
# a[1]=89
# print(a)
# print(b)

a = np.array([11,12,13,14])
b =a.view()
a[1]=89
b[2]=90
print(a)
print(b)
print("-----------------------")
a=np.array([[[3,4,5,6,7],[12,44,21,42,1]],[[31,41,51,16,17],[102,404,201,402,10]]])
b=a.copy()

for x in b:
    # print(x)
    for p in x:
        for t in p :
            print(t)

        print("******")