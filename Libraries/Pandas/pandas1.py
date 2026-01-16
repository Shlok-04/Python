import pandas as pd
# s = pd.Series([10, 20, 30])
# print(s)
# print()

# data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
# df = pd.DataFrame(data)
# print(df)
# print()

# data = {'City': ['New York', 'Paris', 'London'], 'Population': [8.4, 2.1, 8.9]}
# df = pd.DataFrame(data)
# print(df)
# print()

# df = pd.read_csv('csv1.csv')
# print(df)
# print()
# print(df.describe())
# print()
# print(df.dtypes)
# print()
# print(df.columns)
# print()
# print(df.shape)

# print(df['name'])
# print()
# print(df[['name','maths']])
# print()

# print(df.loc[2:5,'name':])
# print(df.loc[2:5,'maths'])
# print(df.loc[2:3,'name':'maths'])

# print(df.iloc[2:5,-1])
# print(df.iloc[2:5,:])


# print()
# print()
# print(df[df['maths']>df['maths'].mean()])

# print()
# print()
# print(df[(df['maths']>df['maths'].mean())  & (df['gender']=='female')] )


data = {
    'Name': ['John', 'Anna', None],
    'Score': [85, None, 90],
    'Grade': ['A', None, 'B']
}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data)
print(df)
# print()
# print()
# print(df.isnull().sum())
# df['Score'] = df['Score'].fillna(df['Score'].mean())
# print()
# print()
# print(df)
print()
print()

# newdf = df
# print(newdf)
# print()
# print()
# newdf = newdf.drop(columns=['Grade'])
# df.drop(columns=['Grade'],inplace=True)
# print(newdf)
# print()
# print()
# print(df)
# print()
# print()

# df.dropna(subset=['Name'],inplace=True)
# print(df)

# print() 
# print() 
# print(df1)
# print() 
# print() 
# df1.dropna(inplace=True)
# print(df1)

