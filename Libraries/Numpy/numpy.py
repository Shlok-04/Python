import numpy as np
# arr = np.array([10, 20, 30])
# print(arr.shape)
# print(arr.dtype)

# arr_1d = np.array([1,2,3,4,5,6])
# print(arr_1d)

# arr_2d = np.array([[1,2],[3,4],[5,6]])
# print(arr_2d)

# print(arr_1d.shape)
# print(arr_1d.dtype)

# print(arr_2d.shape)
# print(arr_2d.dtype)

# print()

# print(np.zeros((2, 3)))
# print()
# print(np.ones((3, 2)))   
# print()
# print(np.eye(3))
# print()
# print(np.arange(0, 10, 2))
# print()
# print(np.linspace(0, 1, 5))
# print()


# arr = np.array([1,2,3],dtype=float)
# print(arr.dtype)
# print()

# arr1 = np.arange(1,11)
# print(arr1)

# print(arr1[1:9])
# print(arr1[1:10])
# print(arr1[1:100])
# print(arr1[1:len(arr1)])


# print(arr1[1:10:2])


# arr_2 = np.array([[11, 12, 13],[21, 22, 23],[31, 32, 33]])
# print(arr_2)
# print()
# print(arr_2[1:2,0:3])
# print()
# print(arr_2[:2,:2])
# print()


# arr = np.array([1,2,3,4,5])
# print(arr)
# arr = arr*10
# print(arr)
# arr[1:3] = [2,3]
# print(arr)
# arr[0:len(arr)] = [0]
# print(arr)


# arr2 = np.array([[11, 12, 13],[21, 22, 23],[31, 32, 33]])
# print(arr2)
# print()
# arr2[1] = [10,20,30]
# print(arr2)
# print()
# arr2[:,1] = 1
# print(arr2)

# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6])
# print(a1*a2)
# print(a1/a2)

# print()

# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6,7])
# print(a1*a2)

# arr = np.array([1, 4, 9, 16])
# print(np.sqrt(arr))   
# print(np.exp(arr))    
# print(np.log(arr))
# print(np.sum(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.mean(arr))


# a2 = np.array([[1,2,3],[4,5,6],[6,7,8]])
# print(a2)
# print()
# print(a2.sum(axis=1))
# print()
# print(a2.sum(axis=0))
# print()
# print(a2.mean(axis=1))
# print()


# arr = np.array([1,2,3,4,5,6])
# # print(arr.mean())
# # print(np.mean(arr))
# arr = arr*3
# print(arr.mean())
# print(arr.sum())
# print(arr.std())



# a = np.array([[1, 2, 3],[4, 5, 6]])
# b = np.array([10, 20, 30])
# print(a + b)

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(b/a)
# print(np.sqrt(a))


# arr = np.array([10, 20, 30, 40, 50])
# print(arr > 25)
# print(arr[arr>25])


# arr = np.array([5, 10, 15, 20, 25])
# condition = arr % 2 == 0
# print(condition)
# print(arr[condition])
# print(arr[arr%2==0])


# arr = np.arange(1,11)
# print(arr)
# print(arr[(arr>2) & (arr<10) & (arr%2==0)])


# arr = np.array([10, 15, 20, 25, 30])
# print(arr[arr>18])
# arr[arr<18] = -1
# print(arr)


# data = np.genfromtxt('csv1.csv',delimiter=',')
# print(data)
# print()
# data = np.genfromtxt('csv1.csv',delimiter=',',skip_header=1)
# print(data)
# print()
# data = np.genfromtxt('csv1.csv',delimiter=',',skip_header=1,usecols=(2,3))
# print(data)
# print()
# print(np.mean(data,axis=1))
# print()
# print(np.mean(data,axis=0))
# summary_data = np.mean(data,axis=0)
# print()
# np.savetxt('output.csv', summary_data, delimiter=',', fmt='%.2f')


# a = np.array([1, 2, 3, 4, 5, 6])
# b = a.reshape((2, 3))
# print(b)

# a = np.array([[1,2],[3,4],[5,6]])
# b = a.flatten()
# print(b)

# a = np.array([1, 2])
# b = np.array([3, 4])
# c = np.vstack((a, b))
# print(c)

# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# c = np.vstack((a, b))
# print(c)

# a = np.array([[1], [2]])
# b = np.array([[3], [4]])
# c = np.hstack((a, b))
# print(c)


a = np.arange(1,13)
print(a)
b = a.reshape(3,4)
print(b)
c = b.flatten()
print(c)
print()
a = np.array([[1,2,3],[10,20,30]])
b = np.array([[4,5,6],[40,50,60]])
c = np.vstack((a,b))
print(c)
c = np.hstack((a,b))
print(c)


print(np.random.rand(3))
print(np.random.randint(0,10,2))
arr = np.array([10, 20, 30, 40])
choice = np.random.choice(arr, 2)
print(choice)

# np.random.seed(42)
print(np.random.randint(1,10,2))


arr = np.random.randint(0,2,100)
ch = 0
ct = 0
for i in arr:
    if i==0:
        ct+=1
    else:
        ch+=1
print()
print(ch,ct)
ch = np.sum(arr==1)
ct = np.sum(arr==0)
print(ch,ct)