import numpy as np
a = np.array([12,42,12,32,11,12,32,123,12])
i  = np.where(a%2==0)
print(i)

b = np.sort(a)
print("a is : ",a)
print("b is :" ,b)
b=np.flip(b)
print("new b is ",b)
c=np.flip(a)
print(c)
# b[::-1])
basket = np.array(['Banana','Orange'])