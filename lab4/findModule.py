import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="needsjesus",
  database="lab4"
)
cursor1 = mydb.cursor()

def findFn():
#Q2: Find module
    print("Q2. FIND OPERATION")
    print("")

    print("Enter the name for which you want to see reservation details :-")
    findName=input()

    sql = "select * from railres where name =%s"
    input_name = (findName, )
    cursor1.execute(sql, input_name)

    print("")
    print("The tuple of the name you asked for:-")
    for i in cursor1:
        print(i)
    print("")