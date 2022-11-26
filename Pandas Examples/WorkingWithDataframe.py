import pandas as pd
a ={
    "name":["Ron","Raman","Zeel"],
    "Marks":[23,53,12]
}
b=[[1,2,3],[5,6,7]]
s = pd.DataFrame(a)
print(s)
s2=pd.DataFrame(b)
print(s2)

a1={
    "Country":["Usa","India","CHina"],
    "Population ":[300,1.5,1.3]}
a2=pd.DataFrame(a1)
print(a2)
print("The ppulation of inida is ",a2["India"]