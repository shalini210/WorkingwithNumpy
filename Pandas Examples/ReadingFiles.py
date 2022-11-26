import  pandas as pd
d = pd.read_csv('SampleFile.csv')
print(pd.options.display.max_rows)
pd.options.display.max_rows=89
print(pd.options.display.max_rows)
j = pd.read_json('example_2.json')
print(j.to_string())
print(j.info())
print(d.head())
print("above is head and below is tail")
print(d.tail())