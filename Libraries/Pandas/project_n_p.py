import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Sales_data.csv')
df = pd.DataFrame(data)
print(df)
print()


print(df.isnull().sum())
print()


print(df.info())
print()


df['Sales per Month'] = df['Units sold'] * df['Price per Unit']
print(df)
print()


plt.subplot(1,2,1)
plt.plot(df['Month'],df['Sales per Month'])
plt.xlabel('Month')
plt.ylabel('Sales per Month')

plt.subplot(1,2,2)
plt.bar(df['Month'],df['Sales per Month'])
plt.xlabel('Month')
plt.ylabel('Sales per Month')
plt.show()


print("Average Units sold : ",df['Units sold'].mean())
print("Average Sales per month : ",df['Sales per Month'].mean())
print("Total annual Sales : ",df['Sales per Month'].sum())

max_sales = 0
month = -1

for i in range(0,len(df['Sales per Month'])):
    if df['Sales per Month'][i] > max_sales:
        max_sales = df['Sales per Month'][i]
        month = df['Month'][i]

print(f"Maximum sales of {max_sales} in {month}")

plt.pie(df['Sales per Month'],labels=df['Month'],autopct='%1.1f%%')
plt.title("Percentage Sales per Month")
plt.show()
