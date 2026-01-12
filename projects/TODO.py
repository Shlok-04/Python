def printlist():
    with open('todo.txt', 'r') as file:
        content = file.read()
        print(content)
        # print()

def add(task):
    with open('todo.txt', 'a') as file:
        file.write(task + '\n')
        # print()
    
def clearlist():
    with open('todo.txt','w') as file:
        pass



# a=0
while True:
    a = int(input("Enter 0 to exit and 1 to continue : ")) 
    if a==1:
        s = input("Enter 'a' to add task, 'c' to clear list, 'p' to printlist : ")
        if s=='p':
            printlist()
        elif s=='a':
            t = input("Write task : ")
            add(t)
            printlist()
        elif s=='c':
            clearlist()
        else:
            print("INVALID INPUT , TRY AGAIN!!")
    else:
        break






    