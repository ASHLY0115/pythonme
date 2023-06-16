import pandas as pd
import matplotlib.pyplot as plt




# print(rd.head())
# print(rd.shape)
# print(rd.dtypes)
usecol=['cgpa','name']
rd=pd.read_csv('sample.csv')
print(rd)
rd.plot(kind='scatter',x='date',y='temperature')
plt.show()
