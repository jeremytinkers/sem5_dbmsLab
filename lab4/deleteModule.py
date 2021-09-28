import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="needsjesus",
  database="lab4"
)

cursor1 = mydb.cursor()

def deleteFn():
    #Q4 : Delete:-
    print("Q4. DELETE OPERATION")
    print("")

    print("Enter the unique seatno registration that you would like to delete")
    user_seatNo = input()

    #show table data before:-

    print("")
    print("Table Data Before:-")
    cursor1.execute("select * from railres")
    print("")
    for i in cursor1:
        print(i)


    delete_sql = "delete from railres where seatno = %s"
    delete_val = (user_seatNo,)
    cursor1.execute(delete_sql, delete_val)

    mydb.commit()

    #show table data after:-

    print("")
    print("Table Data After:-")
    cursor1.execute("select * from railres")
    print("")
    for i in cursor1:
        print(i)
    print("")