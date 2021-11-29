import mysql.connector
import config

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=config.adminPassword,
  database="lab4"
)

cursor1 = mydb.cursor()

def insertFn():
    #Q1: insert module:-

    print("Q1. INSERT OPERATION")
    print("")
    
    #show table data before:-
    print("Table Before Insertion:-")
    cursor1.execute("select * from patient")
    for i in cursor1:
        print(i)
    print("")

    print("Enter Patient id:- ")
    pid = input()
    print("Enter Name:- ")
    name = input()
    print("Enter diagnosis:- ")
    diagnosis = input()
    print("Enter Contact:- ")
    contact = input()
    print("Enter date of admission:- ")
    doa = input()

#create table patient(pid int primary key, name varchar(30), diagnosis varchar(30), contact int, doa date)
  
    insert_sql = "INSERT INTO patient (pid, name, diagnosis, contact, doa) VALUES (%s,%s,%s, %s, %s)"
    insert_variables = (pid, name, diagnosis, contact, doa)

    cursor1.execute(insert_sql, insert_variables)
    print(cursor1.rowcount, "record inserted.")


    mydb.commit()

    #show table data:-
    print("")
    print("Table After Insertion:-")
    cursor1.execute("select * from patient")
    print("")
    for i in cursor1:
        print(i)
    print("")
