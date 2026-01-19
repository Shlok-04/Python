from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# x = np.array([[1],[2],[3],[4]])
# y = np.array([2,4,6,8])

# lr = LinearRegression()

# lr.fit(x,y)

# new_output = lr.predict([[5]])
# print(new_output)


# data = pd.DataFrame({
#   'experience': [1, 2, 3, 4, 5],
#   'salary': [30000, 35000, 40000, 45000, 50000]
# })

# x = data[['experience']]
# y = data['salary']

# lr = LinearRegression()
# lr.fit(x,y)

# new_output = lr.predict([[6]])
# print(new_output)


data = pd.DataFrame({
    'RAM(GB)' : [2,4,6,8],
    'PRICE' : [8000, 12000, 18000, 24000]
})

x = data[['RAM(GB)']]
y = data['PRICE']
lr = LinearRegression()
lr.fit(x,y)
xtest = [[10],[12]]
new_output = lr.predict(xtest)
print(new_output)
