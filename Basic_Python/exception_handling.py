# try:
#     x = int(input("Enter number 1 : "))
#     y = int(input("Enter number 2 : "))
#     z = x/y
#     print(z)
# except ZeroDivisionError:
#     print("Value of number 2 cannot be zero")


# x = int(input("Enter a number : "))
# if x < 0 or x>100:
#     raise ValueError("Enter a number between 0 and 100")
# print("Number set to:", x)


# try:
#     value = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input.")
# else:
#     print("You entered:", value)
# finally:
#     print("Execution completed.")


# nums = [10,20]
# try:
#     print(nums[2])
# except IndexError:
#     print("Index out of bound")


# try:
#     file = open('file.txt', 'r')
#     content = file.read()
# except:
#     print("No such file exists")
# else:
#     print("File content : ",content)
# finally:
#     print("Exection complete")