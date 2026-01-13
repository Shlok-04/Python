# class Dog:
#     def bark(self):
#         print("woof woof")

# dog = Dog()
# print(dog.bark())


# class Car:
#     def __init__(self,brand,colour):
#         self.brand = brand
#         self.colour = colour
#     def car_brand(self):
#         print(f"The brand of the car is {self.brand}")
#     def car_colour(self):
#         print(f"The car is of {self.colour} colour.")
# car = Car("Toyota","Blue")
# print(car.brand)
# print(car.colour)
# print(car.car_brand())


# class Book:
#     def __init__(self,name,author):
#         self.name = name
#         self.author = author
#     def name_and_author(self):
#         print(f"The name of the book is {self.name} and it is written by {self.author}")
# book1 = Book("Physics","HC Verma")
# book1.name_and_author()


# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius*self.radius
    
# circle1 = Circle(3)
# print(f"The area of the circle is {circle1.area()}")


# class Employee:
#     def __init__(self,salary):
#         self.salary = salary
#     def total_salary(self):
#         print("The total salary is ",self.salary)
#     def salary_with_bonus(self):
#         print("The total salary with bonus is ",1.1*self.salary)

# emp1 = Employee(10000)
# emp1.total_salary()
# emp1.salary_with_bonus()

# class BankAcc:
#     def __init__(self,balance):
#         self.balance = balance
#         self.withdraw = 0
#         self.deposit = 0
#     def dep(self,amount):
#         self.balance = self.balance + amount
#         print(f"Your current balance is {self.balance}")
#     def wit(self,amount):
#         if self.balance >= amount:
#             self.balance = self.balance - amount
#             print("Your current balance is ",self.balance)
#         else:
#             print("Your current balance is 0")

# acc1 = BankAcc(1000)
# acc1.dep(100)
# acc1.wit(900)


# INHERITANCE
# class Animal:
#     def sound(self):
#         print("Different animal makes different sounds")
# class Dog(Animal):
#     def bark(self):
#         print("Woof Woof")

# a1 = Animal()
# a1.sound()
# d1 = Dog()
# d1.sound()
# d1.bark()


# class Animal:
#     def sound(self):
#         print("Different animal makes different sounds")
# class Dog(Animal):
#     def sound(self):
#         print("Woof Woof")

# a1 = Animal()
# a1.sound()
# d1 = Dog()
# d1.sound()


# class Student:
#     def __init__(self,name):
#         self.name = name

# class St_Grade(Student):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade = grade

# s = St_Grade("Alice","A")
# print(s.grade)
# print(s.name)
# print()

# s1 = Student("Name")
# sg1 = St_Grade(s1.name,"B")
# print(sg1.grade)
# print(sg1.name)


