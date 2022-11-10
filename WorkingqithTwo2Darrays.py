import numpy
zerod = numpy.array(90);
oned = numpy.array([32,43,12,32])
print("dimension if array zerod is ", zerod.ndim)
print("dimension if array oned is ", oned.ndim)
a = numpy.array([[12,2,4],[5,3,1],[34,55,77]])
threed = numpy.array([[[12,2,4],[5,3,1],[34,55,77]],[[12,2,4],[5,3,1],[34,55,77]]])
print("dimension if array a is ", a.ndim)
print("dimension if array threed is ", threed.ndim)
b = numpy.array([[2,1,4],[4,6,7],[34,5,6]])
print(a)
print(b)
print("sum of a and b is ",a+b)
print("max element of array a is ",a.max(axis=0))