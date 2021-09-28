import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="needsjesus",
  database="lab4"
)
cursor1 = mydb.cursor()

def updateFn():
    #Q3: Update
    print("Q3. UPDATE OPERATION")
    print("")

    print("Enter the unique seat no of the passenger whose destination is to be changed")
    user_seatNo = input()

    #show table tuple before:-

    sql = "select * from railres where seatno =%s"
    val = (user_seatNo, )
    cursor1.execute(sql, val)

    print("")
    print("Passenger data before updation:-")
    for i in cursor1:
        print(i)


    print("Enter the new Destination")
    newDest = input()

    update_sql = "UPDATE railres SET destination = %s WHERE seatno = %s"
    update_val = (newDest, user_seatNo)
    cursor1.execute(update_sql, update_val)

    mydb.commit()

    #show table data:-

    cursor1.execute("select * from railres")
    print("")
    print("Updated Table:-")
    for i in cursor1:
        print(i)
    print("")