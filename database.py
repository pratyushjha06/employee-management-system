import mysql.connector as driver

def create_database():
    con=driver.connect(host='localhost',user='root', passwd='123456')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create database if not exists employee')
    print()
    print("Database Created")
    con.close()


def show_databases():
    con=driver.connect(host='localhost',user='root',passwd='123456')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show databases')
    for i in cur:
        print(i)
    con.close()
