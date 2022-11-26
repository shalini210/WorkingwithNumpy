import pandas
# import pandas as pd
# print(pandas.__version__)
a1 =[11,25,63,54,25]
print(a1)
s1 = pandas.Series(a1)
print(s1)
print("accessing element atindex 2 ",s1[2])
s2 = pandas.Series(a1,index=["A","B","C","D","E"])
print(s2)
print(s2["C"])

student_name=["karan","yatin","ankit"]
student_marks=["77","44","a+"]

b2=pandas.Series(student_marks,index=[student_name])
print(b2)
print("Marks of Karan is ",b2["karan"])
#marks of karan are 77