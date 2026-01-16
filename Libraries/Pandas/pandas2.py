import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# df = pd.read_csv("csv1.csv")
# print(df)
# print()
# df = df.drop_duplicates()
# df = df.drop_duplicates(subset=[''])
# print(df)
# print()
# print(df.info())
# print()
# print(df.describe())
# # df['JoinDate'] = pd.to_datetime(df['JoinDate'])
# print()
# df.rename(columns={'name': 'Name'}, inplace=True)
# df.rename(columns={'gender': 'Gender','maths':'Maths'}, inplace=True)
# print(df)
# print()


# data = {
#     'Name': ['Anna', 'Bob', 'Anna'],
#     'Score': ['85', '90', '85'],
#     'Joined': ['2021-01-01', '2021-02-15', '2021-01-01']
# }
# df = pd.DataFrame(data)
# print(df)
# print()
# print(df.describe())
# print()
# print(df.info())
# df['Score'] = df['Score'].astype(int)
# df['Joined'] = pd.to_datetime(df['Joined'])
# print()
# print(df.info())


# df = pd.DataFrame({
# 'Name': ['Alice', 'Bob', 'Charlie'],
# 'Score': [85, 90, 95]
#   })

# def to_grade(score):
#     if score >= 90:
#         return 'A'
#     elif score >= 80:
#         return 'B'
#     else:
#         return 'C'
  
# df['Grade'] = df['Score'].apply(to_grade)
# print()
# print(df)

# df = df.sort_values(by='Score',ascending=False)

# print()
# print(df)

# df = df.sort_values(by='Score',ascending=True)

# print()
# print(df)

# df['Rank'] = df['Score'].rank(ascending=False)


# print()
# print(df)



# df = pd.DataFrame({
#   'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT'],
#   'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#   'Salary': [50000, 55000, 48000, 52000, 60000]
#     })
    
# print()
# print(df)    
# print()
# grouped = df.groupby('Department')['Salary'].agg(['mean', 'max', 'min'])
# print(grouped)
# grouped = df.groupby('Department')['Salary'].agg(['mean'])
# print()
# print(grouped)
# print()



# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8],'C':[10,20]})

# df = pd.concat([df1, df2], axis=0)
# print(df)

# dates = pd.Series(['2024-01-01', '2024-01-05', '2024-01-10'])
# converted = pd.to_datetime(dates)
# print(converted)

# df = pd.DataFrame({
#   'Date': pd.to_datetime(['2024-01-01', '2024-02-15', '2024-03-30'])
# })
# print(df)
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day
# print()
# print(df)
# df = df.drop(columns=['Date'])
# print()
# print(df)


# df = pd.DataFrame({
#   'Date': pd.date_range('2024-01-01', periods=10, freq='D'),
#   'Sales': [100, 120, 90, 150, 80, 200, 170, 160, 130, 110]
# })
# df.set_index('Date', inplace=True)

# weekly = df.resample('W').sum()
# print(weekly)




# df = pd.DataFrame({
#     'Department': ['HR', 'HR', 'IT', 'IT', 'Sales'],
#     'Gender': ['M', 'F', 'M', 'F', 'F'],
#     'Salary': [50000, 52000, 60000, 58000, 55000]
# })

# pivot = pd.pivot_table(df, values='Salary', index='Department', columns='Gender', aggfunc='mean')
# print(pivot)
# print()
# print(pd.crosstab(df['Department'], df['Gender']))
# print()
# print(pd.crosstab(df['Gender'], df['Department']))


# sales = pd.DataFrame({
#     'Region': ['East', 'East', 'West', 'West'],
#     'Product': ['Pen', 'Notebook', 'Pen', 'Notebook'],
#     'Revenue': [100, 150, 200, 250]
# })

# grouped = sales.groupby(['Region','Product'])['Revenue'].agg(['sum'])
# print(grouped)





# MATPLOTLIB

# sales = pd.Series([100, 120, 150, 170], index=['Q1', 'Q2', 'Q3', 'Q4'])
# sales.plot(kind='line', title='Quarterly Sales')
# plt.ylabel('Revenue')
# plt.show()


# sales_data = pd.DataFrame({
#  'Product': ['Pen', 'Notebook', 'Eraser'],
#  'Sales': [150, 200, 80]
# })
# sales_data.set_index('Product')['Sales'].plot(kind='bar', title='Product Sales')
# plt.ylabel('Units Sold')
# plt.show()


# df = pd.DataFrame({
#  'Hours_Studied': [1, 2, 3, 4, 5],
#  'Score': [50, 55, 65, 70, 80]
# })
# df.plot(kind='scatter', x='Hours_Studied', y='Score', title='Study Time vs Score')
# plt.show()


# ages = pd.Series([22, 25, 27, 25, 30, 35, 40, 22, 28])
# ages.plot(kind='hist', bins=5, title='Age Distribution')
# plt.xlabel('Age')
# plt.show()


# x = np.array([1,2,3,4,5])
# y = x**2
# plt.scatter(x, y)
# x = np.array([0,-1,-2,-3,-4,-5])
# y = x**2
# plt.scatter(x, y)   
# plt.show()