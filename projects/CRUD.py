import sqlite3

conn = sqlite3.connect("CRUD.db")
cursor = conn.cursor()

# cursor.execute("drop table if exists student1")

cursor.execute("""
               create table if not exists student1(
               name text,
               age integer,
               marks integer
               )
               """)

while True:
    s = input("Enter \n'a' to add\n'p' to print\n'd' to delete\n'u to update'\n'anything' to exit : \n")
    if s=='a':
        name = input("Enter you name : ")
        age = int(input("Enter you age : "))
        marks = int(input("Enter you marks : "))
        cursor.execute("""
        insert into student1 (name, age, marks)
        values (?, ?, ?)
        """, (name, age, marks))

    elif s=='d':
        name = input("Enter you name of the studnet whose content you want to delete : ")
        age = int(input("Enter you age of the studnet whose content you want to delete : "))
        marks = int(input("Enter you marks of the studnet whose content you want to delete : "))
        cursor.execute("""
        delete from student1
        where name = ? and age=? and marks=?
                       """,(name,age,marks))
        
    elif s=='p':
        cursor.execute("select * from student1")
        rows = cursor.fetchall()
        print(rows)
    
    elif s=='u':
        w = input("Enter what do you want to update : ")
        if w=='name':
            n = input("Enter the new name : ")
            print("Other details of the student : ")
            a = int(input("Enter the age of the student whose name you want to update : "))
            m = int(input("Enter the marks of the student whose name you want to update : "))
            
            cursor.execute("""
            update student1
            set name = ?
            where age = ? and marks = ?
            """,
            (n, a, m)
            )

        elif w=='age':
            a = int(input("Enter the new age : "))
            print("Other details of the student : ")
            n = input("Enter the name of the student whose age you want to update : ")
            m = int(input("Enter the marks of the student whose age you want to update : "))

            cursor.execute("""
            update student1
            set age = ?
            where name = ? and marks = ?
            """,
            (a, n, m)
            )

        elif w=='marks':
            m = int(input("Enter the new marks : "))
            print("Other details of the student : ")
            n = input("Enter the name of the student whose marks you want to update : ")
            a = int(input("Enter the age of the student whose marks you want to update : "))

            cursor.execute("""
            update student1
            set marks = ?
            where name = ? and age = ?
            """,
            (m, n, a)
            )

        else:
            print("NO SUCH COLUMN EXISTS")

    else:
        break
