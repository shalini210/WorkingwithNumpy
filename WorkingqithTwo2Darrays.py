import numpy
a = numpy.array([[12,2,4],[5,3,1],[34,55,77]])

b = numpy.array([[2,1,4],[4,6,7],[34,5,6]])
print(a)
print(b)
print("sum of a and b is ",a+b)
print("max element of array a is ",a.max(axis=0))