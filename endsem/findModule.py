import mysql.connector
import config

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=config.adminPassword,
  database="lab4"
)

cursor1 = mydb.cursor()

def findFn():
#Q2: Find module
    print("Q2. FIND OPERATION")
    print("")

    print("Enter patient id :-")
    pid=input()

    sql = "select * from patient where pid =%s"
    pid_input = (pid, )
    cursor1.execute(sql, pid_input)

    print("")
    print("The tuple of the name you asked for:-")
    for i in cursor1:
        print(i)
    print("")