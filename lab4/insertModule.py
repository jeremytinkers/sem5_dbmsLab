import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="needsjesus",
  database="lab4"
)
cursor1 = mydb.cursor()

def insertFn():
    #Q1: insert module:-

    print("Q1. INSERT OPERATION")
    print("")
    
    #show table data before:-
    print("Table Before Insertion:-")
    cursor1.execute("select * from railres")
    for i in cursor1:
        print(i)
    print("")

    print("Enter Seat Number:- ")
    seatNo = input()
    print("Enter Name:- ")
    name = input()
    print("Enter Source Address:- ")
    src = input()
    print("Enter Destination Address:- ")
    dest = input()

  
    insert_sql = "INSERT INTO railres (seatno, name, source, destination) VALUES (%s,%s,%s, %s)"
    insert_variables = (seatNo,name,src, dest)

    cursor1.execute(insert_sql, insert_variables)
    print(cursor1.rowcount, "record inserted.")


    mydb.commit()

    #show table data:-
    print("")
    print("Table After Insertion:-")
    cursor1.execute("select * from railres")
    print("")
    for i in cursor1:
        print(i)
    print("")
