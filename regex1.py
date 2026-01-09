# import re
# str = input("Enter a string : ")
# upper = r"[A-Z]"
# lower = r"[a-z]"
# digit = r"\d"
# sc = r"[!@#$%^&]"
# if len(re.findall(upper,str))>=1 and len(re.findall(lower,str))>=1 and len(re.findall(digit,str))>=1 and len(re.findall(sc,str))>=1:
#     print("The password is strong")
# else :
#     print("The password is weak") 



# str = input("Enter a string: ")
# pattern = r"[A-Za-z0-9]+@[A-Za-z]+\.(org|com)$"
# match = re.fullmatch(pattern, str)
# if match:
#     print("Valid email")
# else:
#     print("Invalid email")


# str = input("Enter a different date : ")
# pattern = r"[0-3]{0,1}[0-9]{1}-[0-1]{0,1}[0-9]{1}-[1-2]{1}[0-9]{1}[0-9]{1}[0-9]{1}"
# st = re.findall(pattern,str)
# print(st)



# str = input("Enter your number : ")
# pattern = r"^(\+91|0)\d{10}$"
# print(re.fullmatch(pattern,str))
# if re.fullmatch(pattern,str):
#     print("Valid number")
# else:
#     print("Invalid number")


# str = input("Enter IPv4 address : ")
# pattern = r"[0-2]{0,1}[0-9]{0,1}[0-9]{1}\.[0-2]{0,1}[0-9]{0,1}[0-9]{1}\.[0-2]{0,1}[0-9]{0,1}[0-9]{1}\.[0-2]{0,1}[0-9]{0,1}[0-9]{1}"
# if re.findall(pattern,str):
#     print("Valid")
# else:
#     print("Invalid")


# str = input("Enter write you html code : ")
# str = "hello <h1><h2> <h3> h4 h5 <em>"
# pattern = r"<(h[1-5]|b|br|i|p|em)>"
# print(re.findall(pattern,str))


# str = "21 21.1 3.3 22"
# str = input("Enter a string of int and float numbers")
# pattern = r"[0-9]+\.[0-9]+ "
# print(re.findall(pattern,str))


# str = "https://www.hostinger.com/tutorials/what-is-a-url"
# # str = input("Enter a URL : ")
# pattern = r"(http|https)://www\.[a-z]+\.com/[a-z]+/[A-Za-z0-9-]+"
# print(re.search(pattern,str).group())
