import  numpy as np
a = np.array([12,3,23,1],dtype='S')
print(a)
print(a.dtype)
b = np.array(['Apple','Banana','orange'])
print(b)
print(b.dtype)
names = np.array(['1','2','3'],dtype='i')
print(names)
print(names.dtype)
array1 = np.array([12.2,32.1,3.4,5.5])
array2 = array1.astype('i')
print(array1)
print(array2)
# x =1,0,2,4,3
# y = it will store the boolean array created by using array x bool
x=np.array([3,4,5,6,1,0])

y=x.astype(bool)
print(y)
