import numpy as np

# arr = np.random.randint(1,101,25)
# res = arr.reshape(5,5)
# print(res)
# print()

arr = np.random.randint(1,30,9)
print(arr)
# print()
# newarr = arr[arr%2==0]
# print(newarr)
# print(f"Mean : {np.mean(arr)}")
# print("Median : ",np.median(arr))
# print("Standard deviation : ",np.std(arr))

# norm_arr = arr/(np.sum(arr))
# print(norm_arr)
# print(np.sum(norm_arr))

# idx = -1
# max_num = np.min(arr) - 1
# print(max_num)

# for i,num in enumerate(arr):
#     if num>max_num:
#         max_num = num
#         idx = i
# print(f"Max number is : {max_num} and its index is {idx}")
# idx = -1
# max_num = np.min(arr) - 1
# for i in range(len(arr)):
#     if arr[i]>max_num:
#         max_num = arr[i]
#         idx = i
# print(f"Max number is : {max_num} and its index is {idx}")
# print()

# a = np.random.randint(1,10,4).reshape(2,2)
# b = np.random.randint(1,10,4).reshape(2,2)
# print(a)
# print()
# print(b)
# print(a*b)
# print()
# print(np.matmul(a,b))
# print()
# print(a@b)
# print()

# print(arr)
# print("Average ",np.mean(arr) )
# print("All the values greater than the average", arr[arr> np.mean(arr)])
# print()

# print(arr)
# res = arr.reshape(3,3)
# print("Reshaped array : ")
# print(res)
# print()
# print("Sorting row wise and column wise : ")
# print(np.sort(res,axis=1))
# print()
# print(np.sort(res,axis=0))


# na = np.array([60,1,2,3,4,5,15,45])
# print(na)
# na = na[na%3==0]
# na = na[na%5==0]
# print(na)
# print()
# na = np.array([60,1,2,3,4,5,15,45])
# l = [3,5]
# for i in l:
#     na = na[na%i==0]
# print(na)

# print(arr)
# res = arr.reshape(3,3)
# print("Reshaped array : ")
# print(res)
# print()
# print("row wise and column wise sum : ")
# print(np.sum(res,axis=1))
# print()
# print(np.sum(res,axis=0))
# print()

# print("To remove duplicates using Unique : ")
# ar = np.array([8,8,9,1,1,2,2,3,3,3,4,5,5,6,7,7])
# print(np.unique(ar))


# from collections import Counter
# ar = [8,8,9,1,1,2,2,3,3,3,4,5,5,6,7,7]
# counts = Counter(ar)
# # print(counts)
# newlist = []
# for i in ar:
#     if counts[i]!=-1:
#         newlist.append(i)
#         counts[i]=-1
# print("To remove duplicates using count of numbers : ")
# print(newlist)

# newlist = []
# for i in ar:
#     if i not in newlist:
#         newlist.append(i)
# print("To remove duplicates using 'not in' condition : ")
# print(newlist)


# na = np.array([1,np.nan,2,3,4,np.nan,5,6,7,np.nan])
# print(type(na))
# na[np.isnan(na)] = np.nanmean(na)
# print(na)

# a = np.array([[1,2,3],[10,20,30]])
# b = np.array([[4,5,6],[40,50,60]])
# c = np.vstack((a,b))
# print(c)
# c = np.hstack((a,b))
# print(c)


# a = np.array([[4, 2],[2, 1]])
# e = np.linalg.eigvals(a)
# print(a)
# print("\nEigenvalues:")
# print(e)
# # (4-a) (1-a) - 2*2 = 0
# # 4-4a-a+a^2 = 4
# # a^2 - 5a = 0
# # a = 0 , a = 5