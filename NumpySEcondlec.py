import  numpy
a = numpy.array([123,32,31,31,2312,312])
print(a)
print("value at index 2 is "+ str(a[2]))
a2 = numpy.array([[2 ,5 ,6],[2,3,6]])
print(a2)
print("Dimension of array a is : "+ str(a.ndim))
print("Dimension of array 2 is : "+ str(a2.ndim))
print("Each element of array a has size : ", a.itemsize, " bytes")
print("value at index 1,2 is ", a2[1,2])
print("max element in array a is ",a.max())
print("max element in array a2 is ",a2.max())
print("min element in array a is ", a.min());
print("min element in array a2 is ", a2.min())
print(a2+1)
print(a2)
a2= a2+1
print(a2)