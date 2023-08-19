import mysql.connector as driver

def create_table():
    con=driver.connect(host='localhost',user='root',passwd='123456',database='employee')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute("create table if not exists emp(emp_id integer primary key, Name varchar(50),Phn_no int(50), Designation varchar(50), Salary float)")
    print()
    print("Table Created -> EMP")
    cur.execute('DESC emp')
    for i in cur:
        print(i)
    con.close()
    
def show_tables():
    con=driver.connect(host='localhost',user='root',passwd='123456',database='employee')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show tables')
    for i in cur:
        print(i)
    con.close()

def insert_record():
    con=driver.connect(host='localhost',user='root',passwd='123456',database='employee')
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        ID=int(input("ENTER EMPLOYEE ID : "))
        NAME=input("ENTER NAME OF EMPLOYEE : ")
        PHN_NO=int(input("ENTER PHONE NUMBER : "))
        DESIGNATION=input("ENTER THE DESIGNATION OF EMPLOYEE : ")
        SALARY=float(input("ENTER EMPLOYEE SALARY : "))
        query1="INSERT INTO emp VALUES({},'{}',{},'{}',{})".format(ID,NAME,PHN_NO,DESIGNATION,SALARY)
        cur.execute(query1)
        con.commit()
        print('Record Inserted')
        con.close()
    else:
        print("Error : Not Connected")

def update_record():
    con=driver.connect(host='localhost',user='root',passwd='123456',database='employee')
    cur=con.cursor()
    d=int(input("Enter Employee ID for update record : "))
    ID=int(input("ENTER NEW EMPLOYEE ID : "))
    NAME=input("ENTER NEW NAME OF EMPLOYEE : ")
    PHN_NO=int(input("ENTER PHONE NUMBER : "))
    DESIGNATION=input("ENTER THE DESIGNATION OF EMPLOYEE : ")
    SALARY=float(input("ENTER EMPLOYEE SALARY : "))
    query1="update emp set emp_id=%s, Name='%s',Phn_no=%s, Designation='%s', Salary=%s where emp_id=%s" %(ID,NAME,PHN_NO,DESIGNATION,SALARY,d)
    cur.execute(query1)
    con.commit()
    print("Record Updated")
    con.close()

def delete_record():
    con=driver.connect(host='localhost',user='root',passwd='123456',database='employee')
    cur=con.cursor()
    d=int(input("Enter Employee ID for deleting record : "))
    query1="delete from emp where emp_id={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def search_record():
    con=driver.connect(host='localhost',user='root',passwd='123456',database='employee')
    cur=con.cursor()
    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO SEARCH RECORD: ")
    print("1. ACCORDING TO ID")
    print("2. ACCORDING TO NAME")
    print("3. ACCORDING TO PHN_NO")
    print("4. ACCORDING TO DESIGNATION")
    print("5. ACCORDING TO SALARY")
    print()
    choice=int(input("ENTER THE CHOICE (1-5) : "))
    if choice==1:
          d=int(input("Enter Employee ID which you want to search : "))
          query1="select * from emp where emp_id=%s" %(d)
    elif choice==2:
          name=input("Enter Employee Name which you want to search : ")
          query1="select * from emp where Name='%s'" %(name)
    elif choice==3:
          phn=float(input("Enter Employee Phone number which you want to search : "))
          query1="select * from emp where Phn_no=%s" %(phn)
    elif choice==4:
          desg=float(input("Enter Employee Designation which you want to search : "))
          query1="select * from emp where Designation=%s" %(desg)
    elif choice==5:
          sal=float(input("Enter Employee Salary which you want to search : "))
          query1="select * from emp where Salary=%s" %(sal)
    else:
          print("Wrong Choice")
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    for i in rec:
        print(i)
    print("Record Searched")
    con.close()

def display_record():
    con=driver.connect(host='localhost',user='root',passwd='123456',database='employee')
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from emp')
        rec=cur.fetchall()
        count=cur.rowcount
        for i in rec:
            print(i) 
        print("+-------------------------------------------------+")
        print("    Total no. of records are : ",count)    
        print("+-------------------------------------------------+")
        #for i in rec:
        #    print(i)
        con.close()
    else:
        print("Error : Database Connection is not success" )








