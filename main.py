# Project on Employee Management System

import mysql.connector as driver
from database import create_database, show_databases
from employee_record import create_table, show_tables, insert_record, update_record, delete_record,search_record, display_record
import sys

def menu():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print()
        print()
        print("==============================")
        print("       PB ENTERPRISE")
        print("==============================")
        print("  ........MENU.......  ")
        print("1. CREATE DATABASE")
        print("2. SHOW DATABASES")
        print("3. CREATE TABLE")
        print("4. SHOW TABLES")
        print("5. INSERT RECORD")
        print("6. UPDATE RECORD")
        print("7. DELETE RECORD")
        print("8. SEARCH RECORD")
        print("9. DISPLAY RECORD")
        print()
        print()
        choice=int(input("Enter the choice (1-9) : "))
        if(choice==1):
            create_database()
        elif(choice==2):
            show_databases()
        elif(choice==3):
            create_table()
        elif(choice==4):
            show_tables()
        elif(choice==5):
            insert_record()
        elif(choice==6):
            update_record()
        elif(choice==7):
            delete_record()
        elif(choice==8):
            search_record()
        elif(choice==9):
            display_record()
        else:
            print("Wrong Choice.")
        print ("==========================================================")
        print("THANK YOU, HAVE A NICE DAY")
        loop=input("Do you want more try? Press 'y' to continue...")
    else:
        sys.exit()

menu()

