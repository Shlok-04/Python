# 1) Use lambda to create a function that multiplies a number by 3.
list1 = [1,2,3,4,5]
multiply = lambda x : x*3
newlist = []
for i in list1:
    newlist.append(multiply(i))
print(newlist)

# 2) Given a list of numbers, use map() with lambda to get their cubes.
cubes = list(map(lambda x: x**3, list1))
print(cubes)

# 3) Use filter() to select names that start with the letter 'A'.
list1 = ['baba','abab','A','aA']
with_a = list(filter(lambda x: x[0]=='a', list1))
print(with_a)


# 4) Use reduce() to find the maximum number in a list.
from functools import reduce
list1 = [5,3,7,9,4,5]
max_num = reduce(lambda x,y : max(x,y) , list1)
print(max_num)

# 5) Write a program that takes a list of words and filters only those longer than 5 characters.
words = ["Python", "is", "fun","apple", "banana", "kiwi", "plum"]
filtered_words = list(filter(lambda x: len(x)>5, words))
print(filtered_words)


# 6) Create a pipeline using map, filter, and lambda to:
# - square numbers
# - filter out odd results
# - then sum them with reduce

# Example input: [1, 2, 3, 4, 5]
# Expected output: 20
list1 = [1,2,3,4,5]
sq_list = []
square = lambda x : x*x
for i in list1:
    sq_list.append(square(i))
print(sq_list)
filter_odd = list(filter(lambda x : x%2==0 , sq_list))
sum = reduce(lambda x,y : x+y , filter_odd)
print(sum)