import mysql.connector
m=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shana@321",
    database="employee"
)
c=m.cursor()
#c.execute("create table empl(name varchar(100) primary key not null,age int,salary int)")
#m.commit()
#c.close()
def list_emp():
    c.execute("Select * from empl")
    rows=c.fetchall()
    print("Name  Age  Salary")
    for rows in rows:
        for col in rows:
            print(col,end='  ')
        print()
def add_emp(name,age,sal):
    s="insert into empl(name,age,salary)values(%s,%s,%s)"
    v=[(nm,age,sal)]
    c.executemany(s,v)

    m.commit()
def edit_emp(n,n_n,n_a,n_s):
    s=("update empl set name=%s,age=%s,salary=%s where name=%s")
    val=[(n_n,n_a,n_s,n)]
    c.executemany(s,val)
    m.commit()
def del_emp(n):
    s=("delete from empl where name=%s")
    val=[(n,)]
    c.executemany(s,val)
    m.commit()
ch=1
while(ch<5):
    print("\n1.List\n2.Add\n3.Edit\n4.Delete\n5.Exit")
    ch=int(input("Please select your input: "))
    if ch==1:
        print("\nThe list of employees")
        list_emp()
    elif ch==2:
        nm=input("Enter the name: ")
        age=int(input("Enter the age: "))
        sal=int(input("Enter the salary: "))
        add_emp(nm,age,sal)
    elif ch==3:
        n=input("Enter the name of the employee to be edited: ")
        n_n=input("Enter the new name: ")
        n_a=int(input("Enter the new age: "))
        n_s=int(input("Enter the new salary: "))
        edit_emp(n,n_n,n_a,n_s)
        print("\nEmployee Details Edited Successfully..!!")
    elif ch==4:
        n=input("Enter the name of the employee to be deleted: ")
        del_emp(n)
        print("\nEmployee Details Deleted Successfully...!!")
    else:
        if ch==5:
            continue
        print("\nInvalid")